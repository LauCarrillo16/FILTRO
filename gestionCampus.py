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

#Registrar ruta
def registrarRuta():
    nombreRuta = input("Ingrese el nombre de la nueva ruta: ")
    nuevaRuta = {
        "nombre": nombreRuta,
        "modulos": {
            "Fundamentos de programacion":[],
            "Programacion web": [],
            "Programacion formal": [],
            "Bases de datos": [],
            "Backend": []
        }
    }
    print("A continuacion ingrese los temas para cada modulo")
    
    for modulo in nuevaRuta["modulos"]:
        print(f"\nIngrese los temas para el modulo '{modulo}' (separado por comas): ")
        temas = input().split(",")

        temas = [tema.strip() for tema in temas]

        nuevaRuta["modulos"][modulo] = temas

    if "rutas" not in datos.data:
        datos.data["rutas"] = []
    datos.data["rutas"].append(nuevaRuta)

    datos.guardarDatos()
    print("Ruta registrada con exito")


def nuevoStack():
    nombreStack = input("Ingrese el nombre del nuevo stack: ")
    capacidad = int(input("Ingrese la capacidad del Stack: "))
    horas = int(input("Ingrese las horas ocupadas: "))
    
    nuevoStack = {
        nombreStack: {
            "capacidad": capacidad,
            "horas": horas
        }
    }

    datos.data["stacks"][0].update(nuevoStack)

    datos.guardarDatos()
    print("Stack creado con exito")