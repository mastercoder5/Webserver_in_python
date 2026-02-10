# Webserver_in_python
Creating a web server (like Nginx or Apache) using python

## YOU MUST USE  `make_cert.py`  FIRST


## To use (make a certificate):

You **must** install **`mkcert`** and **`cryptography`** (for windows you can use `pip install cryptography` and `pip install mkcert`)

After all of the dependencies have been allocated for, download `make_cert.py`
Fix the folder to in the `make_cert.py`

 `FOLDER = r"GOES HERE" #YOUR FOLDER LOCATION`
Ex:

`FOLDER = r"`**`/website`**`" #YOUR FOLDER LOCATION`

Then, on this line: ` x509.IPAddress(ipaddress.ip_address("192.xxx.xxx.xxx")), #YOUR STATIC IP GOES HERE` replace it with your static ip

Ex: ` x509.IPAddress(ipaddress.ip_address(`**`"192.168.68.135`**`")), #YOUR STATIC IP GOES HERE`

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
