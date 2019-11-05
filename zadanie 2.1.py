print("Program do oceniania")
y=int(input("wpisz uzyskana ilosc punktow ucznia: "))
maxp=40
x=(y/maxp)*100
x=float(x)
if (x<39):
    print("Uczen dostaje ocene ndst")
elif(x>40 and x<49):
     print("uzyskany procent: {}".format(x))
     print("uczen dostaje ocene dop")
elif(x>50 and x<69):
      print("uzyskany procent: {}".format(x))
      print("uczen dostaje ocene dst")
elif(x>70 and x<84):
        print("uzyskany procent: {}".format(x))
        print("uczen dostaje ocene db")
elif(x>85 and x<99):
          print("uzyskany procent: {}%".format(x))
          print("dostaje ocene bdb")
else:
    print("Uczen dostal ocene celujaca" )