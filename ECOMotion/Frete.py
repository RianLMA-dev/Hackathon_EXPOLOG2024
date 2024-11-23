import uuid
from Empresa import Empresa

class Frete:
    def __init__(self, origem, destino, carga_max, peso, motorista = None):
        self.id = str(uuid.uuid4())  # ID único do frete
        self.origem = origem
        self.destino = destino
        self.carga_max = carga_max
        self.peso = peso
        self.cargas = []
        self.motorista = motorista

    def carga_disponivel(self):
        return self.carga_max - self.peso
    
    def adcionar_carga(self, empresa, peso):
        if peso <= self.carga_disponivel():
            if empresa not in self.cargas:
                self.cargas[empresa] = 0
            self.cargas[empresa] += peso

    def __str__(self):
        motorista_info = f"Motorista: {self.motorista.nome}" if self.motorista else "Motorista: Não atribuído"
        return (f"ID: {self.id}, Origem: {self.origem}, Destino: {self.destino}, "
                f"Peso: {self.peso}kg, {motorista_info}")
    
