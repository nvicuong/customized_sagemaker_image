import requests

url = "http://localhost:8080/invocations"

data = "1,2,3,4"

# Gửi yêu cầu POST
response = requests.post(url, data=data, headers={'Content-Type': 'text/csv'})

# In kết quả
if response.status_code == 200:
    try:
        # Kiểm tra và phân tích dữ liệu JSON
        print(response.json())
    except requests.exceptions.JSONDecodeError:
        print("Received non-JSON response")
        print("Response text:", response.text)
else:
    print(f"Request failed with status code {response.status_code}")
    print("Response text:", response.text)
