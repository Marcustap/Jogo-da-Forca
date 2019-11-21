secreto = 'melancia'
letra = []
chances = 3

while True:
    letra_digitada = input('Digite uma letra ')

    if len(letra_digitada) > 1:
        print('Por favor, digite apenas uma letra!!')
        continue

    letra.append(letra_digitada)

    if letra_digitada not in secreto:
        chances -= 1
        letra.pop()
        print(f'Putz, a letra "{letra_digitada}" não existe na palavra secreta. Você ainda tem {chances} chances')
    else:
        print(f'Muito bem! a letra "{letra_digitada}" existe na palavra secreta. Você ainda tem {chances} chances')

    palavra_secreta = ''

    for letra_secreta in secreto:
        if letra_secreta not in letra:
            palavra_secreta += '*'
        else:
            palavra_secreta += letra_secreta

    print(f'A palavra secreta está assim')
    print(palavra_secreta)
    print()

    if palavra_secreta == secreto:
        print('Impressionante! Você ganhou!!!')
        break

    if chances == 0:
        print(f'Que pena, suas chances acabaram! A palavra secreta era "{secreto}"')
        break

