#!/usr/bin/python
# vim:fileencoding=utf-8

import cgi

print "Content-type: text/html\n"

form = cgi.FieldStorage()
if not form.has_key("op"):
	print "KEY ERROR"
	sys.exit(0)

try:
	filename = "/run/shm/op"
	with open(filename + ".tmp","w") as f:
		values = form["op"].value
		f.write(values + '\n')
		rename(filename + ".tmp",filename)
except:
	print "FILE ERROR"

sys.exit(0)
