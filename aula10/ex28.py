from random import randint
from time import  sleep

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

target = randint(0, 5)
shot = int(input('- Seu palpite: '))

print('Processando...')
sleep(2)

if target == shot:
    print('Parabéns! Você venceu!')
else:
    print('Você perdeu! O número era {}'.format(target))

