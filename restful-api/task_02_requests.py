import requests
import json

def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        print("Status Code: 200")
        resp_json = response.json()
        dict_json = json.loads(resp_json)
    
        for key, value in resp_json:
            if key == "title":
                print(value)


fetch_and_print_posts()