import datos

#Funciones Coordinador
#Nuevo Camper
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

#Registrar nota de camper registrado
def registrarNotaCamper():
    cc = input("Ingrese el numero de documento del camper: ")

    for camper in datos.data["campers"]:
        if camper["cc"] == cc:
            print(f"Camper encontrado: {camper["nombre"]}{camper["apellido"]}")

        notaRegistroTeo = int(input("Ingrese la nota teorica del camper: "))
        notaRegistroPrac = int(input("Ingrese la nota practica del camper: "))

        promedio = (notaRegistroTeo + notaRegistroPrac)//2

        if promedio >= 60:
            camper["estatus"] = "Aprobado"
            camper["riesgo"] = "bajo"
        else:
            camper["estatus"] = "Reprobado"
            camper["riesgo"] = "alto"
        
        camper["notasRegistro"] = {
            "notaTeorica": notaRegistroTeo,
            "notaPractica": notaRegistroPrac,
            "promedio": promedio
        }

        datos.guardarDatos()
        print("Notas registradas y camper actualizado con exito")
        return
    print("No se encontro el camper")