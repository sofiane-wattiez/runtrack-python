def Reading():
    read = open("output.txt" , "r")
    print(read.read())
    read.close()
Reading()