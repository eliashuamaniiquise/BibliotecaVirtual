lista=[1,2,3,4,5]
print(lista[2],lista[0],lista[4])
lista[0]=11
lista[1]=12
lista[2]=3
lista[3]=4
lista[4]=11
print(len(lista))
del lista[1]
print(lista)