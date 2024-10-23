from flask import Flask, redirect, render_template,request,url_for,jsonify
from datetime import *
import subprocess 
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(username, password)

        if username == 'admin' and password == 'superduperroot':
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error="Invalid credentials")
    
    return render_template('login.html')

@app.route("/index")
def index():
    process = subprocess.Popen(['bash', 'k8s_script.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()
    output_lines = stdout.splitlines()
    if len(output_lines) > 1:
        kubectl_top_nodes = output_lines[1]  # kubectl top nodes
    if len(output_lines) > 3:
        kubectl_get_namespaces = output_lines[3]  # kubectl get namespaces
    if len(output_lines) > 4:
        kubectl_get_pods = output_lines[4]  # kubectl get pods -n $namespace -o wide
    if len(output_lines) > 5:
        kubectl_describe_pod = output_lines[5]  # kubectl describe pod $pod -n $namespace
    if len(output_lines) > 6:
        kubectl_top_pods = output_lines[6]  # kubectl top pods -n $namespace
    if len(output_lines) > 7:
        kubectl_get_nodes = output_lines[7]
    namespace=['kube-system','azure','test','default'] # wird zu kubectl_get_namespaces
    pods= nodes = [
        {'name': 'pod-1', 'cpu': '250m / 2vCPU', 'memory': '1.2Gi / 8Gi', 'status': 'Healthy'},
        {'name': 'pod-2', 'cpu': '180m / 2vCPU', 'memory': '900Mi / 8Gi', 'status': 'Healthy'},
        {'name': 'pod-3', 'cpu': '350m / 2vCPU', 'memory': '2.3Gi / 8Gi', 'status': 'Unhealthy'},
        {'name': 'pod-4', 'cpu': '150m / 2vCPU', 'memory': '750Mi / 8Gi', 'status': 'Healthy'}
    ] # wird zu kubectl_get_pods
    nodes = [
        {'name': 'node-1', 'cpu': '250m / 2vCPU', 'memory': '1.2Gi / 8Gi', 'status': 'Healthy'},
        {'name': 'node-2', 'cpu': '180m / 2vCPU', 'memory': '900Mi / 8Gi', 'status': 'Healthy'},
        {'name': 'node-3', 'cpu': '350m / 2vCPU', 'memory': '2.3Gi / 8Gi', 'status': 'Unhealthy'},
        {'name': 'node-4', 'cpu': '150m / 2vCPU', 'memory': '750Mi / 8Gi', 'status': 'Healthy'}
    ] # wird zu kubectl_get_nodes
    return render_template('index.html', namespace=namespace,pods=pods,nodes=nodes)


    
    

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)