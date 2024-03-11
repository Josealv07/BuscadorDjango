import requests

#endpoint = "https://www.github.com"
endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint, params={"abc":123}, json = {"prueba":"json"}) #Http Request
print(get_response.json()) # print raw text response
print(get_response.status_code)