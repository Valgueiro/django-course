# calculadora.py
import operacoes

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
op = input("Digite uma operação: ")

resultado = None
if op == '+':
    resultado = operacoes.soma(a, b)
elif op == "/":
    resultado = operacoes.divide(a, b)

print(f"{a}{op}{b} = {resultado}")


