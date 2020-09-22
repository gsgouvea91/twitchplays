# I've been trhu some twitch plays tutorials and cobbled together this little bot to handle
# the job, is simple but it works, feel free to modify this code at will.
import socket
import keypresser
import keyholder
import config 
c = config.Config()
k = keypresser.Keypresser()

#Configurations and connect process, bot atm is fitted to enter 2 chats at the same time.
username = c.getUsername()
token = c.getToken()
channel = c.getChannel()
channel1= c.getChannel1()
bot= c.getBot()
server = c.getServer()
port = c.getPort()

s = socket.socket()
s.connect((server,port))
s.send(f"PASS {token}\n".encode('utf-8'))
s.send(f"NICK {username}\n".encode('utf-8'))
s.send(f"JOIN {channel}\n".encode('utf-8'))
s.send(f"JOIN {channel1}\n".encode('utf-8'))

# Joins chat.
def joinchat():
    Loading = True
    while Loading:
        readbuffer_join = s.recv(1024).decode('utf-8')
        for line in readbuffer_join.split("\n")[0: -1]:
            print(line)
            Loading = loadingComplete(line)
#Checks if bot entered the chat currently fited to enter 2 chats at the same time
def loadingComplete(line):
    if ("End of /NAMES list" in line):
        print("Bot has joined"+channel+"'s Channel\n")
        print("Bot has joined"+channel1+"'s Channel\n")
        sendMessage(s,"cool")
        return False
    else:
        return True
#Sends messages to chat, currently fitted to send messages to 2 chats at the same time
def sendMessage(s,message):
    messageTemp = "PRIVMSG " +channel+" :"+ message
    messageTemp1 = "PRIVMSG " +channel1+" :"+ message
    s.send((messageTemp+"\n").encode())
    s.send((messageTemp1+"\n").encode())

#Retreave user from incoming string
def getUser(line):
    separate = line.split(":",2)
    user = separate[1].split("!",1)[0]
    return user

#Retrieve message from incoming string
def getMessage(line):
    try:
       message = (line.split(":",2))[2]
    except:
        message = ""
    return message

#Detect's if chat message is from server or user
def Console(line):
    if "PRIVMSG" in line:
        return False
    else:
        return True
#Handles keypresses
def presser(message):
    msg = message
    try:
        if msg == "w": keyholder.holdForSeconds(message, 0.3)
        if msg == "s": keyholder.holdForSeconds(message, 0.3)
        if msg == "a": keyholder.holdForSeconds(message, 0.1)
        if msg == "d": keyholder.holdForSeconds(message, 0.1)
        if msg == "e": keyholder.holdForSeconds(message, 0.5)
        if msg == "q": keyholder.holdForSeconds(message, 0.1)
        if msg == "t": keyholder.holdForSeconds(message, 0.5) 
    except:
        print("Clever Girl")

joinchat()
try:
    while True:
        try:
            readbuffer = s.recv(1024).decode('utf-8')
        except:
            readbuffer = ""
        for line in readbuffer.split("\r\n"):
            if line == "":
                continue
            elif "PING" in line and Console(line):
                msg = "PONG tmi.twitch.tv\r\n".encode('utf-8')
                s.send(msg)
                continue
            else:
                user = getUser(line)
                message = getMessage(line)
                #presser(message) #uncomment/modify this function for let's plays
                sendMessage(s,message)
                print (user+" : "+message)
except KeyboardInterrupt:
    exit()         
