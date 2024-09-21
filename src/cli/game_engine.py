"""
Этот модуль содержит основные функции для запуска игры.
"""

def welcome_user():
    """
    Выводит сообщение о приветствии, запрашивает имя пользователя и возвращает его.
    
    Возвращает:
        str: Имя пользователя.
    """
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def choose_game():
    """
    Выводит список доступных игр и запрашивает выбор пользователя.

    Параметры:
        None

    Возвращает:
        int: Номер выбранной игры.
    """
    print("Please choose a game to play:")
    print("1. Find the smallest common multiple (НОК)")
    print("2. Find the missing number in the geometric progression")


def play_game(game_rule, generate_round, name):
    """
    Запускает игру на основе предоставленного правила игры и генератора раундов.

    Параметры:
        game_rule (str): Правило игры, отображаемое пользователю.
        generate_round (function): Функция, генерирующая вопрос и его правильный ответ.

    Возвращает:
        None
    """
    print(game_rule)
    rounds = 3
    while rounds > 0:
        question, correct_answer = generate_round()
        print(f"Question: {question}")
        answer = input("Your answer: ")
        if answer == str(correct_answer):
            print("Correct!")
            rounds -= 1
        else:
            print(f"'{answer}' is wrong answer. The correct answer was '{correct_answer}'.")
            rounds -= 1
    print(f"Congratulations, {name}! You've completed the game.")
    input("Press Enter to exit.")
