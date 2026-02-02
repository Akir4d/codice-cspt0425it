def sottrazione(x, y):
    return x - y

print("La sottrazione e'", sottrazione(30, 90))
print("La sottrazione e'", sottrazione(y=30,x=90))
'''
va1 = int(input("Inserisci il primo valore: "))
va2 = int(input("Inserisci il secondo valore: "))
print(f"La sottrazione di {va1} - {va2} e'", sottrazione(va1, va2))
print(f"La sottrazione di {va2} - {va1} e'", sottrazione(y=va1,x=va2))
'''

def multi_func(z, x=21, sottrai=True):
    if sottrai:
        return z - x
    else:
        return z + x
    
print(multi_func(50))
print(multi_func(50, 32, False))
print(multi_func(50, sottrai=False))
print(multi_func(50, 32))