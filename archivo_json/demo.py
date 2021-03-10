http:/direccion/operaciones?operacion=suma&num1=10&num2=2
{
    "operacion" : "suma",
    "resultado" : 12
}

http:/direccion/operaciones?operacion=resta&num1=10&num2=2
{
    "operacion" : "resta",
    "resultado" : 8
}

http:/direcion/agenda?action=get

{
    "edades":[
        {
            "nombre" : "Dejah",
            "fecha_nacimiento" : "01/01/2000",
            "edad" : 21
        }
    ]
}

http:/direcion/agenda?action=put&nombre=John&fecha_nacimiento=01/01/1999

{
    "resultado" : "registro almacenado"
}

http:/direcion/agenda?action=get

{
    "edades":[
        {
            "nombre" : "Dejah",
            "fecha_nacimiento" : "01/01/2000",
            "edad" : 21
        },
        {
            "nombre" : "John",
            "fecha_nacimiento" : "01/01/2000",
            "edad" : 22
        }
    ]
}