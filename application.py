import os

from flask import Flask, render_template, session, request
from flask_session import Session
from flask_socketio import SocketIO, emit

from channel_content import Message, Channel
import time

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

channel_list = []

@app.route("/")
def index():
    """
    Get the previous channel the user visited if it exists and also obtaint the users username if it exists
    """
    current_channel_id = session.get('channel_id')
    if current_channel_id is not None:
        return render_template('channel.html', messages=channel_list[current_channel_id].get_messages())

    return render_template('index.html', username=session.get('username'))


@app.route("/channels", methods=["GET", "POST"])
def channels():
    """
    List all channels 
    Add a channel by user input
    """
    
    channel_name = request.form.get('channel_name')
    username = request.form.get('name') or session.get('username')

    if not username:
        return render_template('error.html', heading='Incorrect username', message='Enter a username.')

    if channel_name:
        for channel in channel_list:
            if channel_name == channel.get_name():
                return render_template('error.html', heading='Channel already exists', message='This channel name is already taken.')

        channel_list.append(Channel(channel_name))

    session['username'] = username
    return render_template('channels.html', channels=channel_list)


@app.route("/channels/<int:channel_id>")
def channel(channel_id):
    """
    Display all messages within the channel
    """
    session['channel_id'] = channel_id
    channel = channel_list[channel_id]

    return render_template('channel.html', messages=channel.get_messages(), name=channel.get_name())


@socketio.on("send message")
def send(message):
    """
    Broadcasts the message to all users
    Add new message to recent messages without saving more than 100 messages
    """
    content = message.get('content')
    image = message.get('data')
    message = Message(username=session['username'], time=time.strftime('%X'), content=content, image=image)
    
    channel_id = session['channel_id']
    channel = channel_list[channel_id]
    if message.get_content() or message.get_image():
        channel.add_message(message)
    
    emit("broadcast message", 
        {'username': message.get_username(), 'time': message.get_time(), 'content': message.get_content(), 'image': message.get_image()}, 
        broadcast=True)
