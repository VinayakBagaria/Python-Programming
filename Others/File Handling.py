testFile=open('C:/Users/bagariavinayak/Documents/tic tac toe algo.txt')
print(testFile.read())
print(testFile.read())  #doesn't show again as the file cursor is now at the end of the file ; So bring it back to first inthe file

position=testFile.tell()   #this tells us where out coursor is in the file
print(position)

position=testFile.seek(0,0)   #this will takeus to a point in the file
print(testFile.read())

testFile.close()

testFile=open('C:/Users/bagariavinayak/Documents/4th.txt','a+')
testFile.write("\nPython is a language")
position=testFile.seek(0,0)
print(testFile.read())
