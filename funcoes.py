from random import randint
from time import sleep

player = str(input('Informe o nome do jogador: ')).strip().title()
num = int(input('Informe um número de 0 a 10: '))
numE = randint(0, 10)
print('Analisando resposta...')
sleep(2)
print(f'\nO número escolhido pelo computador foi \033[1;35m{numE}\033[m.')
if num == numE:
  print('\033[1;32m\nVOCÊ VENCEU!!!\033[m')
else:
  print('\033[1;31m\nVOCÊ PERDEU!!!\033[m')