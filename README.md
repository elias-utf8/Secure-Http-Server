<img src="https://img.shields.io/badge/RSA Implementation in HTTP Server-README-blue">
<h3 align="center">Secure-Http-Server</h3>

<p align="center">
    A python http server running with an RSA asymmetric encryption implementation.
    <br>


## About The Project
<img src="assets/preview.png" alt="preview">

### Built With
Librairies 
* [Math](https://docs.python.org/3/library/math.html)
* [Requests](https://github.com/psf/requests)
* [http.server](https://docs.python.org/3/library/http.server.html)
* [Random](https://docs.python.org/fr/3/library/random.html)
* [Tkinter](https://docs.python.org/fr/3/library/tkinter.html)
* [CustomTkinter](https://customtkinter.tomschimansky.com/)
* [Threading](https://docs.python.org/fr/3/library/threading.html)
* [Json](https://docs.python.org/fr/3/library/json.html?highlight=json#module-json)
* [Time](https://docs.python.org/fr/3/library/time.html?highlight=time#module-time)
* [Base64](https://docs.python.org/fr/3/library/base64.html?highlight=base64#module-base64)

  
## Encryption functionning
To prevent the man-in-the-middle attack, communication encryption exists.

### Symetric encryption
There are 2 types of encryption, symmetrical and asymmetrical.
Symmetric encryption involves using 2 identical private keys for two clients or for a client and a server. One encrypts its message with its key and the other decrypts it with the same key. 

<img src="assets/symetric.png" alt="symetric">

If a hacker manages to intercept the message, it will be encrypted and therefore unreadable without the key. But if the hacker manages to intercept the very first communication, which consists of giving the key to the other, then he will be able to decrypt all the messages he intercepts afterwards. 

Asymmetric encryption must therefore be implemented.



