from random import randint
contador = 0

computador = randint(1, 10)
print('Pense em um numero de 1 a 10 ')
adivinha = False

while not adivinha :
    jogador = int(input('Qual seu palpite? :'))
    contador += 1
    if jogador == computador:
        adivinha = True
    else:
        if jogador > computador:
            print('É menos... tente denovo')
        elif jogador < computador:
            print('É mais... tente denovo')
print('Parabens você acertou com {} tentativas'.format(contador))