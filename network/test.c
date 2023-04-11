#Pod
kubectl run nginx - pod-- image = nginx-- port 80 kubectl get pods
                                      ip address
                                          kubectl get pods -
                                  o wide
                                      watch kubectl get pods -
                                  o wide
                                      kubectl delete pod {}
kubectl create - f nginx - pod.yaml kubectl describe pod {}
kubectl exec - it {}
-- / bin / bash curl {}
kubectl exec - it {}
-- / bin / bash echo "Hello World" > / usr / share / nginx / html / index.html cat / usr / share / nginx / html / index.html curl{} : 80

#replicaset
                                                                                                                  kubectl delete pod
{
}
kubectl apply - f {}
watch kubectl get replicaset, pods - o wide
                                         kubectl scale replicaset {}
--replicas = 2 kubectl describe replicaset {}
kubectl delete pod {}
kubectl run testpod-- image = nginx-- labels = app = webui-- port 80 kubectl delete replicaset {}

3 deploy
        kubectl create deployment nginx -
    pod-- image = nginx-- replicas = 2 kubectl get deployments,
          replicaset, pods - o wide kubectl delete deployments {}
kubectl create deployment nginx - pod-- image = nginx-- replicas = 2

    kubectl delete deployments
{
}
kubectl create - f {}
kubectl scale deployment {}
--replicas = 2 kubectl scale deployment {}
--replicas = 3

    kubectl describe deployments
{
}
kubectl delete replicaset {}