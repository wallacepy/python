n1 = int(input('Digite um numero: '))
op = input('Digite um operador ( +, -, x, / ): ')
n2 = int(input('Digite outro numero: '))

if op == '+':
    print(f'A soma de {n1} + {n2} é {n1 + n2}')
elif op == '-':
    print(f'A subtração de {n1} - {n2} é {n1 - n2}')
elif op == 'x':
    print(f'A multiplicação de {n1} x {n2} é {n1 * n2}')
else:
    print(f'A divisão de {n1} / {n2} é {n1 / n2}')