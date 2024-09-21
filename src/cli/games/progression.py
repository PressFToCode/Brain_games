"""
Этот модуль содержит функции для игры "Прогрессия".
"""
import random


GAME_RULE = "Find the missing number in the geometric progression."

# Функция для создания геометрической прогрессии
def generate_progression(start, ratio, length, hidden_index):
    """
    Генерирует геометрическую прогрессию и заменяет 
    ее элемент по указанному индексу на ".." для создания вопроса.
    
    Аргументы:
        start (int): Начальное число геометрической прогрессии.
        ratio (int): Коэффициент геометрической прогрессии.
        length (int): Длина геометрической прогрессии.
        hidden_index (int): Индекс элемента, который будет заменен на "..".
    
    Возвращает:
        tuple: Кортеж, содержащий модифицированную геометрическую прогрессию и правильный ответ.
    """
    progression = [start * (ratio ** i) for i in range(length)]
    correct_answer = progression[hidden_index]
    progression[hidden_index] = ".."
    return progression, correct_answer

# Генерация вопроса и правильного ответа для игры "Геометрическая прогрессия"
def generate_round(start, ratio, length, hidden_index):
    """
    Генерирует вопрос и правильный ответ для игры "Геометрическая прогрессия".
    
    Аргументы:
        start (int): Начальное число геометрической прогрессии.
        ratio (int): Коэффициент геометрической прогрессии.
        length (int): Длина геометрической прогрессии.
        hidden_index (int): Индекс элемента, который будет скрыт в прогрессии.
    
    Возвращает:
        tuple: Кортеж, содержащий вопрос в виде строки и правильный ответ в виде целого числа.
    """
    progression, correct_answer = generate_progression(start, ratio, length, hidden_index)
    question = " ".join(map(str, progression))
    return question, correct_answer


def generate_progression_round():
    """
    Генерирует раунд для игры в геометрическую прогрессию.

    Эта функция генерирует случайный старт, коэффициент, длину и индекс скрытого элемента
    и вызывает функцию `progression.generate_round` с этими параметрами.

    Параметры:
        None

    Возвращает:
        tuple: Кортеж, содержащий вопрос и правильный ответ.
    """
    start = random.randint(1, 10)
    ratio = random.randint(2, 5)
    length = random.randint(5, 10)
    hidden_index = random.randint(0, length - 1)
    return generate_round(start, ratio, length, hidden_index)
