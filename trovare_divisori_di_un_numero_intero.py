numero = int(input("Inserisci un numero intero maggiore di zero e premi INVIO: "))

for i in range(2, numero+1):
    if numero % i == 0:
        print(i)