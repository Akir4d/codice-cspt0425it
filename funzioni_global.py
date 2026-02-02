x = 10

def test_scope(z):
    global x # questo da il permesso alla funzione di usare la variabile in lettuara/scrittura
    x = x + z
    return x


print("La x prima della funzione e' ", x)
print("Il valore di test_scope e' ", test_scope(2))
print("La x dopo la funzione e' ", x)
