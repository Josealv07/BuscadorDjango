import requests

#endpoint = "https://www.github.com"
endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, json = {"title":"Hello World 3", "price":"ac1203"}) #Http Request
print(get_response.json()) # print raw text response
print(get_response.status_code)