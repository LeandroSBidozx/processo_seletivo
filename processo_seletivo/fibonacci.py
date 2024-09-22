#input para o número de teste.
num = int(input("Digite um número: "))

#criação da função para testar o número,
def fibonacci(x):
    #variáveis f1 e f2 como controle da sequência (f1 contém o penúltimo valor para a contagem da sequência e f2 contém o valor do estágio atual).
    f1, f2 = 0, 1
    #se for 0 ou 1, por regra pertence à sequência de fibonacci
    if x == 0 or x == 1:
        return f"{x} está na sequência de Fibonacci."
    #enquanto f2 for menor que o número que queremos testar(x).
    while f2 < x:
        #f1 aribui a si o valor de f2 e f2 atribui a si o valor de f1 + f2 (isso é necessário para a sequência continuar em loop)
        f1, f2 = f2, f1 + f2
    if f2 == x:
        #se f2 em algum momento se tornar x (parte do cálculo para a sequência e consequentemente uma parte da sequência).
        return f"{x} está na sequência de Fibonacci."
    else:
        #se em nenhum momento o número de teste se tornar o f2, ele não faz parte da sequência.
        return f"{x} não está na sequência de Fibonacci."
#executa a função para a variável "num" e mostra o resultado na tela. 
print(fibonacci(num))
