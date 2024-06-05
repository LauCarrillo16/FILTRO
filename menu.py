import datos
import gestionCampus

def menuPrincipal():
    datos.cargarDatos()
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
        elif opc == 2:
            menuTrainer()
        elif opc == 3:
            menuCamper()
        elif opc == 4:
            break
        
    

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
        print("8. Regresar al menu principal")

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
        elif opc == 8:
            break

        
def menuMatriculas():
    datos.cargarDatos()
    while True:
        print("Gestion de Matriculas")
        print("1. Asignar ruta a un Camper")
        print("2. Asignar Trainer a ruta y stack")
        print("3. Regresar al menu anterior")
        opc = 0
        try:
            opc = int(input("Ingrese la opcion deseada: "))
        except Exception:
            print("Opcion invalida")
        if opc == 1:
            gestionCampus.asignarRuta()
        elif opc == 2:
            gestionCampus.asginarTrainerRuta()
        elif opc == 3:
            break

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
        print("7. Regresar al menu de Coordinador")
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
        elif opc == 4:
            gestionCampus.trainersCampus()
        elif opc == 5:
            gestionCampus.campersYtrainersRuta()
        elif opc == 6:
            gestionCampus.cuantosPYA()
        elif opc == 7:
            break

            
def menuTrainer():
    datos.cargarDatos()
    while True:
        print("Bienvenido Trainer")
        print("1. Asignar notas del modulo")
        print("2. Regresar al menu principal")
        opc = 0
        try:
            opc = int(input("Ingrese la opcion deseada: "))
        except Exception:
            print("Opcion invalida")
        if opc == 1:
            gestionCampus.evaluarModulo()
        elif opc == 2:
            break

def menuCamper():
    datos.cargarDatos()
    while True:
        print("Bienvenido Camper")
        print("1. Ver mis datos")
        print("2. Regresar al menu principal")
        opc = 0
        try:
            opc = int(input("Ingrese la opcion deseada: "))
        except Exception:
            print("Opcion invalida")
        if opc == 1:
            gestionCampus.verMisDatos()
        elif opc == 2:
            break
