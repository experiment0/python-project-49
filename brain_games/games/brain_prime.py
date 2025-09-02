from math import floor, sqrt
from random import randint

from brain_games import (
    NEGATIVE_ANSWER,
    POSITIVE_ANSWER,
    QuestionWithAnswer,
)
from brain_games.games.process_game import process_game

MIN_NUMBER = 0
MAX_NUMBER = 100


def is_prime(number: int) -> bool:
    """Определяет, является ли число простым

    Args:
        number (int): число

    Returns:
        bool: является ли число простым
    """
    if number <= 1:
        return False
    if number <= 3:
        return True
    
    max_divisor = floor(sqrt(number))
    
    for i in range(2, max_divisor + 1):
        if number % i == 0:
            return False
    
    return True


def generate_question() -> QuestionWithAnswer:
    """Создает вопрос и эталонный ответ к нему

    Returns:
        QuestionWithAnswer: текст вопроса, текст эталонного ответа
    """
    number = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = POSITIVE_ANSWER if is_prime(number) else NEGATIVE_ANSWER
    
    return str(number), correct_answer


def main() -> None:
    """Точка входа в игру
    """   
    instruction = \
        f"Answer \"{POSITIVE_ANSWER}\" if given number is prime. " + \
        f"Otherwise answer \"{NEGATIVE_ANSWER}\"."        
    
    process_game(instruction, generate_question)


if __name__ == "__main__":
    main()
