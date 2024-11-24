import uuid

class Veiculo:
    def __init__(self, tipo, capacidadeCarga, placa, rendimento, peso):
        self.id = str(uuid.uuid4())
        self.tipo = tipo
        self.capacidadeCarga = capacidadeCarga
        self.placa = placa
        self.rendimento = rendimento
        self.peso = peso

    def __str__(self):
        return (f"Veículo ID: {self.id}, Tipo: {self.tipo}, "
                f"Capacidade de Carga: {self.capacidadeCarga}kg, Placa: {self.placa}")
