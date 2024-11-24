from tabulate import tabulate
import uuid

class Frete:
    def __init__(self, origem, destino, distancia, veiculo, empresa_fornecedora_veiculo, tipo, gas, valor):
        self.id = str(uuid.uuid4())
        self.origem = origem
        self.destino = destino
        self.distancia = distancia
        self.veiculo = veiculo
        self.empresa_fornecedora_veiculo = empresa_fornecedora_veiculo  # A empresa fornecedora do veículo
        self.gas = gas  # Preço do combustível
        self.cargas = {}
        self.valores = {}
        self.tipo = tipo
        self.consumo = 0

    def carga_disponivel(self):
        return self.veiculo.capacidadeCarga - sum(self.cargas.values())

    def calcular_valor(self, peso):
        return self.consumo * self.gas * (peso / self.veiculo.capacidadeCarga)

    def adicionar_carga(self, empresa, peso, tipo):
        if tipo == self.tipo:
            if peso <= self.carga_disponivel():
                if empresa not in self.cargas:
                    self.cargas[empresa] = 0
                    self.valores[empresa] = 0
                self.cargas[empresa] += peso
                self.consumo = (self.distancia/self.veiculo.rendimento) * (1+((sum(self.cargas.values())/self.veiculo.peso)))
                self.distribuicao()
            else:
                print("Erro: Peso excede a capacidade disponível.")
        else:
            print("Carga não Permitida")
        
        
    def pegada_co2(self, emissao_media):
        emissao_total = self.consumo * emissao_media
        return emissao_total
        
    def distribuicao(self):
        peso = sum(self.cargas.values())  
        valor = self.consumo * self.gas  
        resto = (self.veiculo.capacidadeCarga - peso) / self.veiculo.capacidadeCarga   
        total = sum(self.cargas[empresa] for empresa in self.valores if self.cargas[empresa] > 0)
        for empresa in self.valores:
            if self.cargas[empresa] > 0:  
                parte = self.cargas[empresa] / total  
                redistribuida = (parte * resto / peso) * valor  
                proporcao = parte * valor + redistribuida 
                self.valores[empresa] = proporcao
            else:
                self.valores[empresa] = 0 


    def detalhes(self):
        print (f"A Viagem de {self.origem} ate {self.destino} ({self.distancia} km), sera feita pelo veiculo de placa {self.veiculo.placa} e tera custo total de R${(self.consumo * self.gas):.2f}")

    def __str__(self):
        dados = []
        for empresa in self.cargas:
            peso = self.cargas[empresa]
            valor = self.valores[empresa]
            porcentagem = (peso/self.veiculo.capacidadeCarga) * 100
            dados.append([empresa, peso, f"R$ {valor:.2f}", f"{porcentagem:.2f}%"])
        
        print(tabulate(dados, headers=["Empresa", "Peso (kg)", "Valor (R$)","Porcentagem"], tablefmt="pretty"))
        return ""