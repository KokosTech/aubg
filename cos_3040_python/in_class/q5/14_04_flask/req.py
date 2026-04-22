import requests

res = requests.post("http://localhost:5000/hello", data="alice")

if res.status_code == 200:
    print(res.json())
else:
    print("Request failed with status code:", res.status_code)
    print("Response content:", res.text)
