#importando a biblioteca.
import json
# Função para processar os dados de faturamento
def faturamento(dado):
    #pegando os valores de faturamento e ignorando os dias em que o valor foi 0
    valores = [dia["valor"] for dia in dado if dia["valor"] > 0]
    
    #caso não tenha valores
    if not valores:
        return "Não há faturamento."

    #menor valor
    menorf = min(valores)
    
    #maior valor
    maiorf = max(valores)
    
    #tirando a média do faturamento mensal
    mediaf = sum(valores) / len(valores)
    
    #dias com faturamento acima da média
    acima = len([valor for valor in valores if valor > mediaf])
    
    #recebendo os resultados
    return {
        "menorf": menorf,
        "maiorf": maiorf,
        "acima": acima
    }

#usando json fornecido
with open('dados.json', encoding="utf-8") as file:
    dados = json.load(file)

#executando a função
resultado = faturamento(dados["diario"])
#mostrando na tela os resultados
print(f"Menor valor de faturamento: {resultado["menorf"]}")
print(f"Maior valor de faturamento: {resultado["maiorf"]}")
print(f"Dias em que o faturamento foi acima da média: {resultado["acima"]}")


