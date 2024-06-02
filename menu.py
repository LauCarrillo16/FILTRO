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
        opc = 0
        try:
            opc = int(input("Ingrese la opcion deseada: "))
        except Exception:
            print("Opcion invalida")
        if opc == 1:
            gestionCampus.registrarCamper()
        elif opc == 2:
            gestionCampus.registrarNotaCamper()
        