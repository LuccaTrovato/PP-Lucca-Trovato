from estacionamiento import *
from vehiculo import *
from utilidades import *
import json
from functools import reduce

path_estacionamientos = "db_estacionamientos.json"

lista_estacionamientos = []


def estacionamiento_leer(path_estacionamientos) -> list[Estacionamiento]:

    lista_estacionamientos = []
    
    with open(path_estacionamientos, 'r') as archivo:
        lista_estacionamientos = json.load(archivo)
    
    return lista_estacionamientos



def estacionamiento_guardar(path) -> None:

    #lista_estacionamientos = estacionamiento_leer(path)
    nuevo_estacionamiento = alta_estacionamiento()
    lista_estacionamientos.append(nuevo_estacionamiento.convertir_obj_a_json())

    with open(path, 'w') as archivo:
        json.dump(lista_estacionamientos,archivo,indent=4)




def alta_vehiculo(estacionamiento_elegido) -> Vehiculo:

    tipo = get_str_validado("Ingrese el tipo de vehiculo (Auto/Moto): ", 0, 4)
    patente = get_str_validado("Ingrese la patente de su vehiculo (XXX-NNN): ", 0,8)


    nuevo_vehiculo = Vehiculo(tipo, patente)

    nuevo_vehiculo.set_estacionamiento_elegido(estacionamiento_elegido)

    return nuevo_vehiculo



def alta_estacionamiento() -> Estacionamiento:

    nombre_estacionamiento = get_str_validado("Ingrese el nombre del estacionamiento: ", 0, 15)
    cant_parcelas_autos = get_int_rango("Ingrese la cantidad de parcelas de autos: ","ERROR, ingrese dentro del rango(0 y 15)","ERROR, ingrese numeros", 0, 15)
    cant_parcelas_motos = get_int_rango("Ingrese la cantidad de parcelas de motos: ","ERROR, ingrese dentro del rango(0 y 15)","ERROR, ingrese numeros", 0, 15)
    coste_hora_auto = get_float_rango("Ingrese el costo de hora de auto: ", "ERROR, ingrese dentro del rango", "ERROR, Ingrese flotante", 0, 100000)
    coste_hora_moto = get_float_rango("Ingrese el costo de hora de moto: ", "ERROR, ingrese dentro del rango", "ERROR, Ingrese flotante", 0, 100000)

    nuevo_estacionamiento = Estacionamiento(nombre_estacionamiento, cant_parcelas_autos, cant_parcelas_motos, coste_hora_auto, coste_hora_moto)
    return nuevo_estacionamiento

def grabar_log(path: str, msj: str):
    #Formato: [Patente: XXX-NNN] [Hora ingreso: DD-MM-YYYY HH:MM] [Hora egreso: DD-MM-YYYYHH:MM] [Importe]
    pass


# MAIN

def punto_1() -> bool:
    nuevo_estacionamiento = alta_estacionamiento()
    #lista_estacionamientos = estacionamiento_leer(path_estacionamientos)
    #lista_estacionamientos.append(nuevo_estacionamiento.convertir_obj_a_json())    para que el punto 9 funcione, si no rompe porque esta convertido en json y no en objeto
    lista_estacionamientos.append(nuevo_estacionamiento)

def punto_2() -> bool:
    estacionamineto_valido = False

    #lista_estacionamientos = estacionamiento_leer(path_estacionamientos)

    mostrar_menu_estacionamientos(lista_estacionamientos)

    eleccion_de_estacionamiento = get_str_validado("Elija el nombre de un estacionamiento para agregar el vehiculo: ", 0, 10)
    estacionamiento_elegido = None

    for estacionamiento in lista_estacionamientos:
        if estacionamiento.get_nombre() == eleccion_de_estacionamiento:
            estacionamineto_valido = True
            estacionamiento_elegido = estacionamiento

    
    if estacionamineto_valido == True:
        nuevo_vehiculo = alta_vehiculo(eleccion_de_estacionamiento)
        if nuevo_vehiculo.get_tipo() == "Auto":
            estacionamiento_elegido.ingreso_auto(nuevo_vehiculo)

        elif nuevo_vehiculo.get_tipo() == "Moto":
            estacionamiento_elegido.ingreso_moto(nuevo_vehiculo)

        print(nuevo_vehiculo.get_tipo())
        print(nuevo_vehiculo.get_hora_ingreso())
        print("el estacionamiento elegido es: ")
        print(nuevo_vehiculo.get_estacionamiento_elegido())
        print("La cantidad de parcelas de autos son de: ")
        print(estacionamiento_elegido.get_cant_parcelas_autos())





