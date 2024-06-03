from datetime import datetime

class Vehiculo:
    hora_ingreso = datetime.now()
    estacionamiento_elegido = ""
    def __init__(self, tipo: str, patente: str) -> None:
        # Constructor de clase.
        self.tipo = tipo
        self.patente = patente


    def get_tipo(self):
        return self.tipo

    def set_tipo(self, value):
        self.tipo = value

    def get_patente(self):
        return self.patente

    def set_patente(self, value):
        self.patente = value

    def get_hora_ingreso(self):
        return self.hora_ingreso
    
    def set_estacionamiento_elegido(self, value):
        self.estacionamiento_elegido = value
    
    def get_estacionamiento_elegido(self):
        return self.estacionamiento_elegido

    def __str__(self) -> str:
        # Devuelve la patente.
        return f'Tipo: {self.tipo}, Patente: {self.patente}'
    def __len__(self) -> int:
        # Devuelve la cantidad de minutos de diferencia entre hora_ingreso y hora_actual.
        pass
