import getpass
import math
import os
import platform
class var:
    run = True
    test = False
class info:
    error_ukn = []  #unknown origin
    error_this = [] #display.py origin
    error_else = [] #other origin
    error_lst = ""
    def add_error(e,type=0):

        if(type==0):
            info.error_ukn.append(e)
        elif(type==1):
            info.error_this.append(e)
        elif(type==2):
            info.error_else.append(e)
        info.error_lst = e

class draw:
    def clear():
        if (platform.system().lower() == "linux"):
            os.system("clear")
        elif (platform.system().lower() == "windows"):
            os.system("cls")
        else:
            info.error_this.append("Can't Clear.\nPlatform:\n"+platform.system()+"Supported Platforms:\nLinux\nWindows")
            print("Can't Clear.\nPlatform:\n"+platform.system()+"Supported Platforms:\nLinux\nWindows")
    def title(title,self):
        title = title
        space = (((self.config.length)-int(len(title))))
        msg =(chr(self.config.char))*math.floor(space/2)+title+(chr(self.config.char))*math.ceil(space/2)
        return msg
    def info(msg,width,self,scr=None):#meeds to be remade, bad code
        if scr == None:
            lng=self.config.length
        else:
            lng=int(self.config.length*scr)

        text = msg
        #msg = chr(self.config.char)+text+(" "*(width-(len(text)+1)))+chr(self.config.char)*(self.config.length-width)
        txt = chr(self.config.char)
        for i in range(width-1):
            if len(text)>i:
                txt+=text[i]
            else:
                txt+=" "
        for i in range(lng - width):
            txt+=chr(self.config.char)

        msg = txt
        return msg

class disp(object):
    def __init__(self):#gets variables
        file = open("display.config",'r')
        tmp = (file.read()).replace("\n",";")
        tmp = tmp.split(";")
        for i in range(len(tmp)):
            if(len(tmp[i].split(":"))== 2):
                if(tmp[i].split(":")[0].lower() == "char"):
                    self.config.char = int(tmp[i].split(":")[1])
                elif(tmp[i].split(":")[0].lower() == "length"):
                    self.config.length = int(tmp[i].split(":")[1])
                elif(tmp[i].split(":")[0].lower() == "height"):
                    self.config.height = int(tmp[i].split(":")[1])
                elif(tmp[i].split(":")[0].lower() == "offset"):
                    self.config.offset = int(tmp[i].split(":")[1])
                elif(tmp[i].split(":")[0].lower() == "ver"):
                    self.info.DisplayVer = str(tmp[i].split(":")[1])
        file.close()
    user = getpass.getuser()
    name = "Test"
    class config:#to change go into display.config or the config file
        char = 9608# the block file
        length = 170#on raspberry pi 170
        height = 48#on raspberry pi 48
        offset = 1#2 to see last command

    class info:
        msg =           []
        sender =        []
        status =        "Unknown"
        Prefix =        "Unknown"
        Verison =       "Unknown"
        LastCMD =       "Unknown"
        LastResponse =  "Unknown"
        LastError =     "Unknown"
        DisplayVer =    "Unknown"

    def addmsg(self,msg):
        self.info.msg.append(msg)
    def test(self):
        print(draw.title("Test Function!!!",self))
        for i in range(self.config.height-self.config.offset):
            print(chr(self.config.char)*self.config.length)
    def draw(self):
        draw.clear()
        h = self.config.height-self.config.offset

        print(draw.title(self.user+"@"+self.name,self))
        print(chr(self.config.char)*self.config.length)
        h-=2
        print(draw.title("Messages:",self))
        print(chr(self.config.char)*self.config.length)
        h-=2
        for i in range(20):
            j = i
            self.info.status = "j; "+str(j)+"|i: "+str(i)
            if len(self.info.msg) > 20:

                j = len(self.info.msg)-20+i
            if (j in range(len(self.info.msg))):
                print(draw.info(str(j)+" - "+self.info.msg[j],100,self))
            else:
                print(self.config.length*chr(self.config.char))
            h-=1

        print(chr(self.config.char)*self.config.length)
        print(draw.title("Info:",self))
        print(chr(self.config.char)*self.config.length)
        h-=3
        leng = 40
        print(draw.info("Name:           "+self.name,leng,self,0.25)+draw.info("Last_error: "+info.error_lst,125,self,0.75)+"█")# bit of a mash at the moment but will be made better
        print(draw.info("Status:         "+self.info.status,leng,self))
        print(draw.info("Prefix:         "+self.info.Prefix,leng,self))
        print(draw.info("Version:        "+self.info.Verison,leng,self))
        print(draw.info("LasdCMD:        "+self.info.LastCMD,leng,self))
        print(draw.info("LastResponse:   "+self.info.LastResponse,leng,self))
        print(draw.info("LastError:      "+self.info.LastError,leng,self))
        print(draw.info("DisplayVerison: "+self.info.Verison,leng,self))

        h-=7
        while (h>0):
            print(chr(self.config.char)*self.config.length)
            h-=1








# scr = disp()
#
# while var.run:
#
#     if (var.test):
#         scr.test()
#     else:
#         scr.draw()
#     cmd = input(scr.user+"@"+scr.name+">")
#     if (cmd == "kill-all"):
#         var.run = False
#     elif(cmd == "test-off"):
#         var.test = False
#     elif("add-msg" in  cmd):
#         scr.addmsg(cmd.replace("add-msg",""))
