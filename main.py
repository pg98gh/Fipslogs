from flask import Flask, redirect, render_template,request,url_for,jsonify,render_template_string
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

@app.route("/index", methods=['POST','GET'])
def index():
    getNamespaces()
    namespaces=['kube-system','azure','test','default'] #get all namespaces from given cluster
    return render_template('index.html', namespaces=namespaces)

@app.route("/submit_namespace", methods=["POST"])
def namespaceData():
    selected_namespace = request.form.get('namespace')
    print("Selected namespace:", selected_namespace)
    getPods(selected_namespace)
    # Mock data - will be generated/passed by kubectl
    pods = [
        {'name': 'pod-1', 'cpu': '250m / 2vCPU', 'memory': '1.2Gi / 8Gi', 'status': 'Healthy'},
        {'name': 'pod-2', 'cpu': '150m / 2vCPU', 'memory': '1.2Gi / 8Gi', 'status': 'Unhealthy'},
        {'name': 'pod-3', 'cpu': '550m / 2vCPU', 'memory': '1.2Gi / 8Gi', 'status': 'Healthy'},
        {'name': 'pod-4', 'cpu': '1240Mi / 2vCPU', 'memory': '1.2Gi / 8Gi', 'status': 'Unhealthy'},
        {'name': 'pod-5', 'cpu': '750Mi / 2vCPU', 'memory': '1.2Gi / 8Gi', 'status': 'Healthy'},
        
    ]
    nodes = [
        {'name': 'node-1', 'cpu': '250m / 2vCPU', 'memory': '1.2Gi / 8Gi', 'status': 'Healthy'},
        {'name': 'node-2', 'cpu': '2000m / 2vCPU', 'memory': '1.2Gi / 8Gi', 'status': 'Unhealthy'},
        {'name': 'node-3', 'cpu': '230m / 2vCPU', 'memory': '1.2Gi / 8Gi', 'status': 'Healthy'},
        {'name': 'node-4', 'cpu': '550m / 2vCPU', 'memory': '1.2Gi / 8Gi', 'status': 'Healthy'},
        {'name': 'node-5', 'cpu': '1980m / 2vCPU', 'memory': '1.2Gi / 8Gi', 'status': 'Unhealthy'},
    ]

    # Render nodes and pods HTML content
    nodes_html = render_template_string("""
    <h2>Node Overview of Cluster</h2>
    <table>
        <thead>
            <tr>
                <th>Node Name</th>
                <th>CPU Usage</th>
                <th>Memory Usage</th>
                <th>Status</th>
            </tr>
        </thead>
        <tbody>
            {% for node in nodes %}
            <tr>
                <td>{{ node.name }}</td>
                <td>{{ node.cpu }}</td>
                <td>{{ node.memory }}</td>
                <td class="{% if node.status == 'Healthy' %}status-green{% else %}status-red{% endif %}">
                    {{ node.status }}
                </td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
    """, nodes=nodes)

    pods_html = render_template_string("""
    <h2>Pod Overview (Namespace: {{ selected_namespace }})</h2>
    <table>
        <thead>
            <tr>
                <th>Pod Name</th>
                <th>CPU Usage</th>
                <th>Memory Usage</th>
                <th>Status</th>
            </tr>
        </thead>
        <tbody>
            {% for pod in pods %}
            <tr>
                <td>{{ pod.name }}</td>
                <td>{{ pod.cpu }}</td>
                <td>{{ pod.memory }}</td>
                <td class="{% if pod.status == 'Healthy' %}status-green{% else %}status-red{% endif %}">
                    {{ pod.status }}
                </td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
    """, pods=pods, selected_namespace=selected_namespace)

    return jsonify(nodesHTML=nodes_html, podsHTML=pods_html)

from typing import List
def getNamespaces() -> List[str] :
    namespace_query = subprocess.run(['echo', 'get', 'namespaces'], check=True, text=True) # run kubectl get namespaces --> returns namespaces
    print (namespace_query.stdout, type(namespace_query.stdout), "inside get ns method")
    #namespaces= namespace_query.stdout.strip.split()
    return namespace_query #namespaces 

def getPods(namespace:str) -> List[str]:
    pod_query = subprocess.run(['echo', 'get', 'pods', '-n', namespace, '-o', 'wide'], check=True, text=True) # run kubectl get pods --> returns pods
    print (pod_query.stdout, type(pod_query.stdout), "inside get pod method")
    #pods= pod_query.stdout.strip.split()
    return pod_query

def getNodes() -> List[str]:
    node_query = subprocess.run(['echo', 'get', 'nodes' '-o', 'wide'], check=True, text=True) # run kubectl get nodes --> returns nodes with name, status, roles, age, version, internal-ip, external-ip
    print (node_query.stdout, type(node_query.stdout), "inside get pod method")
    #nodes= pod_query.stdout.strip.split()
    return node_query

def topNodes() -> List[str]:
    top_query = subprocess.run(['echo', 'top', 'nodes'], check=True, text=True) # run kubectl top nodes --> returns name, CPU(cores),CPU%, Memory(bytes), Memory%
    print (top_query.stdout, type(top_query.stdout), "inside get pod method")
    #tops= pod_query.stdout.strip.split()
    return top_query

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)