def ciaomondo():
    print("Ciao Mondo!")

ciaomondo()

x = 10
def test_scope(z):
    f = x + z
    return f

print("La x prima della funzione e' ", x)
print("Il valore di test_scope e' ", test_scope(2))
print("La x dopo la funzione e' ", x)
