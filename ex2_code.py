def process_lists(list1, list2):
    print("\n📥 Вхідні списки:")
    print(f"Список 1: {list1}")
    print(f"Список 2: {list2}")

    # 1. Об'єднання
    combined = list1 + list2
    print("\n🔗 Об'єднаний список:")
    print(combined)

    # 2. Без повторів
    no_duplicates = list(set(combined))
    print("\n🚫 Без повторів:")
    print(no_duplicates)

    # 3. Відсортований список
    sorted_list = sorted(no_duplicates)
    print("\n📊 Відсортований список:")
    print(sorted_list)

    # 4. Якщо обидва списки порожні
    if not list1 and not list2:
        print("\n⚠️ Обидва списки порожні.")
    elif not list1:
        print("\nℹ️ Перший список порожній.")
    elif not list2:
        print("\nℹ️ Другий список порожній.")

# 🧾 Основна частина програми
def get_list_from_input(prompt):
    try:
        return list(map(int, input(prompt).strip().split()))
    except ValueError:
        print("⚠️ Введено нечислові значення. Список буде порожній.")
        return []

if __name__ == "__main__":
    list1 = get_list_from_input("Введіть перший список чисел (через пробіл): ")
    list2 = get_list_from_input("Введіть другий список чисел (через пробіл): ")
    process_lists(list1, list2)
