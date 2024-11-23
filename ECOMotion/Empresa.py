import uuid 
from Frete import Frete

class Empresa:
    def __init__(self, nome, email, senha):
        self.id = str(uuid.uuid4()) 
        self.nome = nome
        self.email = email
        self.senha = senha
        self.fretes = [] 

    def publicar_frete(self, origem, destino, peso, motorista):
        viagem = Frete(origem, destino, peso, motorista = motorista)
        self.fretes.append(viagem)
        print(f"Frete publicado com sucesso! Detalhes: {viagem}")
        return viagem

    def visualizar_fretes(self):
        if not self.fretes:
            print("Nenhum frete publicado.")
        else:
            print("Fretes publicados:")
            for frete in self.fretes:
                print(f"  - {frete}")

    def rastrear_carga(self, carga_id):
        print(f"Rastreando a carga com ID {carga_id}... Status: Em trânsito.")
