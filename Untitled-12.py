primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite o segundo valor: ')

if primeiro_valor > segundo_valor:
    print(f'O valor {primeiro_valor} é maior que {segundo_valor}!')
elif primeiro_valor < segundo_valor:
    print(f'O valor {segundo_valor} é maior que {primeiro_valor}!')
else:
    print('Os valores são iguais!')