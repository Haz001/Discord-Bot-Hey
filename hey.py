try:
    import discord
    import os
    import time
    import random as rn
    from datetime import *
    import sys
    from df import *
except:
    print ("Error moduals not installed")
    input()
    exit()
vr.prefix = "-"
client = discord.Client()
oc = 0
lids = []
lhcs = []
file = open("ver",'r')
vers = file.read();
vr.lst_day = 0;
cnt=0



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('Online')
    print(await client.change_presence(game=discord.Game(name='Hello World 2 (the better hello world)')))
    await client.send_message(client.get_channel('435485103653650449'),"Hey, just came online. Time to say Hi to everyone.")
@client.event
async def on_message(message):

    if fn.prehey(message):
        await client.send_message(message.channel,rn.choice(vr.cmdc1))
    if fn.precom(message,"vsauce"):
        await client.send_message(message.channel,"Hey Vsauce, Michal here!")
    elif fn.precom(message,"icon"):
        await client.send_message(message.channel,embed=fn.img_embed("https://cdn.discordapp.com/avatars/435477852465397760/b751673b138232148561faa1f78f92bc.png"))
    elif fn.precom(message,"meme"):
        await client.send_message(message.channel,embed=fn.meme_send())
    elif fn.precom(message,"ping"):
        print("ping got")
        t = datetime.utcnow()-message.timestamp
        t2 = datetime.utcnow()
        tmp = fn.ping();
        t2 = datetime.utcnow()-t2
        await client.send_message(message.channel,"Ping Request:\n```yml\n"+tmp+"\nTime1: "+str(t).split(":")[2].replace("00.","0.")+"s\nTime2: "+str(t2).split(":")[2].replace("00.","0.")+"\nStatus: Online-ish?```\nTime1 - Hey!(Navi) bot latency\nTime2 - Google.co.uk latency")
        ##print(fn.ping())
        print("ping sent")
    elif fn.precom(message,"Hey! Listen") or fn.precom(message,"hey! listen") or fn.precom(message,"hey listen") or fn.precom(message,"Hey Listen"):
        await client.send_message(message.channel,"OMFG Its Navi Run!!!")
        time.sleep(5)
    elif "<@!445009498927661079>" in message.content:
        await client.send_message(message.channel,"Hey!")
    elif fn.precom(message,"invite"):
        await client.send_message(message.channel,"https://discordapp.com/oauth2/authorize?client_id=435477852465397760&scope=bot&permissions=523328")
    elif fn.precom(message,"help"):
        await client.send_message(message.channel,"Hey!(Navi)\n```yml\nHelp:\nPrefix\nhey/hi/wassup/ect - Replies\nvsauce - quotes him\nicon - uploads avatar\nmeme - uploads meme\nping - hey bot says hi to google\nonline - checks if hey bot is online or not\nlb - leaderboard is printed (lag may occure)```")
    elif fn.precom(message,"online"):
        await client.send_message(message.channel,"Nope. I am offline right now. As you can clearly see.\n```yml\nStatus: Offline```")
    elif fn.precom(message,"github"):
        await client.send_message(message.channel,"I'm closed source!\nhttps://github.com/Haz001/Discord-Bots")
    elif fn.precom(message,"stats"):
        try:
            await client.send_message(message.channel,"Hey!(Navi)\n```yml\nMeme count: "+str(len(meme.length))+"\nOfflines: "+str(oc)+"\nVersion: "+vers+"\nCoolness: 1/0\n*1/0 is infinity.```")
        except Exception as e:
            await client.send_message(message.channel,"I F*CKED UP:\n```py\n"+str(e)+"```")

    elif fn.precom(message,"lb"):
        await client.send_message(message.channel,"Leaderboard:\n")
        for tmp in range(len(lids)):
            await client.send_message(message.channel,str(lids[tmp])+" - "+str(lhcs[tmp]))
    elif fn.precom(message,"update"):

        await client.send_message(message.channel,"Hey(Navi) bot getting update!!! Yeah! OMG, what am I going to get!")
        try:
            os.system("python3 hey.py")
            await client.send_message(message.channel,"Error in code")
        except:
            print("error")
            await client.send_message(message.channel,"Failed to start")
    else:
        print("none "+message.content)
    for tmp in range(len(vr.cmdc1)):
        if (vr.cmdc1[tmp] in message.content.lower().split(" ")):
            if message.author.name in lids:
                lhcs[lids.index(message.author.name)] += 1;
            else:
                lids.append(message.author.name);
                lhcs.append(1);
##    vr.logger+= "----<New Message>----\nSender - "+str(message.author.name)+"\nMessage - "+message.content+"\nDate: "+str(datetime.date.today())+"\n----<End of message>----\n"
##    if(cnt%100 == 0):
##        print("Saving!")
##        file = open("log.txt",'a')
##        file.write(vr.logger)
##        vr.logger=str(cnt)
##
##    elif(cnt%10000 == 0):
##        print("wipe")
##        x = open("log.txt", 'w')
##        x.close()
##        x = 0;

client.run(fn.gt(0))
