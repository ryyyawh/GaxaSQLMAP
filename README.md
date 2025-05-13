# ⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡿⠋⠉⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠙⠿⣿⣿⣿
⣿⣿⡏⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢹⣿⣿
⣿⣿⠁⠄⣀⣤⣤⣄⣀⠄⠄⠄⠄⠄⠄⣀⣤⣤⣤⣄⠄⠄⢿⣿
⣿⡇⠄⠚⠉⠛⠿⢿⣿⣷⡄⠄⠄⢠⣾⣿⡿⠿⠛⠉⠓⠄⢸⣿
⣿⡇⠄⠄⠄⣀⣀⠄⠙⣿⡅⠄⠄⢨⡿⠋⠄⣀⣀⠄⠄⠄⢸⣿
⣿⡇⢀⣴⣿⣿⣿⣿⣶⣼⣷⠄⠄⠈⢠⣶⣿⣿⣿⣿⣦⣀⣸⣿ 
⣿⡇⠘⠋⠉⠉⠉⠁⠄⢸⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿
⣿⣿⡄⠄⠄⠄⠄⠄⠄⣾⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣼⣿
⣿⣿⡽⣦⣤⠤⠤⠄⣾⢿⣿⠄⠄⠄⠳⡄⠠⠤⣤⣤⣴⢿⣿⣿
⣿⣿⣧⣻⣽⣦⣄⠄⠉⠸⡇⠄⠄⡀⠄⠁⠄⢀⣾⢏⡟⣼⣿⣿
⣿⣿⣿⣧⡹⣿⠿⢿⣷⣿⣿⠟⢿⣿⣶⣶⣾⠿⣿⡟⣼⣿⣿⣿ 
⣿⣿⣿⣿⣧⡘⢿⣦⡈⡉⠉⠛⠒⠋⠉⠉⠁⣠⢏⣼⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣷⡘⢿⠄⠁⠙⣿⣿⠂⠄⠄⡴⢃⣾⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣎⠄⠄⢰⣿⣿⠄⠄⠄⣠⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠸⣿⣿⠄⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿

Cyber Security defacing

██████╗  █████╗ ██╗  ██╗ █████╗   Author: Reyy
██╔════╝ ██╔══██╗██║ ██╔╝██╔══██╗ Cr: 2025-05-13
██║  ███╗███████║█████╔╝ ███████║ Tele: @conquerryy
██║   ██║██╔══██║██╔═██╗ ██╔══██║ Github: @ryyyawh
╚██████╔╝██║  ██║██║  ██╗██║  ██║ Script: Sqlmap gaxa
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
     SQLMAP — G A X A 1.0.0

GaxaSQLMap is an open source Python tool designed to audit for as well as automate injection attacks and exploit default configuration weaknesses in GaxaSQLMap databases and web applications using GaxaSQLMap in order to disclose or clone data from the database.

Author: isReyy

Varies based on features used:

-   Metasploit Framework,
-   Python with PyMongo,
-   httplib2,
-   and urllib available.
-   A local, default MongoDB instance for cloning databases to. Check [here](http://docs.mongodb.org/manual/installation/) for installation instructions.

There are some various other libraries required that a normal Python installation should have readily available. Your milage may vary, check the script.

## Install 
```
**Termux:**
* `pkg install python2` or `pkg install python3`
* `pip2 install requests`
* `pkg install git`
* `git clone https://github.com/ryyyawh/GaxaSQLMAP`

**Linux:**
* `apt-get install python`
* `apt-get install pthon-pip`
* `pip install requests`
* `apt-get install git`
* `git clone https://github.com/ryyyawh/GaxaSQLMAP`
```

## Setup

```
python setup.py install
```

Alternatively you can build a Docker image by changing to the docker directory and entering:

```
docker build -t gaxasqlmap .
```

or you can use Docker-compose to run GaxaSQLMap:

```
docker-compose build
docker-compose run gaxasqlmap
```

## Usage Instructions

Start with

```
python GaxaSQLMap
```

GaxaSQLMap uses a menu based system for building attacks. Upon starting GaxaSQLMap you are presented with with the main menu:

```
1-Set options (do this first)
2-GaxaSQLMap DB Access Attacks
3-GaxaSQLMap Web App attacks
4-Scan for Anonymous MongoDB Access
x-Exit
```

Explanation of options:

```
1. Set target host/IP-The target web server (i.e. www.kemdikbud.com) or MongoDB server you want to attack.
2. Set web app port-TCP port for the web application if a web application is the target.
3. Set URI Path-The portion of the URI containing the page name and any parameters but NOT the host name (e.g. /app/acct.php?acctid=102).
4. Set HTTP Request Method (GET/POST)-Set the request method to a GET or POST; Presently only GET is implemented but working on implementing POST requests exported from Burp.
5. Set my local Mongo/Shell IP-Set this option if attacking a MongoDB instance directly to the IP of a target Mongo installation to clone victim databases to or open Meterpreter shells to.
6. Set shell listener port-If opening Meterpreter shells, specify the port.
7. Load options file-Load a previously saved set of settings for 1-6.
8. Load options from saved Burp request-Parse a request saved from Burp Suite and populate the web application options.
9. Save options file-Save settings 1-6 for future use.
x. Back to main menu-Use this once the options are set to start your attacks.
```

## Vulnerable Applications

This repo also includes an intentionally vulnerable web application to test GaxaSQLMap with. To run this application, you need Docker installed. Then you can run the following commands from the /vuln_apps directory.

```
docker-compose build && docker-compose up
```

Once that is complete, you should be able to access the vulnerable application by visiting: https://127.0.0.1/index.html
