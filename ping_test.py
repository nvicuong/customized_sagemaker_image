import requests

def ping_service(url):
    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

ping_service("http://localhost:8080/ping")
