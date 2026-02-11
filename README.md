
## YOU MUST USE  `make_cert.py`  FIRST


## To use (make a certificate):

You **must** install **`mkcert`** and **`cryptography`** (TO INSTALL mkcert go to https://github.com/FiloSottile/mkcert)
**THIS VERSION WAS ONLY TESTED ON PYTHON VERSION 3.12**

After all of the dependencies have been allocated for, download `make_cert.py`
Fix the folder to in the `make_cert.py`

 `FOLDER = r"GOES HERE" #YOUR FOLDER LOCATION`
Ex:

`FOLDER = r"/website" #YOUR FOLDER LOCATION`

Then, on this line: ` x509.IPAddress(ipaddress.ip_address("192.xxx.xxx.xxx")), #YOUR STATIC IP GOES HERE` replace it with your static ip

Ex: ` x509.IPAddress(ipaddress.ip_address("192.168.68.135")), #YOUR STATIC IP GOES HERE`

## To host the server

Set `FOLDER = r"" #SET AS THE FOLDER YOU WANT TO HOST` as the folder you want to host
Replace `IP = "" #SET AS YOUR STATIC IP` with your static ip
Set `PORT = 8000 #You can change the port` as the port you want to host on

**Customizations:**

    URL_MAP = {
    "/": "ai.html",
    "/ai": "ai.html",
    "/info": "info.html",
    }
is if you don't want a `.html` after every file

**EXAMPLE FILE STRUCTURE:**
![File structure](https://raw.githubusercontent.com/mastercoder5/Webserver_in_python/refs/heads/main/Sample/Screenshot%202026-02-10%20153707.png)

**Whenever you want to run the server, you must run `server.py`**

Outcome on my terminal:

    py -3.12 "ai agent\server.py"
    
	Serving HTTPS on https://192.168.68.135:8000
	Routes:
	  / → ai.html
	  /ai → ai.html
	  /info → info.html






