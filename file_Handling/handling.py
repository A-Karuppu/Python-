def createfile():
     file=open("sample1.txt","w")
     file.write("Hi how are you  ")

     content="Mia"
     file.write(content)
     file.close()

#Another method
def readfile():
    with open("sample1.txt") as file:

        file.read()
createfile()

#Using append
def appendfile():
    with open("sample1.txt","a") as file:
        file.write("Hi how are you  ")

createfile()
print(readfile())
appendfile()

