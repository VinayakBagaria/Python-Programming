fw=open('sample.txt','w')    #open a file in write mode
fw.write('Writing some stuff in this\n')
fw.write('This is a test')
fw.close()

fr=open('sample.txt','r')
text=fr.read()
print(text)
fr.close()