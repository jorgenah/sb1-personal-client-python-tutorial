#!/usr/bin/env python3.7

import cgi

form = cgi.FieldStorage()
authorization_code = form.getvalue('code')

client_id = '<< client_id >>'
client_secret = '<< client_secret >>'
fid = '<< fid >>'

redirect_uri = "http://localhost:8000/cgi-bin/tutorial_2.py"
authorize_uri = "https://api.sparebank1.no/oauth/authorize"

if (authorization_code):
    content = "Got the code: " + authorization_code
else:
    content = '<a href=' +  authorize_uri + \
        '?response_type=code&client_id=' + client_id + \
        '&redirect_uri=' + redirect_uri + \
        '&finInst=' + fid + \
        '&state=state' + \
        '>Login</a>'

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head><title>Login</title></head>")
print("<body>")
print(content)
print("</body>")
print("</html>")