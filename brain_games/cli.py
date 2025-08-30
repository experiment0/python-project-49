import prompt


def welcome_user() -> str:
    """Приветствует пользователя и возвращает его имя

    Returns:
        str: имя пользователя
    """
    print("Welcome to the Brain Games!")    
    user_name = prompt.string("May I have your name? ")    
    print(f"Hello, {user_name}!")
    
    return user_name or ""
