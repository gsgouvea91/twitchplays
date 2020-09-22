# This file is to protect your data, in case you want to adjust stuff in the main file while
# showing your screen in live, there is probably a more efficient way to do this but this also
# works.. so lol hehe, feel free to modify at your will.

class Config:

    def __init__(self):
        self._username ='<username>'
        self._token = '<oauth>'
        self._channel = '<channel>'
        self._channel1= '<channel1>'
        self._bot='MyBot'
        self._server = 'irc.chat.twitch.tv'
        self._port =  6667

    def getUsername(self):
        return self._username
    def getToken(self):
        return self._token
    def getChannel(self):
        return self._channel
    def getChannel1(self):
        return self._channel1      
    def getBot(self):
        return self._bot
    def getServer(self):
        return self._server
    def getPort(self):
        return self._port



