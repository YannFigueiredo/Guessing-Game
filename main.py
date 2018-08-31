from random import randint
from time import sleep
print('\033[1;33m-=-\033[m'*30)
print('\t\t\t\t\033[1;37;42mJOGO DE ADIVINHAÇÃO')
print('\033[m\033[1;33m-=-\033[m'*30)
player = str(input('Informe o nome do jogador: ')).strip().title()
print('\033[1;33m-=-\033[m'*30)
print('Bem-Vindo, {}.'.format(player))
print('\033[1;33m-=-\033[m'*30)
num = int(input('Informe um número de 0 a 10: '))
numE = randint(0, 10)
print('\033[1;33m-=-\033[m'*30)
print('Analisando resposta...')
sleep(2)
print('\033[1;33m-=-\033[m'*30)
print('\nO número escolhido pelo computador foi \033[1;35m{}\033[m.'.format(numE))
if num == numE:
  print('\033[1;32m\nVOCÊ VENCEU!!!\033[m')
else:
  print('\033[1;31m\nVOCÊ PERDEU!!!\033[m')