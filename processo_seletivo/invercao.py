#criando a função para inversao da stringg
def inversao(x):
    #crindo uma string vazia para atribuir a string invertida depois
    invertida = ""
    
    #usando um loop de for para passar por todas as letras da string de trás pra frente
    for i in range(len(x) - 1, -1, -1):
        #atribuindo os valores de trás pra frente ao espaço vazio
        invertida += x[i]
    
    return invertida

#input para o usuário pedir a string
palavra = input("Digite uma palavra para inverter: ")

#executando a função e aprensentando na tela
string_invertida = inversao(palavra)
print("String invertida:", string_invertida)

#funciona pra qualquer string, seja palavra ou frase