def main():
    students = []

    def find_student(name):
        for student in students:
            if student['name'].lower() == name.lower():
                return student
        return None

    while True:
        print("\n--- Анализатор оценок студентов ---")
        print("1. Добавить нового студента")
        print("2. Добавить оценки студенту")
        print("3. Показать отчет (все студенты)")
        print("4. Найти лучшего студента")
        print("5. Выйти")
        choice = input("Введите номер опции: ")

        try:
            choice = int(choice)
        except ValueError:
            print("Пожалуйста, введите число от 1 до 5.")
            continue

        if choice == 1:
            name = input("Введите имя студента: ").strip()
            if find_student(name):
                print(f"Студент с именем '{name}' уже существует.")
            else:
                students.append({'name': name, 'grades': []})
                print(f"Студент '{name}' добавлен.")

        elif choice == 2:
            name = input("Введите имя студента: ").strip()
            student = find_student(name)
            if not student:
                print(f"Студент с именем '{name}' не найден.")
                continue
            while True:
                grade_input = input("Введите оценку (или 'done' для завершения): ").strip()
                if grade_input.lower() == 'done':
                    break
                try:
                    grade = float(grade_input)
                    if 0 <= grade <= 100:
                        student['grades'].append(grade)
                        print(f"Оценка {grade} добавлена.")
                    else:
                        print("Пожалуйста, введите число от 0 до 100.")
                except ValueError:
                    print("Некорректный ввод. Введите число или 'done'.")

        elif choice == 3:
            if not students:
                print("Нет данных о студентах.")
                continue
            print("\n--- Отчет студентов ---")
            all_grades = []
            max_avg = None
            min_avg = None
            total_avg_sum = 0
            total_counts = 0
            for student in students:
                grades = student['grades']
                if grades:
                    try:
                        avg = sum(grades) / len(grades)
                        print(f"{student['name']} — средний балл: {avg:.2f}")
                        all_grades.extend(grades)
                        if (max_avg is None) or (avg > max_avg):
                            max_avg = avg
                        if (min_avg is None) or (avg < min_avg):
                            min_avg = avg
                        total_avg_sum += sum(grades)
                        total_counts += len(grades)
                    except ZeroDivisionError:
                        print(f"{student['name']} — оценки отсутствуют.")
                else:
                    print(f"{student['name']} — оценок нет (N/A).")
            if all_grades:
                try:
                    overall_avg = sum(all_grades) / len(all_grades)
                    print(f"Максимальный средний: {max_avg:.2f}")
                    print(f"Минимальный средний: {min_avg:.2f}")
                    print(f"Общий средний: {overall_avg:.2f}")
                except ZeroDivisionError:
                    print("Нет оценок для вычисления общего среднего.")
            else:
                print("Нет оценок для отображения статистики.")

        elif choice == 4:
            if not students:
                print("Нет студентов для анализа.")
                continue
            # Отфильтровать студентов с оценками
            students_with_grades = [s for s in students if s['grades']]
            if not students_with_grades:
                print("У всех студентов отсутствуют оценки.")
                continue
            top_student = max(
                students_with_grades,
                key=lambda s: sum(s['grades']) / len(s['grades'])
            )
            avg = sum(top_student['grades']) / len(top_student['grades'])
            print(f"Лучший студент: {top_student['name']} со средним баллом {avg:.2f}")

        elif choice == 5:
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите число от 1 до 5.")

if __name__ == "__main__":
    main()