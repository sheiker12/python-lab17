"""
Тесты для модуля калькулятора
"""

import pytest
import math
from src.calculator import Calculator


class TestCalculator:
    """Тестовый класс для калькулятора"""
    
    @pytest.fixture
    def calc(self):
        """Фикстура создания калькулятора"""
        return Calculator()
    
    # Тесты сложения
    def test_add_positive(self, calc):
        """Тест сложения положительных чисел"""
        assert calc.add(2, 3) == 5
        assert calc.add(0, 0) == 0
        assert calc.add(1.5, 2.5) == 4.0
    
    def test_add_negative(self, calc):
        """Тест сложения отрицательных чисел"""
        assert calc.add(-2, -3) == -5
        assert calc.add(-1, 1) == 0
    
    # Тесты вычитания
    def test_subtract_positive(self, calc):
        """Тест вычитания положительных чисел"""
        assert calc.subtract(5, 3) == 2
        assert calc.subtract(3, 5) == -2
    
    def test_subtract_negative(self, calc):
        """Тест вычитания отрицательных чисел"""
        assert calc.subtract(-2, -3) == 1
        assert calc.subtract(-5, 2) == -7
    
    # Тесты умножения
    def test_multiply_positive(self, calc):
        """Тест умножения положительных чисел"""
        assert calc.multiply(2, 3) == 6
        assert calc.multiply(0, 5) == 0
        assert calc.multiply(1.5, 2) == 3.0
    
    def test_multiply_negative(self, calc):
        """Тест умножения отрицательных чисел"""
        assert calc.multiply(-2, 3) == -6
        assert calc.multiply(-2, -3) == 6
    
    # Тесты деления
    def test_divide_positive(self, calc):
        """Тест деления положительных чисел"""
        assert calc.divide(6, 3) == 2
        assert calc.divide(5, 2) == 2.5
    
    def test_divide_negative(self, calc):
        """Тест деления отрицательных чисел"""
        assert calc.divide(-6, 3) == -2
        assert calc.divide(6, -3) == -2
    
    def test_divide_by_zero_raises_error(self, calc):
        """Тест что деление на ноль вызывает ошибку"""
        with pytest.raises(ValueError, match="Деление на ноль невозможно"):
            calc.divide(5, 0)
    
    # Тесты возведения в степень
    def test_power_positive(self, calc):
        """Тест возведения в степень"""
        assert calc.power(2, 3) == 8
        assert calc.power(5, 0) == 1
        assert calc.power(2, -1) == 0.5
    
    # Тесты квадратного корня
    def test_sqrt_positive(self, calc):
        """Тест квадратного корня положительных чисел"""
        assert calc.sqrt(4) == 2
        assert calc.sqrt(9) == 3
        assert calc.sqrt(0) == 0
    
    def test_sqrt_negative_raises_error(self, calc):
        """Тест что корень отрицательного числа вызывает ошибку"""
        with pytest.raises(ValueError, match="Корень из отрицательного числа невозможен"):
            calc.sqrt(-4)
    
    # Тесты факториала
    def test_factorial_positive(self, calc):
        """Тест факториала положительных чисел"""
        assert calc.factorial(0) == 1
        assert calc.factorial(1) == 1
        assert calc.factorial(5) == 120
    
    def test_factorial_negative_raises_error(self, calc):
        """Тест что факториал отрицательного числа вызывает ошибку"""
        with pytest.raises(ValueError, match="Факториал отрицательного числа невозможен"):
            calc.factorial(-1)
    
    # Тесты вычисления выражения
    def test_calculate_expression_simple(self, calc):
        """Тест вычисления простого выражения"""
        assert calc.calculate_expression("2 + 3") == 5
        assert calc.calculate_expression("2 * 3 + 4") == 10
    
    def test_calculate_expression_invalid_chars(self, calc):
        """Тест что недопустимые символы вызывают ошибку"""
        with pytest.raises(ValueError, match="Выражение содержит недопустимые символы"):
            calc.calculate_expression("import os")
    
    def test_calculate_expression_invalid_syntax(self, calc):
        """Тест что неверный синтаксис вызывает ошибку"""
        with pytest.raises(ValueError):
            calc.calculate_expression("2 + ")
    
    # Тесты истории операций
    def test_history_empty_initially(self, calc):
        """Тест что история пуста при создании"""
        assert calc.get_history() == []
    
    def test_history_adds_operations(self, calc):
        """Тест что операции добавляются в историю"""
        calc.add(2, 3)
        calc.subtract(5, 3)
        history = calc.get_history()
        assert len(history) == 2
        assert "2 + 3 = 5" in history[0]
        assert "5 - 3 = 2" in history[1]
    
    def test_history_limit(self, calc):
        """Тест ограничения истории"""
        for i in range(15):
            calc.add(i, i)
        assert len(calc.get_history()) == 10
    
    def test_clear_history(self, calc):
        """Тест очистки истории"""
        calc.add(2, 3)
        calc.clear_history()
        assert calc.get_history() == []
    
    # Параметризованные тесты
    @pytest.mark.parametrize("a,b,expected", [
        (0, 0, 0),
        (1, 2, 3),
        (-1, -2, -3),
        (1.5, 2.5, 4.0),
    ])
    def test_add_parametrized(self, calc, a, b, expected):
        """Параметризованный тест сложения"""
        assert calc.add(a, b) == expected
    
    @pytest.mark.parametrize("a,b,expected", [
        (6, 3, 2),
        (10, 2, 5),
        (-6, 3, -2),
    ])
    def test_divide_parametrized(self, calc, a, b, expected):
        """Параметризованный тест деления"""
        assert calc.divide(a, b) == expected
    
    # Тест на исключения
    def test_exception_messages(self, calc):
        """Тест сообщений об ошибках"""
        with pytest.raises(ValueError) as exc_info:
            calc.divide(5, 0)
        assert "Деление на ноль невозможно" in str(exc_info.value)
        
        with pytest.raises(ValueError) as exc_info:
            calc.sqrt(-1)
        assert "Корень из отрицательного числа невозможен" in str(exc_info.value)
    
    # Медленные тесты (помечены маркером slow)
    @pytest.mark.slow
    def test_power_large_numbers(self, calc):
        """Тест возведения больших чисел в степень"""
        assert calc.power(2, 10) == 1024
        assert calc.power(10, 6) == 1000000
    
    @pytest.mark.slow
    def test_factorial_large_number(self, calc):
        """Тест факториала большого числа"""
        assert calc.factorial(10) == 3628800
