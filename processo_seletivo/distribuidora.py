#criando dicionário chave e valor para os faturamentos e seus respectivos estados
faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}
#calculando faturamento total
total = sum(faturamento_estados.values())
#calculando porcentagem de cada estado
porcentagem = {estado: (valor / total) * 100 for estado, valor in faturamento_estados.items()}

#exibindo o resultado
#para cada percentual das porcentagens
for estado, percentual in porcentagem.items():
    #mostre na tela o estado e seu respectivo percentual (com formatação 2 casas pós vírgula)
    print(f"{estado}: {percentual:.2f}%")
