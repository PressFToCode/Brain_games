"""
Этот модуль содержит главную функцию программы Brain Games, в частности исполняемый файл программы.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'src', 'cli'))

from game_engine import play_game, welcome_user, choose_game
from games import scm, progression

def main():
    """
    Главная функция программы Brain Games.

    Эта функция выводит сообщение о приветствии и предлагает пользователю выбрать игру.
    Затем она берет ввод пользователя, чтобы определить, какую игру играть.

    Если пользователь выбирает игру 1, она генерирует случайный набор чисел и вызывает функцию 
    `play_game` с аргументами `scm.game_rule` и `generate_scm_round`.

    Если пользователь выбирает игру 2, она генерирует случайный набор чисел и вызывает функцию 
    `play_game` с аргументами `progression.game_rule` и `generate_progression_round`.

    Если пользователь вводит недопустимый выбор, она выводит сообщение об ошибке и возвращает.

    Параметры:
    None

    Возвращает:
    None
    """
    name = welcome_user()
    choose_game()
    game_choice = input("Enter 1 or 2: ")
    if game_choice == '1':
        play_game(scm.GAME_RULE, scm.generate_scm_round, name=name)
    elif game_choice == '2':
        play_game(progression.GAME_RULE, progression.generate_progression_round, name=name)
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
