nome = input('Digite seu nome:\n')
idade = input('Digite sua idade:\n')

if nome != '' or idade != '':
    inv = nome[::-1]
    nustr = len(nome)

    print(f'Seu nome é {nome}!')
    print(f'Seu nome invertido é {inv}')

    if ' ' in nome:
        print('Seu nome contem espaço!')
    else:
        print('Seu nome não contem espaço!')

    print(f'Seu nome tem {nustr} letras!')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    print('Voçê não digitou nada!')