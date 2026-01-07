#!/usr/bin/env python3
"""
Главный файл приложения калькулятора
"""

import sys
from src.calculator import Calculator


def print_menu():
    """Вывод меню программы"""
    print("\n" + "="*50)
    print("КАЛЬКУЛЯТОР - Лабораторная работа №17")
    print("="*50)
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Квадратный корень")
    print("7. Факториал")
    print("8. Вычислить выражение")
    print("9. Показать историю")
    print("10. Очистить историю")
    print("0. Выход")
    print("="*50)


def get_number(prompt: str) -> float:
    """Получение числа от пользователя"""
    while True:
        try:
            value = input(prompt)
            return float(value)
        except ValueError:
            print("Ошибка: введите число!")


def get_integer(prompt: str) -> int:
    """Получение целого числа от пользователя"""
    while True:
        try:
            value = input(prompt)
            return int(value)
        except ValueError:
            print("Ошибка: введите целое число!")


def main():
    """Основная функция программы"""
    calc = Calculator()
    
    print("Добро пожаловать в программу-калькулятор!")
    print("Автоматизация тестирования ПО на Python")
    
    while True:
        print_menu()
        
        try:
            choice = input("\nВыберите операцию (0-10): ").strip()
            
            if choice == '0':
                print("\nСпасибо за использование программы!")
                sys.exit(0)
            
            elif choice == '1':  # Сложение
                a = get_number("Введите первое число: ")
                b = get_number("Введите второе число: ")
                result = calc.add(a, b)
                print(f"\nРезультат: {a} + {b} = {result}")
            
            elif choice == '2':  # Вычитание
                a = get_number("Введите первое число: ")
                b = get_number("Введите второе число: ")
                result = calc.subtract(a, b)
                print(f"\nРезультат: {a} - {b} = {result}")
            
            elif choice == '3':  # Умножение
                a = get_number("Введите первое число: ")
                b = get_number("Введите второе число: ")
                result = calc.multiply(a, b)
                print(f"\nРезультат: {a} * {b} = {result}")
            
            elif choice == '4':  # Деление
                a = get_number("Введите первое число: ")
                b = get_number("Введите второе число: ")
                try:
                    result = calc.divide(a, b)
                    print(f"\nРезультат: {a} / {b} = {result}")
                except ValueError as e:
                    print(f"\nОшибка: {e}")
            
            elif choice == '5':  # Степень
                a = get_number("Введите основание: ")
                b = get_number("Введите показатель степени: ")
                result = calc.power(a, b)
                print(f"\nРезультат: {a} ^ {b} = {result}")
            
            elif choice == '6':  # Корень
                a = get_number("Введите число: ")
                try:
                    result = calc.sqrt(a)
                    print(f"\nРезультат: √{a} = {result}")
                except ValueError as e:
                    print(f"\nОшибка: {e}")
            
            elif choice == '7':  # Факториал
                a = get_integer("Введите целое число: ")
                try:
                    result = calc.factorial(a)
                    print(f"\nРезультат: {a}! = {result}")
                except ValueError as e:
                    print(f"\nОшибка: {e}")
            
            elif choice == '8':  # Выражение
                expr = input("Введите выражение (например: 2 + 3 * 4): ")
                try:
                    result = calc.calculate_expression(expr)
                    print(f"\nРезультат: {expr} = {result}")
                except ValueError as e:
                    print(f"\nОшибка: {e}")
            
            elif choice == '9':  # История
                history = calc.get_history()
                if history:
                    print("\nИстория операций:")
                    for i, op in enumerate(history, 1):
                        print(f"{i}. {op}")
                else:
                    print("\nИстория пуста")
            
            elif choice == '10':  # Очистка истории
                calc.clear_history()
                print("\nИстория очищена")
            
            else:
                print("\nОшибка: неверный выбор операции!")
        
        except KeyboardInterrupt:
            print("\n\nПрограмма прервана пользователем")
            sys.exit(0)
        except EOFError:
            print("\n\nКонец ввода")
            sys.exit(0)
        except Exception as e:
            print(f"\nНеожиданная ошибка: {e}")


if __name__ == "__main__":
    main()
