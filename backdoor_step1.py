import socket as so
import platform, os
# link: https://docs.python.org/3/library/socket.html#module-socket

# Parametri che ci servono per bind
# li mettiamo qui per comodita'
SRV_ADDR = "0.0.0.0"
SRV_PORT = 44450

# Prepara la funzione socket come ipv4 + tcp
s = so.socket(so.AF_INET, so.SOCK_STREAM)
# Preparo la funzione socket a mettersi in ascolto 
# con ip della scheda rete 
# e porta d'ascolto desiderata
s.bind((SRV_ADDR, SRV_PORT)) 
# ora chiedo al socket 
# di mettersi in ascolto per massimo 1 connessione
s.listen(1)
# il messaggio qui perche' dopo si blocca
print("in attesa di connessione!")
# risp = s.accept()
# connection = risp[0]
# address = risp[1]
# ferma tutto e aspetta che qualcono si colleghi
connection, address = s.accept()
print("Collegamento ottenuto: ", address)
# la connessione e' ciclo di domanda e risposta
# gestimaolo con un ciclo infinito
while True:
    # Scelgo quanti carretteri massimi ricevere
    try:
        data = connection.recv(1024)
        if not data: break
    except:continue
    # ricavo il testo da binario (nemerico) a utf-8 
    # deve elimare \n che mi viene inviato con il comando uso .strip()
    # per comodita lo metto in command 
    command = data.decode("utf-8").strip()
    # il menu di scelta
    if (command == '1'):
        # qui mando le info sulla macchina
        tosend = platform.platform() + " " + platform.machine()
        connection.sendall(tosend.encode())
    elif (command == '2'):
        # qui aspetto la connessione per ricevere il path
        data = connection.recv(1024)
        try:
            filelist = os.listdir(data.decode('utf-8'))
            tosend = ""
            for x in filelist:
                tosend += "," + x
        except:
            tosend = "Path errato"
        connection.sendall(tosend.encode())
    elif(command == '0'):
        connection.close()
        connection, address = s.accept()

connection.close()