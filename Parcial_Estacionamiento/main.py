from union import *
from utilidades import *
import json
import os

path_estacionamientos = "db_estacionamientos.json"

#ESTACIONAMIENTOS = estacionamiento_leer(path_estacionamientos)



'''
[MENU]
[1] Nuevo estacionamiento
[2] Ingreso de vehículo
[3] Egreso de vehículo
[4] Modificar costes por hora de vehiculos
[5] Listar vehículos estacionados (map)
[6] Listar vehículos ordenados por patente (descendente)
[7] Recaudación total de todos los estacionamientos (reduce)
[8] Listar vehiculos filtrados por cantidad de minutos estacionados que superen los 60 min (filter)
[9] Guardar archivo 'db_estacionamientos.csv'
[10] Ver log de ingresos y egresos
'''

def main():
    opc = ["Nuevo estacionamiento","Ingreso de vehículo","Egreso de vehículo","Modificar costes por hora de vehiculos","Listar vehículos estacionados","Listar vehículos ordenados por patente","Recaudación total de todos los estacionamientos","Listar vehiculos filtrados por cantidad de minutos estacionados que superen los 60 min","Guardar archivo","Ver log de ingresos y egresos"]
    os.system("cls")
    while True:
        match menu("Menu Estacionamiento LUKI", opc, "estacionamiento"):
            case 1:
                punto_1()
            case 2:
                punto_2()
            case 3:
                punto_3()
            case 4:
                punto_4()
            case 5:
                punto_5()
            case 6:
                punto_6()
            case 7:
                punto_7()
            case 8:
                punto_8()
            case 9:
                punto_9()
            case 10:
                punto_10()
            case 0:
                print(f"\nSaliendo")
                break

main()