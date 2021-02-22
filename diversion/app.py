import web
import json
urls = (
    '/operaciones?', 'Operaciones'
)
app = web.application(urls, globals())

class Operaciones:

    def suma(self, num1, num2):
        return num1 + num2

    def resta(self, num1, num2):
        return num1 - num2

    def multi(self, num1,num2):
        return num1 * num2

    def POST(self):
        try:
            parametros = web.input() # Parametros por URL
            num1 = int(parametros.num1)
            num2 = int(parametros["num2"])
        
            operacion = parametros["operacion"]

            if operacion == "suma":
                result = self.suma(num1,num2)
            elif operacion == "resta":
                result = self.resta(num1,num2)
            elif operacion == "multi":
                result = self.multi(num1,num2)

            data = {}
            data["operacion"] = operacion
            data["result"] = result

            return json.dumps(data)

        except:
            data = {}
            data["mensaje"] = "solo se aceptan numeros enteros"
            return json.dumps(data)

if __name__ == "__main__":
    app.run()

