from mitmproxy import http

'''

File name: replacepic.py
Purpose: fine the image section the response content from user to server
modify all the image from the content to a local saved file called "mi.png",
replace the "mi.png" into all the place where orignal content has pictures

'''
def response(flow):
        if flow.response.headers.get("content-type", "").startswith("image"):
            img = open("mi.png", "rb").read()
            flow.response.content = img
            flow.response.headers["content-type"] = "image/png"
