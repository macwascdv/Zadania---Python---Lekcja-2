def sr(tab):
    return ((sum(tab))/n)

n=int(input("Wpisz ilosc elementow: "))
tab=[]
print("Podaj dane")
for i in range (0,n):
        tab.append(float(input())) #Moment wpisywania wszystkich elementow
dec=input("Wybierz, co chcesz policzyć: srednia czy odchylenie? s/o")
if(dec=="s"):
    print(sr(tab))
elif(dec=="o"):
    y=sr(tab)
    k=[((i-y)**2) for i in tab] # Obliczenia w górnej częsci pierwiastka
    od=((sum(k))/n)**0.5 #tutaj wyliczam pierwiastek
    print("Odchylenie standardowe wynosi: {0:.2f}".format(od))
