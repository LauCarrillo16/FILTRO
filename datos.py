import json

#se inicia diccionario vacipo
data = {}

#se asigna el nombre del archivo donde se guardaran los datos
rutaArchivo = "db.json"

def guardarDatos():
    #accedemos a las variables fuera de la funcion
    global data
    global rutaArchivo
    try:
        #convertimos el diccionario data a una cadena JSON con formato legible, 4 espacios de sangria
        contenido = json.dumps(data, indent = 4)
        #abre el archivo en modo escritura
        with open(rutaArchivo, "w") as file:
            #escribe el contenido JSON en el archivo
            file.write(contenido)
        print("Datos guardados exitosamente")
    except Exception as e:
        print("Error al guardar datos")

def cargarDatos():
    global data
    global rutaArchivo
    try:
        #abre el archivo en modo lectura
        with open(rutaArchivo, "r") as file:
            #lee el contenido del JSON y lo carga al diccionario data
            data = json.load(file)
        print("Datos cargados exitosamente")
    except Exception as e:
        print("Error al cargar datos")