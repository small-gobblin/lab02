def euclidean_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Пример использования
if __name__ == "__main__":
    num1 = int(input("Введите первое целое число: "))
    num2 = int(input("Введите второе целое число: "))
    gcd = euclidean_gcd(num1, num2)
    print(f"Наибольший общий делитель {num1} и {num2} равен {gcd}.")
