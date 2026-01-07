#!/bin/bash
# Скрипт установки для лабораторной работы №17

set -e  # Завершить при ошибке

echo "=== Установка лабораторной работы №17 ==="
echo "Система: $(lsb_release -ds)"
echo "Пользователь: $(whoami)"
echo "Дата: $(date)"
echo ""

# Проверка Python
echo "1. Проверка Python..."
python3 --version
if [ $? -ne 0 ]; then
    echo "Ошибка: Python3 не установлен"
    exit 1
fi

# Создание виртуального окружения
echo -e "\n2. Создание виртуального окружения..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "Виртуальное окружение создано"
else
    echo "Виртуальное окружение уже существует"
fi

# Активация и установка зависимостей
echo -e "\n3. Установка зависимостей..."
source venv/bin/activate
pip install --upgrade pip
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    echo "Ошибка: requirements.txt не найден"
    exit 1
fi

# Проверка установки
echo -e "\n4. Проверка установки..."
echo "Python: $(python --version)"
echo "PIP: $(pip --version)"
echo "Pytest: $(pytest --version 2>/dev/null || echo 'не установлен')"

# Инициализация Git (если не инициализирован)
if [ ! -d ".git" ]; then
    echo -e "\n5. Инициализация Git..."
    git init
    git add .
    git commit -m "Initial commit: Lab 17 setup"
    echo "Git репозиторий инициализирован"
fi

echo -e "\n=== Установка завершена успешно! ==="
echo ""
echo "Для запуска приложения:"
echo "  source venv/bin/activate"
echo "  python main.py"
echo ""
echo "Для запуска тестов:"
echo "  pytest"
echo ""
echo "Для сборки с Nuitka:"
echo "  python -m nuitka --standalone main.py"
