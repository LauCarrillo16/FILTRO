import datos

#Funciones Coordinador}

#Bucar camper por cc
def especificoCamper(cc):
    for camper in datos.data["campers"]:
        if camper["cc"] == cc:
            return camper
    return None

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
        "riesgo": "",
        "rutaAsignada": ""
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

#Nuevo stack
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


#Asignar ruta a camper
def asignarRuta():
    cc = input("Ingrese el numero de documento del camper: ")
    camper = especificoCamper(cc)

    if camper: 
        if camper["estatus"] != "Aprobado":
            print("Este camper no esta en estado Aprobado, no se puede asignar ruta")
            return

        if camper.get("rutaAsignada"):
            print("Este camper ya tiene ruta asignada")
            return
        else:
            print("Rutas disponibles")
            for idx, ruta in enumerate(datos.data["rutas"], start = 1):
                print(f"{idx}. {ruta['nombre']}")

            opc = input("Seleccione una ruta para asignar al camper: ")

            try:
                opc = int(opc)
                if 1 <= opc <= len(datos.data["rutas"]):
                    rutaAsignada = datos.data["rutas"][opc - 1]["nombre"]

                    for stack in datos.data["stacks"][0].items():
                        if stack["capacidad"] < stack["capacidadMaxima"]:
                            stack["capacidad"] +=1
                            camper["rutaAsignada"] = rutaAsignada
                            datos.guardarDatos()
                            print(f"Camper asignado a la ruta '{rutaAsignada}' con exito")
                            return
                    print("No hay capacidad disponible en los stacks para asignar camper")
                else:
                    print("Opcion invalida")
            except ValueError:
                print("Opcion invalida")
    else:
        print("No se encontro el camper")

#Registrar nuevo Trainer
def registrarTrainer():
    trainer = {
        "cc": input("Ingrese el numero de documento del nuevo trainer: "),
        "nombre": input("Ingrese el nombre del nuevo trainer: "),
        "apellido": input("Ingrese el apellido del nuevo trainer: "),
        "direccion": input("Ingrese la direccion del nuevo trainer: "),
        "contacto": input("Ingrese el telefono movil: "),

    }
    datos.data["trainers"].append(trainer)
    datos.guardarDatos()
    print("Trainer registrado con exito")