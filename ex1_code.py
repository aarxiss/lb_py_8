def analyze_text(text):
    vowels_ua = "аеєиіїоуюяAEЄИІЇОУЮЯaeєиіїоуюя"
    consonants_ua = "бвгґдєжзйклмнпрстфхцчшщБВГҐДЖЗЙКЛМНПРСТФХЦЧШЩбвгґджзйклмнпрстфхцчшщ"
    
    vowels = [ch for ch in text if ch.lower() in vowels_ua]
    consonants = [ch for ch in text if ch.lower() in consonants_ua]
    letters = [ch for ch in text if ch.isalpha()]

    # Частоти кожної букви
    freq = {}
    for ch in letters:
        ch_low = ch.lower()
        freq[ch_low] = freq.get(ch_low, 0) + 1

    # Виведення результатів
    print("\n🔠 Аналіз тексту:")
    print(f"Вхідний рядок: {text}")
    
    print("\n1️⃣ Голосні літери:")
    print(f"   Список: {vowels}")
    print(f"   Кількість: {len(vowels)}")

    print("\n2️⃣ Приголосні літери:")
    print(f"   Список: {consonants}")
    print(f"   Кількість: {len(consonants)}")

    print("\n3️⃣ Усі літери:")
    print(f"   Список: {letters}")
    print(f"   Кількість: {len(letters)}")

    print("\n4️⃣ Частота кожної літери:")
    for letter, count in sorted(freq.items()):
        print(f"   '{letter}': {count}")


# 🧾 Основна частина програми
if __name__ == "__main__":
    user_input = input("Введіть текст для аналізу: ")
    analyze_text(user_input)
