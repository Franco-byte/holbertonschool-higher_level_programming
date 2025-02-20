import requests
import csv

def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        print("Status Code: 200")
        resp_json = response.json()
    
        for post in resp_json:
            print(post['title'])

def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        posts = response.json()

        keysname = ["id", "title", "body"]

        with open("posts.csv", mode="w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=keysname)
            writer.writeheader()

            for post in posts:
                writer.writerow({"id": post["id"], "title": post["title"], "body": post["body"]})

