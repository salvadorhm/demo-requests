import requests
import json

result =requests.get('https://www.googleapis.com/books/v1/volumes?q=sinsajo')

# print(result.status_code)
# print(result.headers["Content-Type"])
books = result.json()

print(books)

# print(books.keys())
# print(books["totalItems"])

items = books["items"]

# print(items[0].keys())

encoded = json.dumps(items)
decoded = json.loads(encoded)

print(decoded[5]["volumeInfo"]["infoLink"])