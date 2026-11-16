def mins_max(nums: list[int], n: int) -> tuple[list, list]:
    loc_min = []
    loc_max = []

    for i in range(1, n - 1):
        if nums[i] > nums[i + 1] and nums[i] > nums[i - 1]:
            loc_max.append((i, nums[i]))
        elif nums[i] < nums[i + 1] and nums[i] < nums[i - 1]:
            loc_min.append((i, nums[i]))

    return loc_min, loc_max


def avg(nums: list[int], k: int, n: int) -> list:
    if not (2 <= k <= n):
        raise ValueError("Некорректный размер окна")

    result = []
    for i in range(n - k + 1):
        result.append(
            (i + 1, i + k, round(sum(nums[i:i+k]) / k, 2))
        )
    return result


def mono(nums: list[int], n: int) -> str:
    increasing = all(nums[i] < nums[i + 1] for i in range(n - 1))
    decreasing = all(nums[i] > nums[i + 1] for i in range(n - 1))
    non_decreasing = all(nums[i] <= nums[i + 1] for i in range(n - 1))
    non_increasing = all(nums[i] >= nums[i + 1] for i in range(n - 1))

    if increasing:
        return "Последовательность строго возрастающая"
    elif decreasing:
        return "Последовательность строго убывающая"
    elif non_decreasing:
        return "Последовательность неубывающая"
    elif non_increasing:
        return "Последовательность невозрастающая"
    else:
        return "Последовательность немонотонная"


def longest_increasing(nums: list[int]) -> list[int]:
    longest = []
    current = [nums[0]]

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            current.append(nums[i])
        else:
            if len(current) > len(longest):
                longest = current
            current = [nums[i]]

    if len(current) > len(longest):
        longest = current

    return longest


def count_pairs(nums: list[int], s: int) -> int:
    counts = {}
    result = 0

    for num in nums:
        result += counts.get(s - num, 0)
        counts[num] = counts.get(num, 0) + 1

    return result


if __name__ == "__main__":
    # Ввод последовательности
    while True:
        try:
            n = int(input("Введите число N (5-500): "))
            if not (5 <= n <= 500):
                raise ValueError

            lst = list(map(int, input(
                "Последовательность длиной в N чисел: "
            ).split()))

            if len(lst) != n:
                raise ValueError
            break
        except ValueError:
            print("Некорректный ввод")

    print("\nИсходная последовательность:", end=" ")
    print(*lst, sep=", ")

    # Локальные экстремумы
    loc_min, loc_max = mins_max(lst, n)

    print("\nЛокальные минимумы:")
    if loc_min:
        for ind, num in loc_min:
            print(f"Индекс {ind}: {num}")
    else:
        print("Локальных минимумов нет")

    print("\nЛокальные максимумы:")
    if loc_max:
        for ind, num in loc_max:
            print(f"Индекс {ind}: {num}")
    else:
        print("Локальных максимумов нет")

    # Монотонность
    print("\n" + mono(lst, n))

    # Ввод K
    while True:
        try:
            k = int(input(f"\nВведите размер окна K (2-{n}): "))
            if not (2 <= k <= n):
                raise ValueError
            break
        except ValueError:
            print("Некорректный размер окна")

    # Скользящее среднее
    print("\nСкользящее среднее:")
    for start, end, value in avg(lst, k, n):
        print(f"Элементы {start}-{end}: {value:.2f}")

    # Самая длинная возрастающая последовательность
    longest = longest_increasing(lst)
    print("\nСамая длинная возрастающая последовательность:")
    print(*longest, sep=", ")
    print(f"Длина: {len(longest)}")

    # Ввод S
    while True:
        try:
            s = int(input("\nВведите число S: "))
            break
        except ValueError:
            print("Введите целое число")

    # Подсчёт пар
    pairs = count_pairs(lst, s)
    print(f"\nКоличество пар с суммой {s}: {pairs}")
