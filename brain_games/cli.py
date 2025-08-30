from typing import Optional

import prompt


def welcome_user() -> Optional[str]:
    """Приветствует пользователя и возвращает его имя

    Returns:
        Optional[str]: имя пользователя
    """
    print("Welcome to the Brain Games!")    
    user_name = prompt.string("May I have your name? ")    
    print(f"Hello, {user_name}!")
    
    return user_name
