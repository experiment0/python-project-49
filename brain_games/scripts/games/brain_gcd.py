from math import gcd
from random import randint

from brain_games import QuestionWithAnswer
from brain_games.process_game import process_game

MIN_NUMBER = 0
MAX_NUMBER = 100


def generate_question() -> QuestionWithAnswer:
    """Создает вопрос и эталонный ответ к нему

    Returns:
        QuestionWithAnswer: текст вопроса, текст эталонного ответа
    """
    first_number = randint(MIN_NUMBER, MAX_NUMBER)
    second_number = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = gcd(first_number, second_number)
    question = f"{first_number} {second_number}"
    
    return question, str(correct_answer)


def main() -> None:
    """Точка входа в игру
    """
    instruction = "Find the greatest common divisor of given numbers."
    
    process_game(instruction, generate_question)


if __name__ == "__main__":
    main()
