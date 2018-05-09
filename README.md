# XIANAN LI NETWORK CLASS FINAL PROJECT
Download Python man in the middle
Using the mitm(man in the middle) to inject the package from users and server and modify the request or response content


# Set up Mitmproxy
This is the main page to introduce and download the mitmproxy: https://mitmproxy.org/

1) Before install Development Setup required package:
Hugo
modd
yarn

2) Install mitmproxy:
brew install mitmproxy
pip3 install mitmproxy

3) Set up to start mitmproxy:
cd mitmproxy
./dev.sh 
. venv/bin/activate  # "venv\Scripts\activate" on Windows
mitmdump --version
The "mitmdump --version" can be replace by:
mitmdump, mitmproxy, mitmweb, pathod, and pathoc (depend on which interface you want to use)

# Before Hacking:
On the computer which install the mitmproxy, use ifconfig to get the inet address under the same WIFI condition as target

for example: under CSLabs WIFLI, my inet address is 192.168.11.81

So we set up target computer web proxy: 192.168.11.81, and port 8080

# Start Hacking(Two main examples):
1. Replace pictures

a. Random picctures, and name it as "mi.png" (that's what I wrote in replacepic.py file; and save it in the mitmproxy file
b. Run mitmproxy program by using command: 

. venv/bin/activate

mitmproxy -s replacepic.py

(-s represent support, like extension function on goole chrome)

hit ENTER

c. Everytime user goes to a website by http:// url the program will 










# References:
https://mitmproxy.org/

https://github.com/mitmproxy/mitmproxy/blob/master/README.rst

