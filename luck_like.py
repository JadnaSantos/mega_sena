from random import randint
from time import sleep

lista = list()
play = list()
print('-' * 30)
print('           Play           ')
print('-' * 30)

quant = int(input('How many games do you want me to draw?'))
changes =  1
while changes <= quant:
    cont = 0
    while True:
        number = randint(1, 60)
        if number not in lista:
            lista.append(number)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    play.append(lista[:])
    lista.clear()
    changes += 1

print('-=' * 3, f'Draw {quant} Play', '-=' * 3)
for i, l in enumerate(play):
    print(f'Play {i+1}: {l}')
    sleep(1)
print('-=' * 5, '<GOOD LUCK!', '-=' * 5)

