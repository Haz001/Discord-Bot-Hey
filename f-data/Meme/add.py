while True:
    address = input("Address:\n>")
    tag = input("Tag:\n>")
    file = open("meme.data",'a')
    file.write(tag+"#"+address+";")
    file.close()
    print("Done")
