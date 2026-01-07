"""
Модуль калькулятора для лабораторной работы №17
"""

import math


class Calculator:
    """Класс калькулятора с математическими операциями"""
    
    def __init__(self):
        """Инициализация калькулятора"""
        self.history = []
    
    def add(self, a: float, b: float) -> float:
        """
        Сложение двух чисел
        
        Args:
            a: Первое слагаемое
            b: Второе слагаемое
            
        Returns:
            Сумма a и b
        """
        result = a + b
        self._add_to_history(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a: float, b: float) -> float:
        """
        Вычитание
        
        Args:
            a: Уменьшаемое
            b: Вычитаемое
            
        Returns:
            Разность a и b
        """
        result = a - b
        self._add_to_history(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a: float, b: float) -> float:
        """
        Умножение
        
        Args:
            a: Первый множитель
            b: Второй множитель
            
        Returns:
            Произведение a и b
        """
        result = a * b
        self._add_to_history(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a: float, b: float) -> float:
        """
        Деление
        
        Args:
            a: Делимое
            b: Делитель
            
        Returns:
            Частное a и b
            
        Raises:
            ValueError: Если делитель равен нулю
        """
        if b == 0:
            raise ValueError("Деление на ноль невозможно")
        result = a / b
        self._add_to_history(f"{a} / {b} = {result}")
        return result
    
    def power(self, a: float, b: float) -> float:
        """
        Возведение в степень
        
        Args:
            a: Основание
            b: Показатель степени
            
        Returns:
            a в степени b
        """
        result = a ** b
        self._add_to_history(f"{a} ^ {b} = {result}")
        return result
    
    def sqrt(self, a: float) -> float:
        """
        Квадратный корень
        
        Args:
            a: Число
            
        Returns:
            Квадратный корень из a
            
        Raises:
            ValueError: Если число отрицательное
        """
        if a < 0:
            raise ValueError("Корень из отрицательного числа невозможен")
        result = math.sqrt(a)
        self._add_to_history(f"√{a} = {result}")
        return result
    
    def factorial(self, a: int) -> int:
        """
        Факториал числа
        
        Args:
            a: Целое неотрицательное число
            
        Returns:
            Факториал a
            
        Raises:
            ValueError: Если число отрицательное
        """
        if a < 0:
            raise ValueError("Факториал отрицательного числа невозможен")
        result = math.factorial(a)
        self._add_to_history(f"{a}! = {result}")
        return result
    
    def _add_to_history(self, operation: str):
        """Добавление операции в историю"""
        self.history.append(operation)
        if len(self.history) > 10:  # Ограничиваем историю 10 записями
            self.history.pop(0)
    
    def get_history(self) -> list:
        """Получение истории операций"""
        return self.history.copy()
    
    def clear_history(self):
        """Очистка истории операций"""
        self.history.clear()
    
    def calculate_expression(self, expression: str) -> float:
        """
        Вычисление математического выражения
        
        Args:
            expression: Строка с выражением
            
        Returns:
            Результат вычисления
        """
        # Безопасное вычисление выражения
        allowed_chars = set('0123456789+-*/.() ')
        if not all(c in allowed_chars for c in expression):
            raise ValueError("Выражение содержит недопустимые символы")
        
        try:
            result = eval(expression)
            self._add_to_history(f"{expression} = {result}")
            return result
        except Exception as e:
            raise ValueError(f"Ошибка вычисления выражения: {e}")
