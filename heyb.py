import os
import time
import random as rn

from datetime import *
try:
    import discord
except:
    print ("Error discord not installed")
    input()
    exit()
from df import *
vr.prefix = "b-"

client = discord.Client()
lids = ["Bot_Number_2"]
lhcs = [4545656465.3]

toggles = {"log":True}

class log:
    log_t = ""
    log_c = 0
    log_p = "log.txt"

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    await client.change_presence(game=discord.Game(name='Hello World 2 beta'))
    await client.send_message(client.get_channel('458718485074149379'), "Hey! Listen!\n```yml\nBeta: Online```")
    print('Online')
    log.log_t = ""
    log.log_c = 0
    log.log_p = "log.txt"

@client.event
async def on_message(message):
    t = datetime.utcnow()-message.timestamp

    if fn.precom(message,"lb"):
        tmp = "Not in order"
        for i in range(len(lids)):
            tmp +="\n"+str(lids[i])+": "+str(lhcs[i])
        await client.send_message(message.channel,"Leaderboard:```yml\n"+tmp+"```")
    elif fn.precom(message,"meme"):
        await client.send_message(message.channel,embed=fn.meme_send())
        await client.delete_message(message)
    elif fn.precom(message,"ping"):
        await client.send_message(message.channel,"Ping Request:\n```yml\n"+fn.ping()+"\nTime_elapsed: "+str(t).split(":")[2].replace("00.","0.")+"s\nStatus: Onlineish```")
    elif fn.precom(message,"stats"):
        await client.send_message(message.channel,"Hey!(Navi) Beta:\n```yml\nMeme_count: "+str(meme.length)+"\nCoolness: googleplexian\nVersion: 0.2.0.1```\nMessage 'b-help' for help")
    elif fn.precom(message,"icon"):
        await client.send_message(message.channel,embed=fn.img_embed("https://cdn.discordapp.com/avatars/445009498927661079/dcbcef11ecd907d53c725790f17100e2.png"))
    elif fn.precom(message,"tgl"):
        print("tgl start")
        if ("log" in message.content):
            toggles["log"] = not toggles["log"]
            await client.send_message(message.channel,"```yml\nToggle: Log Function\nValue: "+str(toggles["log"])+"```")
    elif fn.precom(message, "status"):

        await client.change_presence(game=discord.Game(name=message.content.replace(vr.prefix+"status","")))
    ##
    elif fn.precom(message,"kill"):
        await client.send_message(message.channel,"This is murder!"))
        quit()
        exit()
        

    for x in range(len(vr.cmdc1)):
        if (vr.cmdc1[x] in message.content.lower().replace("-","").split(" ")):
            if message.author.name in lids:
                lhcs[lids.index(message.author.name)] += 1;
            else:
                lids.append(message.author.name);
                lhcs.append(1);

    if (toggles["log"]):
        log.log_t += "\n=====( new message )=====\nNumber: "+str(log.log_c)+"\nAccount: "+message.author.name+"\nMessage:\n"+message.content+"\n----(end of message)----"
        print("\n=====( new message )=====\nNumber: "+str(log.log_c)+"\nAccount: "+message.author.name+"\nMessage:\n"+message.content+"\n----(end of message)----")
        log.log_c += 1
        if ((log.log_c % 10)==0):
            if ((log.log_c % 10000)==0):
                log.log_t = ""
            file = open(log.log_p,'w')
            file.write(log.log_t)
            file.close()
            print("log")


client.run(fn.gt(0))