def punto_3() -> bool:
    estacionamineto_valido = False
    #lista_estacionamientos = estacionamiento_leer(path_estacionamientos)
    mostrar_menu_estacionamientos(lista_estacionamientos)

    eleccion_de_estacionamiento = get_str_validado("Elija el nombre del estacionamiento para egresar un vehiculo: ", 0, 20)
    
    estacionamiento_elegido = None

    for estacionamiento in lista_estacionamientos:
        if estacionamiento.get_nombre() == eleccion_de_estacionamiento:
            estacionamineto_valido = True
            estacionamiento_elegido = estacionamiento


    if estacionamineto_valido == True:
        eleccion_patente_dar_de_baja = get_str_validado("Ingrese la patente para dar de baja: ", 0,6)

        lista_vehiculos = estacionamiento_elegido.get_lista_vehiculos()
        tipo_vehiculo_segun_patente = None

        for vehiculo in lista_vehiculos:
            if vehiculo.get_patente() == eleccion_patente_dar_de_baja:
                tipo_vehiculo_segun_patente = vehiculo.get_tipo()

        if tipo_vehiculo_segun_patente == 'Auto':
            for auto in estacionamiento_elegido.get_lista_de_autos():
                if auto.get_patente() == eleccion_patente_dar_de_baja:
                    estacionamiento_elegido.egreso_vehiculo_autos(auto)

        elif tipo_vehiculo_segun_patente == 'Moto':
            for moto in estacionamiento_elegido.get_lista_de_motos():
                if moto.get_patente() == eleccion_patente_dar_de_baja:
                    estacionamiento_elegido.egreso_vehiculo_motos(moto)




def punto_4() -> bool:
    eleccion_de_estacionamiento = get_str_validado("Ingrese el estacionamiento para modificar: ", 0,6)
    #lista_estacionamientos = estacionamiento_leer(path_estacionamientos)
    for estacionamiento in lista_estacionamientos:
        if (estacionamiento.get_nombre() == eleccion_de_estacionamiento):
            nuevo_coste_auto = get_float_rango("Ingrese el nuevo coste de auto: ", "ERROR, Ingrese dentro del rango", "ERROR, Ingrese flotante",0,99999)
            estacionamiento.set_coste_hora_auto(nuevo_coste_auto)
            nuevo_coste_moto = get_float_rango("Ingrese el nuevo coste de motos: ", "ERROR, Ingrese dentro del rango", "ERROR, Ingrese flotante",0,99999)
            estacionamiento.set_coste_hora_moto(nuevo_coste_moto)

def formatear_vehiculos(vehiculo):
    return str(vehiculo)

def punto_5() -> bool:
    #lista_estacionamientos = estacionamiento_leer(path_estacionamientos)
    #eleccion_de_estacionamiento = get_str_validado("Ingrese el estacionamiento para modificar: ", 0,6)
    i = 0 
    for estacionamiento in lista_estacionamientos:
        print(f"Estacionamiento {estacionamiento.get_nombre()}")
        vehiculos_estacionados = list(map(formatear_vehiculos, estacionamiento.get_lista_vehiculos()))
        
    print(vehiculos_estacionados)
    
    


def punto_6() -> bool:
    #lista_estacionamientos = estacionamiento_leer(path_estacionamientos)
    for estacionamiento in lista_estacionamientos:
        print(f"Estacionamiento {estacionamiento.get_nombre()}")

        vehiculos_ordenados_por_patente = sorted(estacionamiento.get_lista_vehiculos(), key=lambda vehiculo: vehiculo.get_patente(), reverse=True)
        
        patentes_ordenadas = list(map(formatear_vehiculos, vehiculos_ordenados_por_patente))

        print(patentes_ordenadas)

def punto_7() -> bool:
    #lista_estacionamientos = estacionamiento_leer(path_estacionamientos)
    #recaudacion_total = reduce(lambda total, estacionamiento: total + estacionamiento.get_recaudacion(), lista_estacionamientos, 0)
    for estacionamiento in lista_estacionamientos:
        print(estacionamiento.get_recaudacion())
    #print(f"Recaudación total de todos los estacionamientos: {recaudacion_total}")

def vehiculos_mas_de_60_minutos(lista_estacionamientos):
    for estacionamiento in lista_estacionamientos:
        print(filter(lambda vehiculo: (datetime.now() - vehiculo.get_hora_ingreso().total_seconds() > 3600), estacionamiento.get_lista_vehiculos()))

def punto_8() -> bool:

    vehiculos_mas_de_60_minutos(lista_estacionamientos)

def punto_9() -> bool:
    
    estacionamiento_guardar(path_estacionamientos)


def punto_10() -> bool:
    pass