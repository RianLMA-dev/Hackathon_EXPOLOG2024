from Veiculo import Veiculo
from Frete import Frete
from constantes import *

def compartilhado():
    
    veiculo = Veiculo("Volkswagen Delivery 11.180", 7500, "PMO-7008", 5.4, 10800)

    frete = Frete("Juazeiro-do-Norte", "Russas", 364.8, veiculo, "CMOtion","Mobilia", gas)

    print("-------------------------CASO COMPARTILHADO-------------------------")
    print("Sem parceria")
    print(frete)
    frete.detalhes()
    print(f"Durante essa viagem, foram liberados {frete.pegada_co2(emissao_disel):.2f} kg de CO2 na Atmosfera")

    frete.adicionar_carga("Empresa A", 3000,"Mobilia")
    print("")
    print("Com 1 Parceria")
    print(frete)
    frete.detalhes()
    print(f"Durante essa viagem, foram liberados {frete.pegada_co2(emissao_disel):.2f} kg de CO2 na Atmosfera")

    pegada = frete.pegada_co2(emissao_disel)

    print("No Total:")
    frete.detalhes()
    frete.pegada_co2(emissao_disel)
    print()
    return pegada

def individual():
    veiculo1 = Veiculo("Volkswagen Delivery 11.180", 7500, "PMO-7008", 5.4, 10800)
    veiculo2 = Veiculo("Volkswagen Delivery 11.180", 7500, "CPX-2315", 5.4, 10800)

    frete1 = Frete("Juazeiro-do-Norte", "Russas", 364.8, veiculo1, 3200, "CMOtion","Mobilia", gas)
    frete2 = Frete("Juazeiro-do-Norte", "Russas", 364.8, veiculo2, 3000, "Empresa A","Mobilia", gas)
 
    pegada = frete1.pegada_co2(emissao_disel)+frete2.pegada_co2(emissao_disel)

    print("-------------------------CASO INDIVIDUAL-------------------------")
    print("CMOtion:")
    print(frete1)
    frete1.detalhes()
    frete1.economia()
    print(f"Durante essa viagem, foram liberados {frete1.pegada_co2(emissao_disel):.2f} kg de CO2 na Atmosfera")
    print()

    print("Empresa A:")
    print(frete2)
    frete2.detalhes()
    frete2.economia()
    print(f"Durante essa viagem, foram liberados {frete2.pegada_co2(emissao_disel):.2f} kg de CO2 na Atmosfera")
    print()

    print(f"Ao todo, as tres empresas liberaram {pegada:.2f} kg de CO2 na Atmosfera")
    return pegada

comp = compartilhado()
#ind = individual()

#print(f"Em comparação, a nossa solução reduziu em {((ind-comp)/ind)*100:.2f}% a emissão de CO2 na Atmosfera")