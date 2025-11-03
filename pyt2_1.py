import math

# 1. Функція для обчислення математичного виразу
def calculate_z(x):

    if x == 0:
        raise ValueError("Аргумент x не може дорівнювати нулю, оскільки це призведе до ділення на нуль (1/x).")

    try:
        # Використання вбудованих функцій: math.sqrt() та math.sin()
        z = (math.sqrt(2) / 2) * math.sin(1 / x) + 1
        return z
    except Exception as e:
        print(f"Виникла помилка при обчисленні: {e}")
        return None

# 2. Функція для перевірки, чи є число недостатнім
def is_deficient_number(n):

    if not isinstance(n, int) or n <= 0:
        return f"Введене значення {n} не є натуральним числом."

    # Власні дільники - це всі дільники, окрім самого числа n.
    # Найменший власний дільник завжди 1.
    proper_divisor_sum = 1 # Починаємо з 1, оскільки 1 завжди є власним дільником для n > 1

    # Перевіряємо дільники від 2 до кореня з n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            # Якщо i є дільником, то n // i також є дільником
            proper_divisor_sum += i
            # Додаємо n // i тільки якщо це не i (для ідеальних квадратів)
            if i * i != n:
                proper_divisor_sum += (n // i)

    # Порівнюємо суму власних дільників із самим числом
    return proper_divisor_sum < n

# --- БЛОК ВИКОНАННЯ ПРОГРАМИ ---

print("=== Функція 1: Обчислення виразу z ===")
# Цикл для коректного введення x
while True:
    try:
        # Введення даних користувачем
        x_input = input("Будь ласка, введіть число x для обчислення z = (sqrt(2)/2) * sin(1/x) + 1: ")
        x_val = float(x_input.replace(',', '.')) # Дозволяємо ввід з комою або крапкою

        # Виклик функції
        result_z = calculate_z(x_val)

        if result_z is not None:
            print(f"При x = {x_val}, значення z = {result_z}")
        break # Виходимо з циклу, якщо обчислення успішне

    except ValueError as ve:
        if "could not convert string to float" in str(ve):
             print("Помилка: Невірний формат вводу. Будь ласка, введіть коректне число (наприклад, 0.5 або 10).")
        else:
            print(f"Помилка: {ve}")

print("\n=== Функція 2: Перевірка недостатнього числа ===")
# Цикл для коректного введення n
while True:
    try:
        n_input = input("Будь ласка, введіть натуральне число n для перевірки, чи воно є недостатнім: ")
        n_val = int(n_input)

        # Виклик функції
        result_deficient = is_deficient_number(n_val)

        if result_deficient is True:
            print(f"Число {n_val} є **недостатнім** числом.")
        elif result_deficient is False:
            print(f"Число {n_val} **не є** недостатнім числом (воно або досконале, або надлишкове).")
        else:
            print(f"Результат перевірки: {result_deficient}") # Для випадку, коли n не є натуральним числом
        break # Виходимо з циклу, якщо перевірка успішна

    except ValueError:
        print("Помилка: Невірний формат вводу. Будь ласка, введіть ціле **натуральне** число (наприклад, 15).")
