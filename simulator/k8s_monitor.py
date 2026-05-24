from kubernetes import client, config

def get_pod_status():

    try:

        config.load_kube_config()

        v1 = client.CoreV1Api()

        pods = v1.list_namespaced_pod(namespace="default")

        pod_data = []

        for pod in pods.items:

            pod_data.append({
                "name": pod.metadata.name,
                "status": pod.status.phase
            })

        return pod_data

    except Exception:

        return []