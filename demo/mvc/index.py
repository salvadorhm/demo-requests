import web
import requests
import json

render = web.template.render("mvc/")

class Index():

    def GET(self):
        datos = None
        return render.index(datos)

    def POST(self):
        form = web.input()
        book_name = form["book_name"]
        result =requests.get('https://www.googleapis.com/books/v1/volumes?q='+book_name)
        books = result.json()
        items = books["items"]
        encoded = json.dumps(items)
        decoded = json.loads(encoded)

        url = decoded[5]["volumeInfo"]["infoLink"]

        datos = {
            "book_name":book_name,
            "url":url
        }

        return render.index(datos)
        
