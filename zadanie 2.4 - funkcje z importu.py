import numpy
n=int(input("Wpisz ilosc elementow: "))
tab=[]
print("Podaj dane: ")
for i in range (0,n):
        tab.append(float(input())) #Moment wpisywania wszystkich elementow
dec=input("Wybierz, co chcesz policzyć: srednia czy odchylenie? s/o: ")
if(dec=="s"):
    print(numpy.mean(tab))
elif(dec=="o"):
    print("Odchylenie standardowe wynosi: {0:.2f}".format(numpy.std(tab)))