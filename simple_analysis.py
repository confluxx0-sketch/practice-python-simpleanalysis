import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def round_to_hundreds(values):
    """Округляет числа до сотен по математическому правилу."""
    result = []
    for v in values:
        if v >= 0:
            result.append(int(math.floor(v / 100 + 0.5) * 100))
        else:
            result.append(int(math.ceil(v / 100 - 0.5) * 100))
    return result


def main():
    data = np.random.randint(-10000, 10001, 1000)
    series = pd.Series(data)

    print("Минимум:", series.min())
    print("Максимум:", series.max())
    print("Сумма:", series.sum())
    print("Стандартное отклонение:", series.std())

    counts = series.value_counts()
    print("Количество повторяющихся значений:", (counts > 1).sum())

    plt.figure()
    plt.plot(series.values)
    plt.title("Линейный график исходных данных")
    plt.xlabel("Индекс")
    plt.ylabel("Значение")
    plt.grid(True)

    rounded = round_to_hundreds(series.values)

    plt.figure()
    plt.hist(rounded, bins=50)
    plt.title("Гистограмма округленных значений")
    plt.xlabel("Значение")
    plt.ylabel("Частота")
    plt.grid(True)

    df = pd.DataFrame({"data": series})
    df["sorted_up"] = series.sort_values().reset_index(drop=True)
    df["sorted_down"] = series.sort_values(ascending=False).reset_index(drop=True)

    plt.figure()
    plt.plot(df["sorted_up"], label="По возрастанию")
    plt.plot(df["sorted_down"], label="По убыванию")
    plt.legend()
    plt.title("Отсортированные данные")
    plt.grid(True)

    plt.show()


if __name__ == "__main__":
    main()
