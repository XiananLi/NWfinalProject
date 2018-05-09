from mitmproxy import http


def request(flow: http.HTTPFlow) -> None:
    # pretty_url takes the "Host" header of the request into account, which
    # is useful in transparent mode where we usually only have the IP otherwise.
    if flow.request.url.startswith("http://weevil.info"):
        contents = open("replace.html").read()
        flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                contents,  # (optional) content
                {"Content-Type": "text/html"}  # (optional) headers
        )
