import os

VALOR_OK = 0
CAD_NO_VALIDA = -1
CAD_FUERA_DE_RANGO = -2


def get_int(msj:str, msj_error: str, min: int, max: int, reintentos: int | None = None) -> int | None:
    
    while reintentos is None or reintentos > 0 or reintentos == -1:
        aux = int(input(msj))
        if aux.is_integer() == True:
            if (aux >= min and aux <= max):
                return aux
            else:
                match(reintentos):
                    case None:
                        break;
                    case -1:
                        print(msj_error)
                    case _:
                        print(msj_error)
                        reintentos -= 1
        elif aux.is_integer() == False:
            return msj_error
        
    return None

def get_float(msj:str, msj_error: str, min: float, max: float, reintentos: int | None = None) -> float | None:
    
    while reintentos is None or reintentos > 0:
        aux = float(input(msj))
        if (aux >= min and aux <= max):
            return aux
        else:
            match(reintentos):
                case None:
                    break;
                case -1:
                    print(msj_error)
                case _:
                    print(msj_error)
                    reintentos -= 1
    return None

def menu(titulo: str, opc: list, mostrar_tema: str) -> int:
    i = 0
    print(f'[{titulo}]\n')
    while i < len(opc):
        print(f'[{i+1}] {opc[i]}')
        i += 1
    print(f'\n[0] Salir y mostrar {mostrar_tema}')

    return get_int_rango("Opcion: ","ERROR, Ingrese un numero entre 0 y 10", "ERROR, inserte un numero", 0, 10)

def create_list_range_int(len: int, min: int, max: int, msj: str) -> list:
    aux_list = []

    for i in range(len):
        aux = get_int(f'{msj} {i+1}: ', '[ERROR]', min, max, -1)
        aux_list.append(aux)

    return aux_list

def count_pos(lista: list) -> int:
    contador_pos = 0

    for numero in lista:
        if numero > -1:
            contador_pos += 1 

    return contador_pos

def count_neg(lista: list) -> int:
    contador_neg = 0

    for numero in lista:
        if numero < 0:
            contador_neg += 1 

    return contador_neg

def sum_pares_int(lista: list) -> int:
    acumulador_pares = 0

    for numero in lista:
        if numero % 2 == 0:
            acumulador_pares += numero

    return acumulador_pares

def validar_impar_int(num) -> bool:
    return True if num % 2 == 1 else False

def get_max_impar_int(lista: list) -> int | None:
    mayor_impar = None
    flag_primer_impar = True

    indice = 0
    while indice < len(lista):
        if(lista[indice] % 2 == 1):
            #impar
            if flag_primer_impar:
                mayor_impar = lista[indice]
                flag_primer_impar = False
            else:
                if lista[indice] > mayor_impar:
                    mayor_impar = lista[indice]

        indice += 1

    return mayor_impar



def get_int_rango(msj,msj_rango , msj_error, min, max):
    while True:  
        try:
            entero = int(input(msj))
            if entero >= min and entero <= max:
                break
            else:
                print(msj_rango)
        except ValueError:
            print(msj_error)

    return entero



def validar_str(texto):
    return texto.isalpha()


def get_str_validado(msj:str, min:int, max:int):
    while True:
        texto = input(msj)
        if validar_str(texto):
            if len(texto) >= min and len(texto) <= max:
                return texto
            else:
                print("Ingrese dentro del rango")
        else:
            print("ERROR, ingrese solamente letras")
    


def get_float_rango(msj,msj_rango , msj_error, min, max):
    while True:  
        try:
            flotante = float(input(msj))
            if flotante >= min and flotante <= max:
                break
            else:
                print(msj_rango)
        except ValueError:
            print(msj_error)

    return flotante



def mostrar_menu_estacionamientos(estacionamientos):
    print("Menú de Estacionamientos:")
    for i, estacionamiento in enumerate(estacionamientos, start=1):
        print(f"{i}. {estacionamiento.get_nombre()}")







