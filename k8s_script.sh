#!bin/bash
echo "Starting k8s script!"

echo kubectl top nodes

echo "Please choose your namespace: " 

echo kubectl get namespaces

echo kubectl get pods -n $namespace -o wide

echo kubectl describe pod $pod -n $namespace

echo kubectl top pods -n $namespace

echo "Script finished!!"