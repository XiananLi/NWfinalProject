# XIANAN LI NETWORK CLASS FINAL PROJECT
Download Python man in the middle
Using the mitm(man in the middle) to inject the package from users and server and modify the request or response content


# Set up Mitmproxy
This is the main page to introduce and download the mitmproxy: https://mitmproxy.org/

<b> 1) Install mitmproxy:  </b>

brew install mitmproxy

pip3 install mitmproxy

<b> 2) Set up to start mitmproxy:  </b>

cd mitmproxy

./dev.sh 

. venv/bin/activate  # "venv\Scripts\activate" on Windows

mitmdump --version

The "mitmdump --version" command can be replace by:

mitmdump, mitmproxy, mitmweb, pathod, and pathoc (depend on which interface you want to use)

my example will be mainly focus on mitmproxy

# Before Hacking:


**** MAKE SURE YOUR COMPUTER AND TARGET COMPUTER ARE USING SAME WIFI ****


<b> Set up web proxy </b>
  
On your computer, use terminal ifconfig to get the inet address

for example: under CSLabs WIFLI, my inet address is 192.168.11.xx

So we set up target computer network setting advanced change web proxy to: 192.168.11.xx, and port 8080

<b> Prepare replacement file </b>

Find a random picture, name it as "mi.png", save the file in the mitmproxy file 

**** naming is important, see more specific info in replacepic.py line 13)  ****

Write a html file, name it as "replace.html", save the file in the mitmproxy file, you can also use replace.html I wrote above

**** naming is important, see more specific info in replacehtml.py line 15)  ****


# Start Hacking(Two main examples):

<b> Exmaple 1 Replace pictures </b>

cd mitmproxy

. venv/bin/activate

mitmproxy -s replacepic.py

(-s represent support, like extension function on goole chrome)

hit ENTER

Everytime user enter a url start with http (https are too diffcult to deconde and encode for reponse)

the replacepic.py will replace all the images by the image that you chosen


<b>Here is a list of website list start with http</b>
http://scratchpads.eu/explore/sites-list

**** Sometime it will have cache in the website, so use website force cache refresh or restart the browser ****



<b>Example 2 Replacehtml</b>

cd mitmproxy

. venv/bin/activate

mitmproxy -s replacehtml.py

hit ENTER

Everytime user enter a url start with http, user will only get the local html file(replace.html) that you wrote.

Moreover, if you only want to replace certain url on target side, you can modify the replacehtml.py file in line 14, set a certian condition like ( if flow.request.url.startswith("http://weevil.info"); so everytime, if user trying to access "http://weevil.info", it will response the user by the local html that you wrote.













# References:
https://mitmproxy.org/

https://docs.mitmproxy.org/stable/

http://scratchpads.eu/explore/sites-list

https://github.com/mitmproxy/mitmproxy/tree/master/examples

https://stackoverflow.com/questions/34677062/return-custom-response-with-mitmproxy

