import random

n = random.randint(1, 30)
chance = 0

# A while loop that will run until the condition is met.
while chance <= 5:

    chance += 1
    print(f'\nSua {chance}ª tentativa\n')

    x = int(input('Descubra o numero de 1 a 30: '))

    if x == n:
        print(f'Parabens voce acertou o numero: {x}\n')
        break

    if x > n:
        print(f'Chute um numero menor\n')

    if x < n:
        print('Chute um numero maior\n')

    if chance == 5:
        print(f'Numero correto: {n}')
        break
