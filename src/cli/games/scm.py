"""
Этот модуль содержит функции для игры "НОК".
"""

import math
import random

# Правила игры
GAME_RULE = "Find the smallest common multiple of given numbers."

# Функция для нахождения НОК трёх чисел
def smallest_common_multiple(num1, num2, num3):
    """
    Эта функция вычисляет наименьшее общее кратное (НОК) трёх заданных чисел.

    Параметры:
        num1 (int): Первое число.
        num2 (int): Второе число.
        num3 (int): Третье число.

    Возвращает:
        int: Наименьшее общее кратное num1, num2 и num3.
    """
    def lcm(a, b):
        return abs(a * b) // math.gcd(a, b)
    return lcm(lcm(num1, num2), num3)

# Генерация вопроса и правильного ответа для игры "НОК"
def generate_round(num1, num2, num3):
    """
    Генерирует вопрос и правильный ответ для игры наименьшего общего кратного.
    
    Параметры:
        num1 (int): Первое число.
        num2 (int): Второе число.
        num3 (int): Третье число.
    
    Возвращает:
        tuple: Кортеж, содержащий вопрос и правильный ответ.
    """
    question = f"{num1}, {num2}, {num3}"
    correct_answer = smallest_common_multiple(num1, num2, num3)
    return question, correct_answer

def generate_scm_round():
    """
    Генерирует раунд для игры в наименьшее общее кратное (НОК).

    Эта функция генерирует три случайных числа от 1 до 15 и 
    использует их для создания вопроса и правильного ответа для игры.

    Параметры:
        Нет

    Возвращает:
        кортеж: Кортеж, содержащий вопрос и правильный ответ для игры.
    """
    num1 = random.randint(1, 15)
    num2 = random.randint(1, 15)
    num3 = random.randint(1, 15)
    return generate_round(num1, num2, num3)
