from random import randint

from brain_games import (
    NEGATIVE_ANSWER,
    POSITIVE_ANSWER,
    QuestionWithAnswer,
)
from brain_games.games.process_game import process_game

MIN_NUMBER = 1
MAX_NUMBER = 100


def is_even(number: int) -> bool:
    """Проверяет четность числа

    Args:
        number (int): число

    Returns:
        bool: четное ли число
    """
    return number % 2 == 0


def generate_question() -> QuestionWithAnswer:
    """Создает вопрос и эталонный ответ к нему

    Returns:
        QuestionWithAnswer: текст вопроса, текст эталонного ответа
    """
    number = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = POSITIVE_ANSWER if is_even(number) else NEGATIVE_ANSWER
    
    return str(number), correct_answer


def main() -> None:
    """Точка входа в игру
    """   
    instruction = \
        f"Answer \"{POSITIVE_ANSWER}\" if the number is even, " + \
        f"otherwise answer \"{NEGATIVE_ANSWER}\"."
    
    process_game(instruction, generate_question)


if __name__ == "__main__":
    main()
