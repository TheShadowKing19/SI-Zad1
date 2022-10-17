import random
from tqdm import tqdm
# Funkcja ma generować taką tablice liczb, by nie było bicia


def sprawdzbicie():
    pass


def wygenerujtabele(n: int) -> list:
    """
    Funkcja generuje tabele n liczb losowych od (1,n).

    Args:
        n: Ilość liczb do wygenerowania

    Returns:
        Lista losowo wygenerowanych liczb od (1,n).
    """
    tablica = random.sample(range(1, n+1), n)
    print(tablica)
    sprawdzany_indeks = 0
    for i in range(0, len(tablica)):
        for j in range(0, len(tablica)):
            if i == j:
                continue
            elif abs(i - j) == abs(tablica[i] - tablica[j]):
                print(f"Bicie!, i = {i+1} oraz j = {j+1}")

    return tablica


if __name__ == '__main__':
    tablica = wygenerujtabele(5)


