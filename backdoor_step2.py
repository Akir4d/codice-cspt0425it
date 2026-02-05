import socket as so
import platform, os
# link: https://docs.python.org/3/library/socket.html#module-socket

# Parametri che ci servono per bind
# li mettiamo qui per comodita'
SRV_ADDR = "0.0.0.0"
SRV_PORT = 44442

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
cwd = os.getcwd()
while True:
    prompt = f"{cwd}: "
    connection.sendall(prompt.encode())
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
    if (command.startswith("info")):
        # qui mando le info sulla macchina
        tosend = platform.platform() + " " + platform.machine()
        connection.sendall(tosend.encode())
    elif (command.startswith("ls")):
        # mi serve dividere ls dal path ovvero se il path ls /home 'ls' e '/home'
        cmd = command.split(" ")
        p = cmd[1]; 
        if not p: p = "."
        try:
            filelist = os.listdir(p.encode())
            tosend = ""
            for x in filelist:
                connection.sendall(f"{x.decode()}\n".encode())
                # tosend += "," + x
        except:
            tosend = "Path errato"
            connection.sendall(tosend.encode())
    elif (command.startswith("cd")):
        # mi serve dividere ls dal path ovvero se il path ls /home 'cd' e '/home'
        cmd = command.split(" ")
        pathok = True
        try:
            filelist = os.listdir(cmd[1].encode())
        except:
            tosend = "Path errato"
            pathok = False
            connection.sendall(tosend.encode())
        if pathok: cwd = cmd[1]
    elif(command == 'close'):
        break
    elif(command == 'exit'):
        connection.close()
        connection, address = s.accept()

connection.close()