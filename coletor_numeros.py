matriz = []

while True:
    digitado = input('Digite um número: ')
    if digitado.isdigit():
        matriz.append(int(digitado))
        break
    else:
        print('Digite um número válido, por favor!')

while len(matriz) < 10:
    digitado = input('Digite um outro numero para salvar: ')
    if digitado.isdigit():
        matriz.append(int(digitado))
    else:
        print('Digite um numero caceta')

print('Esses foram os números digitados:', matriz)
