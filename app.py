from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():
	host_name = socket.gethostname()
	host_ip = socket.gethostbyname(host_name)
	node_name = os.getenv("MY_NODE_NAME")
	html = "<h3>Hello {name}!</h3> <b>Hostname:</b> {hostname}<br/><b>Host IP:</b> {ip} <br/><b>Node Name:</b> {nodename} <br/>"
	return html.format(name=os.getenv("NAME"), hostname=host_name, ip=host_ip, nodename=node_name)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8090)