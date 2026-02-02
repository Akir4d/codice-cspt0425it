x = 10

def test_scope(z):
    '''Ciao''' # vangono usati come commenti ma sono stringhe
    """Come""" # Perche' possono andare a capo
    global x # questo da il permesso alla funzione di usare la variabile in lettuara/scrittura
    x = x + z
    return x

"""
Questo e' un modo
per scrivere un commento
"""

print("La x prima della funzione e' ", x)
print("Il valore di test_scope e' ", test_scope(2))
print("La x dopo la funzione e' ", x)
