def quadrado(n):
    return n**2

quadrado(2) # 4
quadrado(3) # 9



def chave(dicionario, valor):
    for chave, elemento in dicionario.items():
        if elemento == valor:
            return chave
    
    return None

pontuacao = {
    "mateus": 4,
    "berg": 5,
    "edilene": 10
}

chave(pontuacao, 4)  # mateus
chave(pontuacao, 10) # edilene
chave(pontuacao, 11) # None



VARIAVEL_GLOBAL = "global"

def imprime():
    print("Variavel global: ", VARIAVEL_GLOBAL)


def imprime():
    variavel_local = "local"
    print("Variavel local: ", variavel_local)

# imprime()
# print(variavel_local)


def soma(a, b, imprime=False):
    resultado = a + b
    if imprime:
        print(resultado)
    return resultado


soma(3, 5)
# soma(3, 5, imprime=True)


def computacao_assincrona(param1, param2, callbackFn):
    try:
        print("Fazendo uma computaçao assincrona bem complicada.....")
    except:
        print("Algo de errado aconteceu")
        return None

    return callbackFn(param1, param2)

def callback(a, b):
    return a + b

print(computacao_assincrona(2, 4, callback))


def multiplicacao(a, b):
    return a*b

argumentos = [4, 5]
multiplicacao(*argumentos)



def multiplicacao(*args):
    acumulador = 1
    for arg in args:
        acumulador *= arg

    return acumulador

def fatorial(n):
    return multiplicacao(*range(1, n))

print(fatorial(6)) # 120

multiplicacao(2, 3)
multiplicacao(2, 3, 4, 5)





