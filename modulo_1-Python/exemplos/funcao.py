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

imprime()
print(variavel_local)


