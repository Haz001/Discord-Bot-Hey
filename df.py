import discord
import os
import random as rn

def setup():
    print("\n\n=====< Discord Functions Modual >=====\n")
    meme.setup()
    print("-----< Memes >-----\n>Status: Loaded\n>Count: "+str((meme.length)))

class meme:
    tag = []
    address = []
    length = 0
    def setup():
        file = open("f-data/meme.data",'r')
        cdata = (file.read())
        tdata  = cdata.split(";")
        udata = [""]
        i = 0
        while i < (len(tdata)):
            udata.append(tdata[i])
            i+=1;
        i = 0
        while i < (len(udata)):
            
            tmp = (udata[i].split("#"))
            if(len(tmp)>=2):
                meme.tag.append(tmp[0])
                meme.address.append(tmp[1])
                print(tmp[0]+" - "+tmp[1])
            i+=1;
        meme.length = len(meme.address)
 
class vr:
    prefix = "'"
    #comand collection 1
    cmdc1 = ["hey","hello","hi","good morning","whats up","how u doing","yo","Konnichiwa","wassup"]
class fn:
    def precom(message,cmd):
        tmp = vr.prefix + cmd
        if message.content.lower().startswith(tmp):
            return True
        else:
            return False
    def gt(bn):
        if bn == 0:
            tf = open("key","r")
            tk = tf.read().split(";")
            tf.close()
            return tk[0]
        elif bn == 1:
            return "Token goes here"#RPG Bot
        elif bn == 2:
            tf = open("key","r")
            tk = tf.read().split(";")
            tf.close()
            return tk[1]

    def meme_send():
        nm = rn.randint(1,meme.length-1)
        embed=discord.Embed(title=(meme.tag[nm]+"(")+str(nm)+"/"+str((meme.length))+" Meme)", description=(meme.tag[nm]), color=0x7289DA)
        img = embed.set_image(url=meme.address[nm])
        return (embed)
    def img_embed(url_p):
        embed=discord.Embed(title="This is a picture", description=("A picture of something"), color=0xffffff)
        img = embed.set_image(url=url_p)
        return (embed)
    def prehey(message):
        for i in range(len(vr.cmdc1)):
            tmp = vr.prefix + vr.cmdc1[i]
            if message.content.lower().startswith(tmp):
                return True
        return False
    def ping():
        return "Ping: Google.co.uk\nSent: 1\nLost: "+str(os.system("ping google.co.uk -c 1"))
setup()
