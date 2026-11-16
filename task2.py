import re
from collections import Counter


def get_words(text: str) -> list[str]:
    return re.findall(r"[^\W_]+", text.lower())


def word_frequency(words: list[str]) -> list[tuple]:
    counts = Counter(words)
    return sorted(counts.items(), key=lambda x: (-x[1], x[0]))[:10]


def find_palindromes(words: list[str]) -> list[str]:
    result = []

    for word in words:
        if len(word) >= 3 and word == word[::-1]:
            if word not in result:
                result.append(word)

    return result


def check_email(email: str) -> bool:
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+"
    return re.fullmatch(pattern, email) is not None


def check_phone(phone: str) -> bool:
    pattern = r"(?:\+7|8)[ -]?\(?\d{3}\)?[ -]?\d{3}[ -]?\d{2}[ -]?\d{2}"
    return re.fullmatch(pattern, phone) is not None


def caesar(text: str, k: int) -> str:
    result = ""

    alphabets = (
        "abcdefghijklmnopqrstuvwxyz",
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "абвгдеёжзийклмнопрстуфхцчшщъыьэюя",
        "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    )

    for char in text:
        new_char = char

        for alphabet in alphabets:
            if char in alphabet:
                index = alphabet.index(char)
                new_char = alphabet[(index + k) % len(alphabet)]
                break

        result += new_char

    return result


def average_word_length(words: list[str]) -> float:
    if not words:
        return 0.0

    return round(sum(len(word) for word in words) / len(words), 2)


if __name__ == "__main__":
    # Ввод текста
    print("Введите текст (пустая строка для завершения): ")
    lines = []

    while True:
        line = input()
        if not line:
            break
        lines.append(line)

    text = "\n".join(lines)
    words = get_words(text)

    if not words:
        print("В тексте нет слов")
    else:
        print("\nСлова текста:")
        print(*words, sep=", ")

        # Частота слов
        print("\nТоп-10 самых частых слов:")
        frequency = word_frequency(words)

        for i, (word, count) in enumerate(frequency, 1):
            print(f"{i}. {word} — {count}")

        # Палиндромы
        print("\nСлова-палиндромы:")
        palindromes = find_palindromes(words)

        if palindromes:
            print(*palindromes, sep=", ")
        else:
            print("Палиндромов нет")

    # Проверка email
    print("\nПроверка email-адресов")
    emails = input("Введите email через пробел: ").split()

    if emails:
        for email in emails:
            status = "валидный" if check_email(email) else "невалидный"
            print(f"Email «{email}» — {status}")
    else:
        print("Email-адреса не введены")

    # Проверка телефонов
    print("\nПроверка номеров телефонов")
    print("Введите номера через запятую:")
    phones = input().split(",")

    if any(phone.strip() for phone in phones):
        for phone in phones:
            phone = phone.strip()
            if not phone:
                continue
            status = "валидный" if check_phone(phone) else "невалидный"
            print(f"Телефон «{phone}» — {status}")
    else:
        print("Номера телефонов не введены")

    print("\nШифр Цезаря")

    while True:
        try:
            k = int(input("Введите сдвиг K: "))
            break
        except ValueError:
            print("Некорректный ввод")

    encrypted = caesar(text, k)
    decrypted = caesar(encrypted, -k)

    print(f"\nЗашифрованный текст:\n{encrypted}")
    print(f"\nРасшифрованный текст:\n{decrypted}")

    # Средняя длина слова
    print("\nСредняя длина слова:")
    print(f"{average_word_length(words):.2f}")
