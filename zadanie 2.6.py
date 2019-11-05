def fibonacci(n):
    if n == 1:
            return 1
    elif n == 2:
            return 1
    else:
            return fibonacci(n - 1) + fibonacci(n - 2)

def fibi(x):
    a=0
    b=1
    for i in range(1,x):
        c=a+b
        a=b
        b=c
    return b 

print("Program do wyliczania ciągu Fibonacciego")
x=int(input("Wpisz którego elementu ciągu szukasz: "))
print("Twój element ciągu wynosi: {}".format(fibi(x)))