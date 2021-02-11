class Diccionarios():

    def __init__(self):
        pass

    def diccionario(self):
        data = {}
        data["nombre"] = "Dejah"
        data["edad"] = 23
        data["nombre"] = "John"
        data["edad"] = 24

        status = {}
        status["estado_civil"] = "casada"
        status["email"] = "dejah@barson"

        calificaciones = []

        calificaciones.append(10)
        calificaciones.append(9)
        calificaciones.append(10)

        data["status"] = status
        data["calificaciones"] = calificaciones

        for row in data:
            print(data[row])




    def arreglos(self):
        data = []

        persona = {}
        persona["nombre"] = "Dejah"
        persona["edad"] = 23
        data.append(persona)

        persona = {"nombre":"John", "edad":24}
        data.append(persona)

        for row in data:
            print(row)

objeto = Diccionarios()
objeto.diccionario()
# objeto.arreglos()
