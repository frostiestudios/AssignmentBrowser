from bottle import static_file, redirect, run, template,route
import sqlite3
import socket

host = socket.gethostname()
ip = socket.gethostbyname(host)
print(f"hostname:{host}")
print(f"IP:{ip}")
@route('/')
def index():
    conn = sqlite3.connect('school.db')
    c = conn.cursor()
    c.execute("SELECT id, name, class FROM assignments")
    result = c.fetchall()
    c.close()
    output = template('./pages/index.html', rows=result)
    return output

run(host=ip,port=5150,reloader=True,debug=True)

    