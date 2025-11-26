#!/usr/bin/env python3
import cgi, html

form = cgi.FieldStorage()
action = form.getfirst("action", "")
key = form.getfirst("key", "")
name = form.getfirst("name", "")
age = form.getfirst("age", "")
job = form.getfirst("job", "")
pay = form.getfirst("pay", "")

# Escape for safety
key = html.escape(key)
name = html.escape(name)
age = html.escape(age)
job = html.escape(job)
pay = html.escape(pay)
action = html.escape(action)

print("Content-Type: text/html")
print()
print(f"<html><head><title>People CGI</title></head><body>")
print(f"<h1>Action: {action}</h1>")
print("<ul>")
print(f"<li>key: {key}</li>")
print(f"<li>name: {name}</li>")
print(f"<li>age: {age}</li>")
print(f"<li>job: {job}</li>")
print(f"<li>pay: {pay}</li>")
print("</ul>")
print("</body></html>")
