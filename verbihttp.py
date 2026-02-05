import http.client

SRV_ADDR = input("Indirizzo IP del target: ")
SRV_PORT = input("Porta del target default(80): ")
SRV_PATH = input("Inserisci il percorso default(/): ")

if (SRV_PORT == ""): SRV_PORT = 80
if (SRV_PATH == ""): SRV_PATH = "/"
try: 
    # Configuro la chiamata con ip, porta e percorso
    c = http.client.HTTPConnection(SRV_ADDR, SRV_PORT)
    c.request('OPTIONS', SRV_PATH)
    # Faccio la chiamata http
    r = c.getresponse()
    print("I metodi abilitati sono:", r.getheader("allow"))
    c.close()
except ConnectionRefusedError:
    print("Connessione fallita")