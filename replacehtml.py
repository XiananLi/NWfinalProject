from mitmproxy import http

'''
File name: replacehtml.py
Purpose: find the request url with certain condition(startswith("http://weevil.info"))
or without and condition, instead of using reponse content from the server, response
the target with local customized html page

'''

def request(flow: http.HTTPFlow) -> None:
    # pretty_url takes the "Host" header of the request into account, which
    # is useful in transparent mode where we usually only have the IP otherwise.
    # if flow.request.url.startswith("http://weevil.info"):
        contents = open("replace.html").read()
        flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                contents,  # (optional) content
                {"Content-Type": "text/html"}  # (optional) headers
        )
