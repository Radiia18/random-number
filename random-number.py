import random
n = (random.randint(1,100))
k = int(input())
while k!=n:
    print('Попробуй снова.')
    if k<n:
        print(k, 'меньше чем загаданное число. Попробуйте число больше.')
    elif k>n:
        print(k, 'больше чем загаданное число. Попробуйте число меньше.')
    k = int(input())
print('Ты выиграл! Молодец!')