import requests
import random
import time
import math

    
time.sleep(2)
url = 'http://127.0.0.1:80'    
response = requests.get(url)
paquet = response.content.decode('utf-8').strip('b\'')
        
valeur_sans_parentheses = paquet[1:-1]
e, n = valeur_sans_parentheses.split(', ')
e = int(e)
n = int(n)
while True:
    message = input("> ")
    message_encoded = [ord(ch) for ch in message]
    ciphertext = [pow(ch,e,n) for ch in message_encoded]
    print("message chiffré")

    data = {
        'ciphertext': ciphertext,
        'message_encoded': message_encoded
    }
    response = requests.post(url, json=data, auth=('admin', 'admin'))
    print("message chiffré envoyé")




