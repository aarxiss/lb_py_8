import string

def analyze_text(text, ignore_spaces=True, ignore_digits=False, ignore_punctuation=False):
    filtered_text = text

    if ignore_spaces:
        filtered_text = filtered_text.replace(" ", "")
    if ignore_digits:
        filtered_text = ''.join(ch for ch in filtered_text if not ch.isdigit())
    if ignore_punctuation:
        filtered_text = ''.join(ch for ch in filtered_text if ch not in string.punctuation)

    # Частота символів
    frequency = {}
    for ch in filtered_text:
        frequency[ch] = frequency.get(ch, 0) + 1

    unique_chars = set(frequency.keys())

    # Вивід результатів
    print("\n📊 Результати аналізу:")
    print("1️⃣ Частота символів (словник):")
    print(frequency)

    print("\n2️⃣ Унікальні символи (множина):")
    print(unique_chars)

    # Вивести символи, що зустрічаються певну кількість разів
    try:
        n = int(input("\n🔢 Введіть кількість, щоб знайти символи, які зустрічаються рівно стільки разів: "))
        filtered_by_n = [ch for ch, count in frequency.items() if count == n]
        print(f"🔍 Символи, які зустрічаються {n} разів: {filtered_by_n}")
    except ValueError:
        print("⚠️ Невірне число, пропускаємо цю частину.")

# 🧾 Основна частина програми
if __name__ == "__main__":
    user_text = input("Введіть текст для аналізу: ")

    print("\n🔧 Налаштування:")
    ignore_spaces = input("Ігнорувати пробіли? (так/ні): ").strip().lower() == "так"
    ignore_digits = input("Ігнорувати цифри? (так/ні): ").strip().lower() == "так"
    ignore_punctuation = input("Ігнорувати пунктуацію? (так/ні): ").strip().lower() == "так"

    analyze_text(user_text, ignore_spaces, ignore_digits, ignore_punctuation)
