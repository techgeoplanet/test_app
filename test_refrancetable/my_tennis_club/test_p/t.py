import requests

url = "https://ubiquitous-fiesta-jjqqp4q9gqrhp59v-8000.app.github.dev/api/students/"
data = {
    "name": "YourName",
    "course": 2
}

response = requests.post(url, data=data)

if response.status_code == 200:
    print("POST request was successful!")
else:
    print(f"POST request failed with status code: {response.status_code}")
