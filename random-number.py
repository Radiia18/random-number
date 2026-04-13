import random

def game():
    number = random.randint(1, 100)
    

    print("Я загадал число от 1 до 100.")

    while True:
        try:
            guess = int(input("Введи число: "))
            

            if guess < number:
                print("Меньше чем нужно. Попробуй больше.")
            elif guess > number:
                print("Больше чем нужно. Попробуй меньше.")
            else:
                print("Ты выиграл!")
                break

        except:
            print("Ошибка! Нужно ввести число.")

