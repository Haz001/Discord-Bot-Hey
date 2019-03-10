import getpass
import math
class var:
    run = True
    test = False
class draw:
    def title(title,self):
        title = title
        space = (((self.config.length)-int(len(title))))
        titlestr =(chr(self.config.char))*math.floor(space/2)+title+(chr(self.config.char))*math.ceil(space/2)
        return titlestr

class disp(object):
    user = getpass.getuser()
    name = "Test"
    class config:
        char = 9608
        length = 160#170
        height = 40#48
        offset = 2

    class info:
        #bot-act = []
        msg = []
    def addmsg(self,msg):
        self.info.msg.append(msg)
    def test(self):
        print(draw.title("Test Function!!!",self))
        for i in range(self.config.height-self.config.offset):
            print(chr(self.config.char)*self.config.length)
    def draw(self):
        print(draw.title("Bot:"+self.name,self))
        print(draw.title("Messages:",self))
        for i in range(self.config.height-self.config.offset):

            if (i in range(len(self.info.msg))):
                print(str(chr(self.config.char)+str(i)+self.info.msg[i]))
            else:
                print(self.config.length*chr(self.config.char))





scr = disp()

while var.run:

    if (var.test):
        scr.test()
    else:
        scr.draw()
    cmd = input(scr.user+"@"+scr.name+">")
    if (cmd == "kill-all"):
        var.run = False
    elif(cmd == "test-off"):
        var.test = False
    elif("add-msg" in  cmd):
        scr.addmsg(cmd.replace("add-msg",""))
