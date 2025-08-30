from typing import Callable, Tuple

from brain_games.cli import welcome_user
from brain_games.config import ROUNDS_COUNT
from brain_games.scripts.dialogue_messages import (
    display_error,
    display_question,
    display_success,
    display_victory,
    get_user_answer,
)


def process_game(
    instruction: str,
    generate_question: Callable[[], Tuple[str, str]],
) -> None:
    """Реализует процесс игры из нескольких раундов

    Args:
        instruction (str): инструкция для пользователя
        generate_question (Callable[[], Tuple[str, str]]): 
            фукнция, которая возвращает вопрос для пользователя 
            и эталонный ответ
    """
    user_name = welcome_user()
    print(instruction)
    
    current_round = 1
    correct_answers_count = 0
    is_user_answer_wrong = False
    
    while current_round <= ROUNDS_COUNT and not is_user_answer_wrong:        
        question, correct_answer = generate_question()
        display_question(question)
        
        user_answer = get_user_answer()
        is_user_answer_wrong = user_answer.lower() != correct_answer.lower()
        
        if is_user_answer_wrong:
            display_error(user_name, user_answer, correct_answer)
        else:
            correct_answers_count += 1
            display_success()
        
        current_round += 1
        
    if correct_answers_count == ROUNDS_COUNT:
        display_victory(user_name)
    