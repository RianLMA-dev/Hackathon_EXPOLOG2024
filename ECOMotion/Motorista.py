import uuid 

class Motorista:
    def _init_(self, nome, email, telefone, veiculo, empresa=None):
        self.id =  str(uuid.uuid4())  
        self.nome = nome  
        self.email = email  
        self.telefone = telefone  
        self.veiculo = veiculo  
        self.empresa = empresa

    def exibir_dados(self):
        print("\n=== Dados do Motorista ===")
        print(f"ID: {self.id}")
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"Telefone: {self.telefone}")
        print(f"Veículo: {self.veiculo}")

    def atualizar_veiculo(self, novo_veiculo):
        self.veiculo = novo_veiculo
        print("\nInformações do veículo atualizadas com sucesso!")
