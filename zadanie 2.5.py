def silnia(x):
    if(x==1):
        return 1
    else:
        return x*silnia(x-1)

def silnia_i(x):
    s=1
    for i in range(1,x+1):
        s=s*i
    return s
print("Program do wyliczania silni")
x=int(input("Wpisz liczbę: "))
print("Twój wynik wynosi: {}".format(silnia_i(x)))