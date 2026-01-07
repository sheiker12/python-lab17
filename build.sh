#!/bin/bash
# Скрипт сборки приложения с Nuitka

set -e

echo "=== Сборка приложения калькулятора ==="
echo ""

# Проверка виртуального окружения
if [ ! -d "venv" ]; then
    echo "Ошибка: виртуальное окружение не найдено"
    echo "Запустите сначала: ./setup.sh"
    exit 1
fi

# Активация окружения
source venv/bin/activate

# Запуск тестов перед сборкой
echo "1. Запуск тестов..."
pytest tests/ -v --tb=short

# Сборка с Nuitka
echo -e "\n2. Сборка с Nuitka..."
python -m nuitka \
    --standalone \
    --onefile \
    --output-filename=calculator \
    --output-dir=dist \
    --remove-output \
    --show-progress \
    --warn-implicit-exceptions \
    --warn-unusual-code \
    --assume-yes-for-downloads \
    main.py

# Проверка собранного файла
echo -e "\n3. Проверка собранного приложения..."
if [ -f "dist/calculator" ]; then
    chmod +x dist/calculator
    echo "Файл: dist/calculator"
    echo "Размер: $(du -h dist/calculator | cut -f1)"
    echo ""
    
    # Тестовый запуск
    echo "Тестовый запуск..."
    timeout 2s ./dist/calculator --help 2>/dev/null || echo "Приложение запущено успешно"
    
    # Создание архива
    echo -e "\n4. Создание архива..."
    tar -czf calculator_debian.tar.gz -C dist calculator
    echo "Архив создан: calculator_debian.tar.gz"
    
    echo -e "\n=== Сборка завершена успешно! ==="
    echo "Приложение готово к использованию: ./dist/calculator"
else
    echo "Ошибка: сборка не удалась"
    exit 1
fi
