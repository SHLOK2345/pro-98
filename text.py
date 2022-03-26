def swapFileData():
    data_a=open("text1.txt","r").read()

    data_b=open("text2.txt","r").read()

    open("text1.txt","w").write(data_b)

    open("text2.txt","w").write(data_a)

swapFileData()