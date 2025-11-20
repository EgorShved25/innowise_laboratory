def generate_profile(age):
    """Определяет жизненный этап по возрасту."""
    if 0 <= age <= 12:
        return "Ребенок"
    elif 13 <= age <= 19:
        return "Подросток"
    elif age >= 20:
        return "Взрослый"
    else:
        return "Неизвестно"

def main():
    user_name = input("Введите ваше полное имя: ")
    birth_year_str = input("Введите ваш год рождения: ")

    # Обработка ввода года рождения
    try:
        birth_year = int(birth_year_str)
    except ValueError:
        print("Некорректный ввод года рождения. Завершение программы.")
        return

    current_year = 2025
    current_age = current_year - birth_year

    # сбор увлечений
    hobbies = []
    while True:
        hobby = input("Введите любимое хобби или напишите 'stop' для завершения: ")
        if hobby.lower() == 'stop':
            break
        hobbies.append(hobby)

    # определение жизненного этапа
    life_stage = generate_profile(current_age)

    # создание профиля
    user_profile = {
        'name': user_name,
        'age': current_age,
        'stage': life_stage,
        'hobbies': hobbies
    }

    # вывод сводки
    print("\n--- Краткий профиль ---")
    print(f"Имя: {user_profile['name']}")
    print(f"Возраст: {user_profile['age']}")
    print(f"Жизненный этап: {user_profile['stage']}")

    # обработка хобби
    if not user_profile['hobbies']:
        print("Вы не указали хобби.")
    else:
        print(f"Любимые хобби ({len(user_profile['hobbies'])}):")
        for hobby in user_profile['hobbies']:
            print(f"- {hobby}")

if __name__ == "__main__":
    main()