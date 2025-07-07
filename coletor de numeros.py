
matriz = []

while True:
    digitado = input('Digite um número: ')
    if digitado.isdigit():
        matriz.append(int(digitado))
        break
    else:
        print('Digite um número válido, por favor!')

while len(matriz) < 10:
    digitado = input('Digite um outro numero para salvar:')
    if digitado.isdigit():
        matriz.append(digitado)
    else:
        print('Digite um numero valido, por favor!')


print('Esses foram os numeros digitados:', matriz)