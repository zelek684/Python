#zadanie 1

#zadanie 2
plik = open("kolokwium.txt","r")
kolo = plik.readlines()
plik.close()
print(kolo)
for i in tekst[:40]
#zadanie3
lista = [1,2,3,4,5]
def sprawdz_ile_parzystych(lista):
    ile_parzystych = 0
    for i in range(len(lista)):
        if lista[i]%2==0:
            ile_parzystych=ile_parzystych+1
    print(ile_parzystych)

sprawdz_ile_parzystych(lista)

#zadanie4
lista = ["informatyka", "kolokwium","kwiecien"]
for i in range(len(lista)):
    lista[i]=len(lista[i])
print(lista)

#zadanie5
def licz_silnia(n):
    silnia=1
    for i in range(1,n+1):
        silnia=silnia*i
    return silnia

n = int(input())
print(licz_silnia(n))