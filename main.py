import random
from tqdm import tqdm
# Funkcja ma generować taką tablice liczb, by nie było bicia


def sprawdzbicie(tablica: list) -> False:
    """
    Funkcja sprawdza podaną tablicę na podstawie warunku |i - j| == |arr[i] - arr[j]|

    Args:
        tablica: Lista do sprawdzenia zawierająca współrzędne hetmanów.

    Returns: False, jeśli nie nastąpiło bicie hetmanów. W przeciwnym razie zwraca True

    """
    for i in tqdm(range(0, len(tablica))):
        for j in range(i, len(tablica)):
            if i == j:
                continue
            elif abs(i - j) == abs(tablica[i] - tablica[j]):
                print(f"Bicie!, i = {i+1} oraz j = {j+1}")
                return True
    print(f"Brak bić dla tablicy {tablica}")
    return False


def wygenerujtabele(n: int) -> list:
    """
    Funkcja generuje tabele n liczb losowych od (1,n) bez powtórzeń.

    Args:
        n: Ilość liczb do wygenerowania oraz max

    Returns:
        Lista losowo wygenerowanych liczb od (1,n) bez powtórzeń.
    """
    tablica = random.sample(range(1, n+1), n)
    return tablica


def generujpotomka(n: int):
    """

    Args:
        ojciec:
        n:

    Returns:

    """

    do_przeszukania = []
    do_przeszukania.append([])
    temp = []
    for i in range(0, n):
        do_przeszukania.append([i])
        temp = []
        temp.append(i)
        for j in range(0, n):
            temp.append(j)
            do_przeszukania.append(temp)
            temp = temp[:len(temp)-1]
    print(do_przeszukania)


if __name__ == '__main__':
   generujpotomka(4)


