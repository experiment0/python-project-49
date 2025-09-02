from enum import Enum, auto
from random import choice, randint

from brain_games import QuestionWithAnswer
from brain_games.games.process_game import process_game

MIN_GENERAL_NUMBER = 1

MAX_ADDED_NUMBER = 50

MAX_FIRST_MULTIPLIER = 30
MAX_SECOND_MULTIPLIER = 10


class Operation(Enum):  
    ADDITION = auto()
    SUBTRACTION = auto()
    MULTIPLICATION = auto()


def generate_question() -> QuestionWithAnswer:
    """Создает вопрос и эталонный ответ к нему

    Returns:
        QuestionWithAnswer: текст вопроса, текст эталонного ответа
    """
    operation = choice(list(Operation))
    
    match operation:
        case Operation.ADDITION:
            first_number = randint(MIN_GENERAL_NUMBER, MAX_ADDED_NUMBER)
            second_number = randint(MIN_GENERAL_NUMBER, MAX_ADDED_NUMBER)
            correct_answer = first_number + second_number
            question = f"{first_number} + {second_number}"
        case Operation.SUBTRACTION:
            first_number = randint(MIN_GENERAL_NUMBER, MAX_ADDED_NUMBER)
            second_number = randint(MIN_GENERAL_NUMBER, MAX_ADDED_NUMBER)
            correct_answer = first_number - second_number
            question = f"{first_number} - {second_number}"
        case Operation.MULTIPLICATION:
            first_number = randint(MIN_GENERAL_NUMBER, MAX_FIRST_MULTIPLIER)
            second_number = randint(MIN_GENERAL_NUMBER, MAX_SECOND_MULTIPLIER)
            correct_answer = first_number * second_number
            question = f"{first_number} * {second_number}"
        
    return question, str(correct_answer)


def main() -> None:
    """Точка входа в игру
    """
    instruction = "What is the result of the expression?"
    
    process_game(instruction, generate_question)


if __name__ == "__main__":
    main()
    
    
    