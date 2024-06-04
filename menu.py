import datos
import gestionCampus

def menuPrincipal():
    while True:
        print("Bienvenido al sistema de gestion de CampusLands")
        print("1. Coordinador")
        print("2. Trainer")
        print("3. Camper")
        print("4. Salir")
        opc = 0
        try:
            opc = int(input("Ingrese la opcion deseada: "))
        except Exception:
            print("Opcion invalida")
        if opc == 1:
            menuCoordinador()
        if opc == 2:
            menuTrainer()
    

def menuCoordinador():
    datos.cargarDatos()
    while True:
        print("Bienvenido Coordinador")
        print("1. Registrar camper")
        print("2. Registrar nota de camper registrado")
        print("3. Registrar nueva ruta")
        print("4. Registrar nuevo Stack")
        print("5. Registrar Trainer")
        print("6. Matriculas (asignar camper a ruta o trainer a ruta)")
        print("7. Reportes")

        opc = 0
        try:
            opc = int(input("Ingrese la opcion deseada: "))
        except Exception:
            print("Opcion invalida")
        if opc == 1:
            gestionCampus.registrarCamper()
        elif opc == 2:
            gestionCampus.registrarNotaCamper()
        elif opc == 3:
            gestionCampus.registrarRuta()
        elif opc == 4:
            gestionCampus.nuevoStack()
        elif opc == 5:
            gestionCampus.registrarTrainer()
        elif opc == 6:
            menuMatriculas()
        elif opc == 7:
            menuReportes()

        
def menuMatriculas():
    datos.cargarDatos()
    while True:
        print("Gestion de Matriculas")
        print("1. Asignar ruta a un Camper")
        print("2. Asignar Trainer a ruta y stack")
        opc = 0
        try:
            opc = int(input("Ingrese la opcion deseada: "))
        except Exception:
            print("Opcion invalida")
        if opc == 1:
            gestionCampus.asignarRuta()
        elif opc == 2:
            gestionCampus.asginarTrainerRuta()

def menuReportes():
    datos.cargarDatos()
    while True:
        print("Reportes")
        print("1. Campers que se encuentren enestado inscrito")
        print("2. Campers que aprobaron el examen inicial")
        print("3. Campers que cuentan con riesgo algo")
        print("4. Trainers de CampusLands")
        print("5. Campers y Trainers asociados a una ruta")
        print("6. Cuantos Campers perdieron y aprobaron los modulos y su entrenador")
        opc = 0
        try:
            opc = int(input("Ingrese la opcion deseada: "))
        except Exception:
            print("Opcion invalida")
        if opc == 1:
            gestionCampus.campersInscritos()
        elif opc == 2:
            gestionCampus.campersAprobados()
        elif opc == 3:
            gestionCampus.campersRiestoA()


            
def menuTrainer():
    datos.cargarDatos()
    while True:
        print("Bienvenido Trainer")
        print("1. Asignar notas del modulo")
        opc = 0
        try:
            opc = int(input("Ingrese la opcion deseada: "))
        except Exception:
            print("Opcion invalida")
        if opc == 1:
            gestionCampus.evaluarModulo()