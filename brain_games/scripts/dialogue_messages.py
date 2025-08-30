import prompt


def display_question(question: str) -> None:
    """Выводит вопрос для пользователя

    Args:
        question (str): текст или число для вопроса
    """
    print(f"Question: {question}")


def get_user_answer() -> str:
    """Возвращает ответ пользователя

    Returns:
        str: ответ, полученный от пользователя
    """
    user_answer = prompt.string("Your answer: ")
    
    return user_answer or ""


def display_success() -> None:
    """Сообщает пользователю о том, что он правильно ответил на вопрос
    """
    print("Correct!")


def display_error(
    user_name: str, 
    user_answer: str, 
    correct_answer: str
) -> None:
    """Сообщает пользователю о том, что он не правильно ответил на вопрос

    Args:
        user_name (str): имя пользователя
        user_answer (str): ответ, который дал пользователь
        correct_answer (str): правильный ответ
    """
    print(
        f"'{user_answer}' is wrong answer ;(. " + 
        f"Correct answer was '{correct_answer}'."
    )    
    print(f"Let's try again, {user_name}!")
    

def display_victory(user_name: str) -> None:
    """Сообщает пользователю о победе

    Args:
        user_name (str): имя пользователя
    """
    print(f"Congratulations, {user_name}!")
