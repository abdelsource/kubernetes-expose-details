from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():
	node_name = os.getenv("MY_NODE_NAME")
	namespace = os.getenv("MY_POD_NAMESPACE")
	pod_name = os.getenv("MY_POD_NAME")
	pod_ip = os.getenv("MY_POD_IP")
	pod_sa = os.getenv("MY_POD_SERVICE_ACCOUNT")

	html = "<h3>Hello {name}!</h3> <b>Node Name: </b> {nodename}<br/><b>POD Name: </b> {podname} <br/>"
	"<b>Namespace:</b> {namespace} <br/> <b>Pod IP:</b> {podip} <br/> <b>Pod Service Account:</b> {pod_sa} <br/>"
	return html.format(name=os.getenv("NAME"), nodename=node_name, podname=pod_name, namespace=namespace, podip=pod_ip,pod_sa=pod_sa)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8090)