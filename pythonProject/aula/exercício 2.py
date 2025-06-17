def soma(numero1, numero2):
    return numero1 + numero2

def subtracao(numero1, numero2):
    return numero1 - numero2

def multiplicacao(numero1, numero2):
    return numero1 * numero2

def divisao(numero1, numero2):
    return numero1 // numero2

numero1 = int(input("Digite um numero inteiro"))
numero2 = int(input("Digite um numero inteiro"))

resultadoSoma = soma(numero1, numero2)
resultadoSubtracao = subtracao(numero1, numero2)
resultadoMultiplicacao = multiplicacao(numero1, numero2)
resultadoDivisao = divisao(numero1, numero2)

print("o resultado de uma funcao Soma", resultadoSoma)
print("o resultado de uma funcao Subtracao", resultadoSubtracao)
print("o resultado de uma funcao Multiplicacao", resultadoMultiplicacao)
print("o resultado de uma funcao Divisao", resultadoDivisao)
