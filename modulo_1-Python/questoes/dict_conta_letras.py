entrada = input("Digite uma entrada: ")

qtd_lida = {}

for caractere in entrada.replace(" ", ""):
    if caractere not in qtd_lida:
        qtd_lida[caractere] = 0
    qtd_lida[caractere] += 1

print(qtd_lida)
