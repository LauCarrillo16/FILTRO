import json

data = {}

rutaArchivo = "db.json"

def guardarDatos():
    global data
    global rutaArchivo
    try:
        contenido = json.dumps(data, indent = 4)
        with open(rutaArchivo, "w") as file:
            file.write(contenido)
        print("Datos guardados exitosamente")
    except Exception as e:
        print("Error al guardar datos")

def cargarDatos():
    global data
    global rutaArchivo
    try:
        with open(rutaArchivo, "r") as file:
            data = json.load(file)
        print("Datos cargados exitosamente")
    except Exception as e:
        print("Error al cargar datos")