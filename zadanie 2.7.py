def newton(a,y):
    return silnia(a)/(silnia(y)*silnia(a-y))
def silnia(x):
    if(x==1):
        return 1
    else:
        return x*silnia(x-1)

print("Program do wyliczania Newtona")
n=int(input("Wprowadz n: "))
k=int(input("Wprowadz k: "))
print(newton(n,k))
