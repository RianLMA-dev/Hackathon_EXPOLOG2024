import uuid

class Veiculo:
    def _init_(self, tipo, capacidadeCarga, placa):
        self.id =  str(uuid.uuid4())
        self.tipo = tipo
        self.capacidadeCarga = capacidadeCarga
        self.placa = placa

    def atualizarDetalhes(self, tipo=None, capacidadeCarga=None, placa=None):
        """Permite a atualização dos detalhes do veículo."""
        if tipo:
            self.tipo = tipo
        if capacidadeCarga:
            self.capacidadeCarga = capacidadeCarga
        if placa:
            self.placa = placa
        print("Detalhes atualizados com sucesso!")
    
    def _str_(self):
        return (f"Veículo ID: {self.id}, Tipo: {self.tipo}, "
                f"Capacidade de Carga: {self.capacidadeCarga}kg, Placa: {self.placa}")