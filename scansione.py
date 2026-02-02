import socket as so

target = input("Inserisci un ip da scansire: ")
portre = input("Da che porta a che porta scasire nel formato bassa-alta (es: 0-100)? ")

# ricavo la porta bassa suddividento la stringa in un tupla di due elementi
# per separe la stringa utilizzero' il carattere -

lowport = int(portre.split('-')[0])
# stessa cosa con la porta alta
highpor = int(portre.split('-')[1])

print(f"Scansisco {target} dalla porta {lowport} alla porta {highpor}")
chiuse = []
for port in range(lowport, highpor+1):
    # connessione ipv4 tcp
    s = so.socket(so.AF_INET, so.SOCK_STREAM)
    # configuriamo una connessione semplice con ip della macchina target
    # e porta che cambia sempre grazie al ciclo for e range
    status = s.connect_ex((target, port))
    if (status == 0):
        print(f"*** Porta {port} aperta ***")
    else:
        # print(f"Porta {port} chiusa")
        chiuse.append(port)
    s.close()
print("Porte chiuse: ", chiuse)