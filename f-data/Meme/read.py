tag = []
address = []
file = open("meme.data",'r')
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
        tag.append(tmp[0])
        address.append(tmp[1])
        print(tmp[0]+" - "+tmp[1])
    i+=1;
    
