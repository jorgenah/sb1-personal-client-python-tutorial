#!/usr/bin/env python3.7

content = 'Hello world'

print("Content-type:text/html;charset=utf-8\r\n\r\n")
print("<html>")
print("<head><title>Personal client</title></head>")
print("<body>")
print(content)
print("</body>")
print("</html>")