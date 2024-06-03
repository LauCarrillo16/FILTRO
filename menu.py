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
    

def menuCoordinador():
    while True:
        print("Bienvenido Coordinador")
        print("1. Registrar camper")
        print("2. Registrar nota de camper registrado")
        print("3. Registrar nueva ruta")
        print("4. Registrar nuevo Stack")
        print("5. Matriculas (asignar camper a ruta o trainer a ruta)")
        print("6. Registrar Trainer")
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
            menuMatriculas()
        elif opc == 6:
            gestionCampus.registrarTrainer()
        
def menuMatriculas():
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
            