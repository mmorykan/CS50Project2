class Message:
    def __init__(self, username, time, content=None, image=None):
        self.username = username
        self.time = time
        self.content = content
        self.image = image


    def get_username(self):
        return self.username


    def get_time(self):
        return self.time


    def get_content(self):
        return self.content


    def get_image(self):
        return self.image


class Channel:
    def __init__(self, channel_name):
        self.channel_name = channel_name
        self.messages = []


    def get_name(self):
        return self.channel_name


    def get_messages(self):
        return self.messages


    def add_message(self, message):
        if len(self.messages) == 100:
            self.messages.pop()

        self.messages.append(message)

