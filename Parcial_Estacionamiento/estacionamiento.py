from datetime import datetime

class Estacionamiento:
    
    autos = []
    motos = []
    lista_vehiculos = []

    recaudacion = 0

    def __init__(self, nombre: str, cant_parcelas_autos: int, cant_parcelas_motos: int, coste_hora_auto: float, coste_hora_moto: float) -> None:
        # Constructor de clase.
        self.nombre = nombre
        self.cant_parcelas_autos = cant_parcelas_autos
        self.cant_parcelas_motos = cant_parcelas_motos
        self.coste_hora_auto = coste_hora_auto
        self.coste_hora_moto = coste_hora_moto

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, value):
        self.nombre = value

    def get_cant_parcelas_autos(self):
        return self.cant_parcelas_autos

    def set_cant_parcelas_autos(self, value):
        self.cant_parcelas_autos = value

    def get_cant_parcelas_motos(self):
        return self.cant_parcelas_motos

    def set_cant_parcelas_motos(self, value):
        self.cant_parcelas_motos = value

    def get_coste_hora_auto(self):
        return self.coste_hora_auto

    def set_coste_hora_auto(self, value):
        self.coste_hora_auto = value

    def get_coste_hora_moto(self):
        return self.coste_hora_moto

    def set_coste_hora_moto(self, value):
        self.coste_hora_moto = value
    
    def get_lista_de_autos(self):
        return self.autos

    def get_lista_de_motos(self):
        return self.motos
    
    def get_lista_vehiculos(self):
        return self.lista_vehiculos

    def ingreso_auto(self, auto):
        self.autos.append(auto)
        self.cant_parcelas_autos -= 1
        self.lista_vehiculos.append(auto)
    
    def ingreso_moto(self, moto):
        self.motos.append(moto)
        self.cant_parcelas_motos -= 1
        self.lista_vehiculos.append(moto)

    def egreso_vehiculo_autos(self, vehiculo):
        self.autos.remove(vehiculo)
        self.cant_parcelas_autos += 1
        hora_egreso = datetime.now()
        tiempo_estacionado_horas = (hora_egreso - vehiculo.get_hora_ingreso()).total_seconds() / 3600

        coste_calculado = tiempo_estacionado_horas * self.get_coste_hora_auto()

        self.recaudacion += coste_calculado

        print("El coste del vehiculo que egreso es de: ")
        print(round(coste_calculado))

    def egreso_vehiculo_motos(self, vehiculo):
        self.motos.remove(vehiculo)
        self.cant_parcelas_motos += 1
        hora_egreso = datetime.now()
        tiempo_estacionado_horas = (hora_egreso - vehiculo.get_hora_ingreso()).total_seconds() / 3600

        coste_calculado = tiempo_estacionado_horas * self.get_coste_hora_moto()

        self.recaudacion += coste_calculado
    
    def get_recaudacion(self):
        return self.recaudacion




    def convertir_obj_a_json(self):
        return{
            "nombre": self.nombre,
            "cant_parcelas_autos": self.cant_parcelas_autos,
            "cant_parcelas_motos": self.cant_parcelas_motos,
            "coste_hora_auto": self.coste_hora_auto,
            "coste_hora_moto": self.coste_hora_moto
        }


    
    
    def __str__(self) -> str:
        # Mostrara toda la informacion del estacionamiento. [CANT MOTOS] [CANT AUTOS] [RECAUDACION DEL DIA]
        return f"Nombre: {self.nombre}, Cantidad de parcelas autos: {self.cant_parcelas_autos},Cantidad de parcelas motos: {self.cant_parcelas_motos}, Recaudacion:  "
    def __len__(self) -> int:
        # Devuelve la recaudacion con el formato float, con dos numero despues de la coma.
        pass

#estacionamiento_1 = Estacionamiento("EST1", 10, 10, 1500.45, 800.50)


