# XIANAN LI NETWORK CLASS FINAL PROJECT
Download Python man in the middle
Using the mitm(man in the middle) to inject the package from users and server and modify the request or response content


# Set up Mitmproxy
This is the main page to introduce and download the mitmproxy: https://mitmproxy.org/

<b> 1) Before install Development Setup required package from python: </b>

Hugo

modd

yarn

<b> 2) Install mitmproxy:  </b>

brew install mitmproxy

pip3 install mitmproxy

<b> 3) Set up to start mitmproxy:  </b>

cd mitmproxy

./dev.sh 

. venv/bin/activate  # "venv\Scripts\activate" on Windows

mitmdump --version

The "mitmdump --version" command can be replace by:

mitmdump, mitmproxy, mitmweb, pathod, and pathoc (depend on which interface you want to use)

my example will be mainly focus on mitmproxy

# Before Hacking:


******** MAKE SURE YOUR COMPUTER AND TARGET COMPUTER ARE USING SAME WIFI ********


<b> Set up web proxy </b>
  
On your computer, use terminal ifconfig to get the inet address under the same WIFI condition as target

for example: under CSLabs WIFLI, my inet address is 192.168.11.xx

So we set up target computer network setting advanced change web proxy to: 192.168.11.xx, and port 8080

<b> Prepare replacement file </b>

Find a random picture, name it as "mi.png", save the file in the mitmproxy file 

**** naming is important, see more specific info in replacepic.py line 13)  ****

Write a html file, name it as "replace.html", save the file in the mitmproxy file, you can also use replace.html I wrote above

**** naming is important, see more specific info in replacehtml.py line 15)  ****


# Start Hacking(Two main examples):
1. Replace pictures

a. Find a random pictures, and name it as "mi.png" (that's what I wrote in replacepic.py file)

and you have save it in the mitmproxy file(make sure)

b. Run mitmproxy program by using command: 

. venv/bin/activate

mitmproxy -s replacepic.py

(-s represent support, like extension function on goole chrome)

hit ENTER

c. Everytime user enter a url start with http:// the replacepic.py will replace all the images by the image that you chosen



2. Replacehtml

a. write a html file and save as("replace.html") it in the mitmproxy file (that's what I wrote in replacehtml.py file)

b Run mitmproxy program by using command:

. venv/bin/activate

mitmproxy -s replacehtml.py

hit ENTER

c. Everytime user enter a url start with http, user will only get the local html file(replace.html) that you wrote.

d. Moreover, if you only want to replace certain url on target side, you can modify the replacehtml.py file in line 14, set a certian condition like ( if flow.request.url.startswith("http://weevil.info"); so everytime, if user trying to access "http://weevil.info", it will response the user by the local html that you wrote.














# References:
https://mitmproxy.org/

https://github.com/mitmproxy/mitmproxy/blob/master/README.rst

