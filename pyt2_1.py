# Файл: main_program.py

# Підключення функції is_deficient_number з модуля deficient_checker
from deficient_checker import is_deficient_number

def get_natural_number_input() -> int:
    """
    Запитує користувача ввести натуральне число (ціле, > 0).
    """
    while True:
        try:
            n_str = input("Введіть натуральне число n для перевірки: ")
            n = int(n_str)
            if n <= 0:
                print("Помилка: Число має бути натуральним (більшим за 0).")
                continue
            return n
        except ValueError:
            print("Помилка: Введено некоректне значення. Будь ласка, введіть ціле число.")

# --- Основна частина програми ---
if __name__ == "__main__":
    print("✨ Перевірка числа на властивість 'Недостатнє число' ✨")
    
    # Використовуємо функцію для отримання вхідних даних
    number_n = get_natural_number_input()
    
    # Використовуємо підключену функцію з окремого модуля
    try:
        is_deficient = is_deficient_number(number_n)
        
        # Виведення результату
        print("-" * 50)
        print(f"Число n: {number_n}")
        
        if is_deficient:
            print(f"✅ Число {number_n} є **недостатнім числом**.")
            print("(Сума власних дільників < {number_n})")
        else:
            print(f"❌ Число {number_n} **НЕ** є недостатнім числом.")
            # Для повноти можна вказати, яке воно: досконале (Perfect) чи надлишкове (Abundant)
            print("(Воно може бути досконалим або надлишковим числом.)")
            
        print("-" * 50)

    except ValueError as e:
        print(f"Помилка: {e}")
