from random import randint
from typing import List

from brain_games import QuestionWithAnswer
from brain_games.process_game import process_game

MIN_PROGRESSION_LENGTH = 5
MAX_PROGRESSION_LENGTH = 10

MIN_STEP = 2
MAX_STEP = 10

MIN_START_VALUE = 0
MAX_START_VALUE = 50


def get_progression(
    start_value: int, 
    step: int, 
    progression_length: int
) -> List[str]:
    """Формирует набор чисел арифметической прогрессии

    Args:
        start_value (int): начальное число
        step (int): шаг
        progression_length (int): количество числел в последовательности

    Returns:
        List[str]: набор чисел арифметической прогрессии
    """
    progression = []
    current_value = start_value
    
    for _ in range(progression_length):
        progression.append(str(current_value))
        current_value += step
    
    return progression


def generate_question() -> QuestionWithAnswer:
    """Создает вопрос и эталонный ответ к нему

    Returns:
        QuestionWithAnswer: текст вопроса, текст эталонного ответа
    """
    progression_length = randint(MIN_PROGRESSION_LENGTH, MAX_PROGRESSION_LENGTH)
    step = randint(MIN_STEP, MAX_STEP)
    start_value = randint(MIN_START_VALUE, MAX_START_VALUE)
    
    progression = get_progression(start_value, step, progression_length)
    
    missing_index = randint(0, progression_length - 1)
    correct_answer = progression[missing_index]
    progression[missing_index] = ".."
    
    question = " ".join(progression)
    
    return question, correct_answer


def main() -> None:
    """Точка входа в игру
    """
    instruction = "What number is missing in the progression?"
    
    process_game(instruction, generate_question)


if __name__ == "__main__":
    main()