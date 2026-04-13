import random

def game():
    number = random.randint(1, 100)
    attempts = 0

    print("Я загадал число от 1 до 100.")

    while True:
        try:
            guess = int(input("Введи число: "))

            if guess < 1 or guess > 100:
                print("Число должно быть от 1 до 100!")
                continue

            attempts += 1

            if guess < number:
                print("Меньше чем нужно. Попробуй больше.")
            elif guess > number:
                print("Больше чем нужно. Попробуй меньше.")
            else:
                print(f"Ты выиграл! Количество попыток: {attempts}")
                break

        except:
            print("Ошибка! Нужно ввести число.")

def main():
    while True:
        print("===== МЕНЮ =====")
        print("1 — Играть")
        print("2 — Выход")

        choice = input("Выбери действие: ")

        if choice == "1":
            game()
        elif choice == "2":
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор.")

main()
