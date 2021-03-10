import web
import json

urls = (
    '/read?', 'Read'
)
app = web.application(urls, globals())

class Read():

    def POST(self):
        try:
            data  = web.input() # Parametros por URL
            
            num1 = int(data.num1)
            num2 = int(data.num2)

            add = num1 + num2

            result = {}
            result["status"] = 200
            result["add"] = add

            return json.dumps(result)
        except:
            data = {}
            data["status"] = 400
            data["message"] = "Solo se aceptan numeros enteros"
            return json.dumps(data)

if __name__ == "__main__":
    app.run()
