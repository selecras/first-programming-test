from random import randint
from statistics import median


def create_matrix(n: int, mode: int) -> list[list[int]]:
    if not (3 <= n <= 15):
        raise ValueError("Некорректный размер матрицы")

    if mode == 1:
        return [
            [randint(-20, 20) for _ in range(n)]
            for _ in range(n)
        ]
    elif mode == 2:
        return [
            [(i + 1) * (j + 1) - n for j in range(n)]
            for i in range(n)
        ]
    else:
        raise ValueError("Некорректный способ заполнения")


def print_matrix(matrix: list[list[int]]) -> None:
    for row in matrix:
        for num in row:
            print(f"{num:6}", end="")
        print()


def diagonal_sums(matrix: list[list[int]]) -> tuple[int, int]:
    n = len(matrix)

    main_sum = sum(matrix[i][i] for i in range(n))
    side_sum = sum(matrix[i][n - 1 - i] for i in range(n))

    return main_sum, side_sum


def min_max_matrix(matrix: list[list[int]]) -> tuple:
    n = len(matrix)

    min_value = matrix[0][0]
    max_value = matrix[0][0]
    min_index = (0, 0)
    max_index = (0, 0)

    for i in range(n):
        for j in range(n):
            if matrix[i][j] < min_value:
                min_value = matrix[i][j]
                min_index = (i, j)

            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
                max_index = (i, j)

    return min_value, min_index, max_value, max_index


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    n = len(matrix)

    return [
        [matrix[j][i] for j in range(n)]
        for i in range(n)
    ]


def upper_lower_sums(matrix: list[list[int]]) -> tuple[int, int]:
    n = len(matrix)
    upper = 0
    lower = 0

    for i in range(n):
        for j in range(n):
            if j > i:
                upper += matrix[i][j]
            elif j < i:
                lower += matrix[i][j]

    return upper, lower


def matrix_median(matrix: list[list[int]]) -> tuple[list[int], float]:
    numbers = []

    for row in matrix:
        numbers.extend(row)

    numbers.sort()

    return numbers, median(numbers)


def is_symmetric(matrix: list[list[int]]) -> bool:
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != matrix[j][i]:
                return False

    return True


def matrix_square(matrix: list[list[int]]) -> list[list[int]]:
    n = len(matrix)
    result = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix[i][k] * matrix[k][j]

    return result


if __name__ == "__main__":
    # Ввод размера матрицы
    while True:
        try:
            n = int(input("Введите размер матрицы N (3-15): "))
            if not (3 <= n <= 15):
                raise ValueError
            break
        except ValueError:
            print("Некорректный ввод")

    # Выбор способа заполнения
    print("\nСпособ заполнения матрицы:")
    print("1. Случайные числа от -20 до 20")
    print("2. По формуле")

    while True:
        try:
            mode = int(input("Выберите способ (1-2): "))
            if mode not in (1, 2):
                raise ValueError
            break
        except ValueError:
            print("Некорректный ввод")

    matrix = create_matrix(n, mode)

    # Исходная матрица
    print("\nИсходная матрица:")
    print_matrix(matrix)

    # Суммы диагоналей
    main_sum, side_sum = diagonal_sums(matrix)

    print("\nСуммы диагоналей:")
    print(f"Главная диагональ: {main_sum}")
    print(f"Побочная диагональ: {side_sum}")

    # Минимум и максимум
    min_val, min_ind, max_val, max_ind = min_max_matrix(matrix)

    print("\nМинимальный элемент:")
    print(f"Значение: {min_val}, индекс: {min_ind}")

    print("\nМаксимальный элемент:")
    print(f"Значение: {max_val}, индекс: {max_ind}")

    # Транспонирование
    print("\nТранспонированная матрица:")
    transposed = transpose(matrix)
    print_matrix(transposed)

    # Суммы выше и ниже диагонали
    upper, lower = upper_lower_sums(matrix)

    print("\nСуммы элементов относительно главной диагонали:")
    print(f"Выше диагонали: {upper}")
    print(f"Ниже диагонали: {lower}")

    # Сортировка и медиана
    numbers, med = matrix_median(matrix)

    print("\nОтсортированные элементы матрицы:")
    print(*numbers, sep=", ")
    print(f"\nМедиана: {med:.2f}")

    # Проверка симметричности
    print("\nПроверка симметричности:")

    if is_symmetric(matrix):
        print("Матрица симметрична")
    else:
        print("Матрица несимметрична")

    # Возведение матрицы в квадрат
    print("\nМатрица в квадрате:")
    squared = matrix_square(matrix)
    print_matrix(squared)

