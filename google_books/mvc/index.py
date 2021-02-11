import web
import requests
import json

render = web.template.render("mvc/")

class Index():

    def GET(self):
        books = None
        return render.index(books)

    def POST(self):
        form = web.input()
        book_name = form["book_name"]
        result =requests.get('https://www.googleapis.com/books/v1/volumes?q='+book_name)
        books = result.json()
        items = books["items"]
        encoded = json.dumps(items)
        decoded = json.loads(encoded)

        books = []

        for book in decoded:
            url = book["volumeInfo"]["infoLink"]

            datos = {
                "book_name":book_name,
                "url":url
            }
            books.append(datos)
        
        print(books)

        return render.index(books)
        
