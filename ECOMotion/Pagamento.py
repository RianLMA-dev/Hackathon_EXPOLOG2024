import uuid

class Pagamento:
    def _init_(self, valor, metodoPagamento, status="pendente"):
        self.id = str(uuid.uuid4())
        self.valor = valor
        self.metodoPagamento = metodoPagamento
        self.status = status

    def realizarPagamento(self):
        if self.status == "pendente":
            self.status = "concluído"
            print("Pagamento realizado com sucesso!")
        else:
            print("Pagamento já foi concluído anteriormente.")

    def dividirCusto(self, carga):
        if carga.get("peso") and carga.get("volume"):
            peso = carga["peso"]
            volume = carga["volume"]
            custoPorUnidade = self.valor / (peso + volume)
            return {
                "custoPorPeso": peso * custoPorUnidade,
                "custoPorVolume": volume * custoPorUnidade
            }
        else:
            print("Informações de peso e volume da carga são necessárias.")
            return None

    def _str_(self):
        return (f"Pagamento ID: {self.id}, Valor: R${self.valor:.2f}, "
                f"Método: {self.metodoPagamento}, Status: {self.status}")