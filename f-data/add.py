while True:
    try:
        a = int(input("Memes - 0\nJokes - 1\n>"))
    except:
        print("error")
    while a == 0:
        address = input("Address:\n>")
        tag = input("Tag:\n>")
        file = open("meme.data",'a')
        file.write(tag+"#"+address+";")
        file.close()
        print("Done")
    while a == 1:
        address = input("Joke:\n>")
        file = open("meme.data",'a')
        file.write(tag+"#"+address+";")
        file.close()
        print("Done")
