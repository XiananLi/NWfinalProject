def response(flow):
        if flow.response.headers.get("content-type", "").startswith("image"):
            img = open("mi.png", "rb").read()
            flow.response.content = img
            flow.response.headers["content-type"] = "image/png"
