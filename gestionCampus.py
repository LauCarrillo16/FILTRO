import datos
from datetime import datetime

#Funciones Coordinador}

#Bucar camper por cc
def especificoCamper(cc):
    for camper in datos.data["campers"]:
        if camper["cc"] == cc:
            return camper
    return None

#Buscar trainer por cc
def especificoTrainer(cc):
    for trainer in datos.data["trainers"]:
        if trainer["cc"] == cc:
            return trainer
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
            print(f"Camper encontrado: {camper['nombre']} {camper['apellido']}")

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

    horas = {
        "h1": "6am",
        "h2": "10am",
        "h3": "2pm",
        "h4": "6pm"
    }

    for stack in datos.data["stacks"]:
        if "horarios" not in stack:
            stack["horarios"]= {}
        for key, hora in horas.items():
            if key not in stack["horarios"]:
                stack["horarios"][key] ={
                    "hora": hora,
                    "Trainer" :None,
                    "ruta": None
                }
    datos.guardarDatos()
    print("Ruta registrada con exito")

#Nuevo stack
def nuevoStack():
    nombreStack = input("Ingrese el nombre del nuevo stack: ")
    capacidad = int(input("Ingrese la capacidad del Stack: "))
    
    nuevoStack = {
        nombreStack: {
            "capacidad": capacidad
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
                    rutaAsignada = datos.data["rutas"][opc - 1]

                    print(f"Ruta seleccionada: {rutaAsignada['nombre']}")
                    for trainer in datos.data["trainers"]:
                        for rutaAsignadaTrainer in trainer["rutasAsignadas"]:
                            if rutaAsignadaTrainer["ruta"] == rutaAsignada["nombre"]:
                                print(f"Trainer: {trainer['nombre']} {trainer['apellido']}")
                    
                    print("Stacks disponibles: ")
                    for idx, stack in enumerate(datos.data["stacks"], start=1):
                        print(f"{idx}. {stack['nombre']} - Capacidad: {stack['capacidad']}/{stack['capacidadMaxima']}")
                        print("Horarios: ")
                        for key, horario in stack["horarios"].items():
                            print(f"{key}: {horario['hora']} - Trainer: {horario['trainer']}, Ruta: {horario['ruta']}")


                    stackSelect = int(input("Seleccione un stack: "))-1
                    if stackSelect < 0 or stackSelect >= len(datos.data["stacks"]):
                        print("Stack no existe")
                        return

                    stack = datos.data["stacks"][stackSelect]

                    print("Horarios disponibles: ")
                    for key, horario in stack["horarios"].items():
                        print(f"{key}: {horario['hora']}")

                    horarioSelec = input("Seleccion el horario para asignar (h1, h2, h3): ")
                    if horarioSelec not in stack["horarios"]:
                        print("Horario invalido")
                        return
                    horario = stack["horarios"][horarioSelec]
                    
                    if stack["capacidad"] < stack["capacidadMaxima"]:
                        fechaInicio = input("Ingresa la fecha de inicio (YYYY-MM-DD): ")
                        fechaFin = input("Ingresa la fecha de fin (YYYY-MM-DD): ")
                        try:
                            fechaInicio = datetime.strptime(fechaInicio, "%Y-%m-%d")
                            fechaFin = datetime.strptime(fechaFin, "%Y-%m-%d")
                        except ValueError:
                            print("Formato de fecha invalido")
                            return
            
                        stack["capacidad"] +=1
                        camper["rutaAsignada"] = rutaAsignada
                        camper["fechaInicio"] = fechaInicio.strftime('%Y-%m-%d')
                        camper["fechaFin"] = fechaFin.strftime('%Y-%m-%d')
                        datos.guardarDatos()
                        print(f"Camper asignado a la ruta '{rutaAsignada}' con exito")
                        print(f"Fecha de inicio: {fechaInicio.strftime('%Y-%m-%d')}")
                        print(f"Fecha de finalización: {fechaFin.strftime('%Y-%m-%d')}")
                    else:
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
        "rutasAsignadas":[]

    }
    datos.data["trainers"].append(trainer)
    datos.guardarDatos()
    print("Trainer registrado con exito")

#Asignar Trainer a ruta y stack
def asginarTrainerRuta():
    cc = input("Ingrese el numero de documento del trainer: ")
    trainer = especificoTrainer(cc)

    if not trainer:
        print("Trainer no encontrado")
        return
    
    print("Rutas disponibles:")
    for idx, ruta in enumerate(datos.data["rutas"], start=1):
        print(f"{idx}. {ruta['nombre']}")

    rutaSlec = int(input("Seleccione la ruta a asignar: ")) -1
    if rutaSlec < 0 or rutaSlec >= len(datos.data["rutas"]):
        print("Opcion invalida")
        return
    ruta = datos.data["rutas"][rutaSlec]

    print("Stacks disponibles:")
    for idx, stack in enumerate(datos.data["stacks"], start=1):
        print(f"{idx}. {stack['nombre']}")

    stackSlec = int(input("Seleccione un stack: "))-1
    if stackSlec < 0 or stackSlec >= len(datos.data["stacks"]):
        print("Opcion invalida")
        return
    stack = datos.data["stacks"][stackSlec]

    print("Horarios disponibkles:")
    for key, horario in stack["horarios"].items():
        print(f"{key}. {horario['hora']}")
    
    horarioSelec = input("Seleccion el horario para asignar (h1, h2, h3): ")
    if horarioSelec not in stack["horarios"]:
        print("Horario invalido")
        return
    horario = stack["horarios"][horarioSelec]

    if horario["trainer"] is not None:
        print(f"Ya hay un trainer asignado en el stack '{stack['nombre']}' en el horario '{horario['hora']}'")
        return
    
    horario["trainer"] = trainer["cc"]
    horario["ruta"] = ruta["nombre"]

    trainer["rutasAsignadas"].append({
        "ruta": ruta["nombre"],
        "stack": stack["nombre"],
        "horario": horario["hora"]
    })
    datos.guardarDatos()
    print(f"Trainer '{trainer['nombre']} {trainer['apellido']}' asignado a la ruta '{ruta['nombre']}' en el stack '{stack['nombre']}' en el horario '{horario['hora']}' con éxito")

def evaluarModulo():
    cc = input("Ingrese el numero de documento del camper: ")
    camper = especificoCamper(cc)

    if not camper:
        print("Camper no encontrado")
        return
    
    if not bool(camper["rutaAsignada"]):
        print("Camper no tiene ruta asignada")
        return
    
    ruta = camper["rutaAsignada"]
    modulos = ruta["modulos"]
    
    print("Modulos disponibles: ")
    for idx, modulo in enumerate(modulos.keys(), start=1):
        print(f"{idx}. {modulo}")

    moduloSelec = int(input("Seleccione un modulo para evaluar: "))-1
    if moduloSelec < 0 or moduloSelec >= len(modulos):
        print("Opcion invalida")
        return
    
    moduloNombre = list(modulos.keys())[moduloSelec]
    modulo = modulos[moduloNombre]

    if isinstance(modulo, list):
        modulos[moduloNombre] ={}
        modulo = modulos[moduloNombre]

    if all(key in modulo for key in ["teorica", "practica", "quizesTrabajos"]):
        print("Modulo ya evaluado")
        return
    
    notaTeorica = int(input("Ingrese la nota de la prueba teorica: "))
    notaPractica = int(input("Ingrese la nota de la prueba practica: "))
    notaQuizesTrabajos = int(input("Ingrese la nota de los quizes y trabajos: "))

    promedio = (notaTeorica * 0.3) + (notaPractica * 0.6) + (notaQuizesTrabajos * 0.1)
    aprobado = promedio >= 60

    modulo["teorica"] = notaTeorica
    modulo["practica"] = notaPractica
    modulo["quizesTrabajos"] = notaQuizesTrabajos
    modulo["notaFinal"] = promedio
    modulo["aprobado"] = aprobado

    datos.guardarDatos()
    print(f"Evaluacion del modulo '{modulo}' completa")
    print(f"Nota final: {promedio:.2f} - {'Aproado' if aprobado else 'No Aprobado'}")

def calcularPromedioNotas(modulos):
    totalNotas = 0
    cantidadModulos = 0

    for modulo in modulos.values():
        if isinstance(modulo, dict) and "notaFinal" in modulo:
            totalNotas += modulo["notaFinal"]
            cantidadModulos += 1

        if cantidadModulos == 0:
            return 0
        return totalNotas // cantidadModulos
    
def actualizarRiesgo(camper):
    if "rutaAsignada" in camper and camper["rutaAsignada"]:
        ruta = camper["rutaAsignada"]
        modulos = ruta["modulos"]
        promedio = calcularPromedioNotas(modulos)

        if promedio < 60:
            camper["riesgo"] = "alto"
        else:
            camper["riesgo"] = "bajo"

        camper["notasRegistro"] = {
            "promedio": promedio
        }


def campersRiestoA():
    campers = datos.data["campers"]

    for camper in campers:
        actualizarRiesgo(camper)
    
    campersRiestoA = [camper for camper in campers if camper.get("riesgo") == "alto"]

    if not campersRiestoA:
        print("No hay campers con riesgo alto")
        return
    print("Campers con riesgo alto:")
    for camper in campersRiestoA:
        print(f"Nombre: {camper['nombre']} {camper['apellido']}, Documento: {camper['cc']}, Riesgo: {camper['riesgo']}")
    datos.guardarDatos()


def campersInscritos():
    campersInscritos = [camper for camper in datos.data["campers"] if camper.get("estatus") == "Inscrito"]

    if not campersInscritos:
        print("No hay campers inscritos")
        return
    print("Campers inscritos:")
    for camper in campersInscritos:
        print(f"Nombre: {camper['nombre']} {camper['apellido']}, Documento: {camper['cc']}, Estado: {camper['estatus']}")


def campersAprobados():
    campersAprobados = [camper for camper in datos.data["campers"] if "notasRegistro" in camper and camper["notasRegistro"].get("promedio", 0) >= 60]

    if not campersAprobados:
        print("No hay campers que hayan aprobado el examen inicial")
        return
    print("Campers que han aprobado el examen inicial:")
    for camper in campersAprobados:
        print(f"Nombre: {camper['nombre']} {camper['apellido']}, Documento: {camper['cc']}, Promedio: {camper['notasRegistro']['promedio']}")
        
