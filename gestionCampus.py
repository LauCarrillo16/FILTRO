import datos

def registrarCamper():
    camper = {
        "cc": input("Ingrese el numero de documento del nuevo camper: "),
        "nombre": input("Ingrese el nombre del nuevo camper: "),
        "apellido": input("Ingrese el apellido del nuevo camper: "),
        "direccion": input("Ingrese la direccion del nuevo camper: "),
        "acudiente": input("Ingrese el nombre del acudiente del camper: "),
        "contacto": {
            "movil": input("Ingrese el telefono movil del acudiente: "),
            "fijo": input("Ingrese el telefono fijo del acudiente: ")
        },
        "estatus": "Inscrito",
        "riesgo": ""
    }
    datos.data["campers"].append(camper)
    datos.guardarDatos()
    print("Camper registrado con exito")
