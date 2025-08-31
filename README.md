## Учебный проект на Python с реализацией простых консольных игр

### Тесты [Hexlet](https://ru.hexlet.io/) и статусы линтера [SonarCloud](https://sonarcloud.io/)

[![Actions Status](https://github.com/experiment0/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/experiment0/python-project-49/actions)

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=experiment0_python-project-49&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=experiment0_python-project-49)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=experiment0_python-project-49&metric=bugs)](https://sonarcloud.io/summary/new_code?id=experiment0_python-project-49)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=experiment0_python-project-49&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=experiment0_python-project-49)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=experiment0_python-project-49&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=experiment0_python-project-49)

### О проекте

Данный учебный проект реализован в процессе прохождения курса [Python-разработчик](https://ru.hexlet.io/programs/python).\
В нем реализована серия простых консольных игр, основанных на арифметических вычислениях.\
Каждая игра запускается отдельной командой.\
Игра, в которой пользователь трижды верно ответил на вопрос, заканчивается победой.\
Если пользователь ответил не верно, игра просто заканчивается.

| Команда           | Задача игры                                                       |
| ----------------- | ----------------------------------------------------------------- |
| brain-games       | Просто приветствие пользователя по имени. Задачи как таковой нет. |
| brain-even        | Определить, является ли число четным.                             |
| brain-calc        | Посчитать сумму, разность, произведение чисел.                    |
| brain-gcd         | Найти НОД двух чисел.                                             |
| brain-progression | Определить пропущенное число в арифметической прогрессии.         |
| brain-prime       | Определить, является ли число простым.                            |

### Инструкция по запуску

1. Проверить, установлена ли утилита `uv`:

   ```bash
   uv --version
   ```

   Если не установлена, то нужно установить [по инструкции](https://docs.astral.sh/uv/getting-started/installation/#installation-methods).

2. Установка пакета из данного репо:

   ```bash
   uv tool install --force git+https://github.com/experiment0/python-project-49.git
   ```

   Флаг `--force` нужен на случай, если данный пакет уже был установлен ранее.

3. Демонстрация процесса игры:

   [![asciicast](https://asciinema.org/a/JktqrmcsLVbSG1ntHaYgxmy2Q.svg)](https://asciinema.org/a/JktqrmcsLVbSG1ntHaYgxmy2Q)
