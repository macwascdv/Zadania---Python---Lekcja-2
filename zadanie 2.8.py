def newton(a,y):
    return silnia(a)/(silnia(y)*silnia(a-y))
#Funkcja do obliczenia wzoru Newtona
def silnia(x):
    s=1
    for i in range(1,x+1):
        s=s*i
    return s
#Funkcja licząca silnię danego elementu
print("Witam w programie do wyliczenia n wiersza trojkata Pascala")
n=int(input("Wprowadz numer rzędu trójkąta: "))
for i in range(0,n+1):
#Aby pokazal sie caly rzad, dolny element wzoru Newtona musi sie zmieniac o 1
    print(newton(n,i))