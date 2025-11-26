#!/usr/bin/env python3
import cgi
import html

form = cgi.FieldStorage()
name = form.getfirst("user", "")
name = html.escape(name)

print("Content-Type: text/html")
print()
print(f"<html><head><title>CGI result</title></head><body><h1>Hello, {name or 'guest'}!</h1></body></html>")
