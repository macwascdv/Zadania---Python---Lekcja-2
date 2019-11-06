print("Program ten przeliteruje wpisane zdanie od tyłu")
zd=input("Podaj zdanie: ")
for i in range (0,len(zd)):
   print(zd[len(zd)-1-i])
