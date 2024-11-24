from Veiculo import Veiculo
from Frete import Frete
from constantes import *

def calcular_frete(origem, destino, distancia, modelo, capacidade):
    veiculo = Veiculo(modelo, 7400, "ABC-1234", 5.4, capacidade)
    frete = Frete(origem, destino, distancia, veiculo, "Empresa Compartilhada", "Mobilia", gas)

    # Simulação do caso compartilhado
    frete.adicionar_carga("Empresa A", 3040, "Mobilia")
    frete.adicionar_carga("Empresa B", 4320, "Mobilia")
    
    # Calcula a pegada de CO₂ para o cenário compartilhado
    compartilhado_emissao = frete.pegada_co2(emissao_disel) 

    # Retorna a pegada de CO₂ calculada
    return compartilhado_emissao
