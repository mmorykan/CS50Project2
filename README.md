# Project 2

Web Programming with Python and JavaScript


This project is a chat server where anyone can create channels and join them and chat with anyone else.

Every html file extends layout.html where the css files are linked as well as the socket js file.
The index.html file displays the login page, taking the user to the channels page.
The channels.html file displays the list of all channels as links to their chat rooms. Also, a user can add a channel to the list on this page.
The channel.html file displays a single channel page with a list of up to 100 of the most recent messages posted in this chat. A user can post new messages here as well as return back to the page of all channels.
The error.html file displays an error whenever a user tries to continue without providing a username or whenever a user tries to add a channel with the same name as another channel.
The index.js file contains all the javascript websocket content which is displayed on the channel.html page.
The styles.css file contains the styling for headers and the channels button on the channel pages.
The application.py file contains all the flask functions need to display all html and files.
The channel_content.py file contains a message class and a channel class for more organization.

My personal touch for this project was providing a means of sending images back and forth in a channel.