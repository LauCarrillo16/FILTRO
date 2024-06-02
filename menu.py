import datos
import gestionCampus

def menuPrincipal():
    datos.cargarDatos()
    while True:
        print("Bienvenido al sistema de gestion de Campus")
        print("1. Registrar nuevo Camper")
        opc = 0
        try:
            opc = int(input("Ingrese la opcion deseada: "))
        except Exception:
            print("Opcion invalida")
        if opc == 1:
            gestionCampus.registrarCamper()