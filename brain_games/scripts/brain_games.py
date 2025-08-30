from brain_games.cli import welcome_user


def main() -> None:
    """Точка входа в проект
    """
    user_name = welcome_user()


if __name__ == "__main__":
    main()
