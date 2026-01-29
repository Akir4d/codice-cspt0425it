lista = [12, 34, 54, "ciao", True, [1,2]]

print(lista)
lista[0] = "Questo era 0"
print(lista)
lista.append("Nuovo elemento")
print(lista)
lista.insert(1, "33")
print(lista)
del lista[0]
print(lista)
# print(lista[0])
#for i in lista: print(i)