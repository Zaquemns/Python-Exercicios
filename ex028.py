import random

n = [0, 1, 2, 3, 4, 5]
npc = random.choice(n)
nc = int(input('Pensei em um número de 0 a 5. Adivinhe que número eu escolhi: '))
print(f'Escolhi o número {npc}.')
if nc == npc:
    print(f'PARABÉNS, VOCÊ VENCEU!')
else:
    print(f'VOCÊ PERDEU, FIM DE JOGO!')
