from timeit import default_timer as timer
import pandas as pd
import numpy as np
from IPython.display import display
import matplotlib.pyplot as plt
from queue import Queue


def czyBije(tablica: list) -> False:
    """
    Funkcja sprawdza podaną tablicę na podstawie warunku |i - j| == |arr[i] - arr[j]|, gdzie:
    i - indeks pierwszego sprawdzanego elementu
    j - indeks drugiego sprawdzanego elementu
    arr[i] - wartość pierwszego elementu
    arr[j] - wartość drugiego elementu

    Jeśli wartości po obu stronach równania się zgadzają, następuję bicię hetmanów. Jeśli są różne, nie ma bicia.

    Args:
        tablica: Lista do sprawdzenia zawierająca współrzędne hetmanów.

    Returns:
        False, jeśli nie nastąpiło bicie hetmanów. W przeciwnym razie zwraca True

    """
    for i in range(0, len(tablica)):
        for j in range(i + 1, len(tablica)):
            if tablica[i] == tablica[j]:
                # print(f"Bicie!, i = {i + 1} oraz j = {j + 1}")
                return True
            elif abs(i - j) == abs(tablica[i] - tablica[j]):
                # print(f"Bicie!, i = {i+1} oraz j = {j+1}")
                return True
    print(f"Brak bić dla tablicy {tablica}")
    return False


def generujpotomka(arr: [list], n: int) -> list[list]:
    """
    Funkcja generuje permutacje podanej tablicy dwuwymiarowej od 0 do n. Przykładowo, dla tablicy [0] i n = 4, funkcja
    wygeneruje permutacje: [0, 0], [0, 1], [0, 2], [0, 3].

    Args:
        arr: Tablica dwuwymiarowa, dla której generujemy permutacje.
        n: Granica wygenerowanych permutacji.

    Returns:
        Dwuwymiarowa lista permutacji.
    """
    temp1 = []
    for i in range(0, n):
        temp = arr + [i]
        temp1.append(temp)
    return temp1


def rozwiazNHetmanow(n: int) -> (int, int, int):
    """
    Funkcja służy do uruchomienia rozwiązywania problemu N-hetmanów.

    Args:
        n: Liczba określająca liczbę hetmanów na planszy oraz rozmiar szachownicy nxn.

    Returns:
          wygenerowanych (int): Liczba wygenerowanych potomków
          sprawdzonych (int): Liczba sprawdzonych stanów
          czas_wykonania (int): Czas wykonania zadania
    """
    start = timer()
    sprawdzonych = 0
    wygenerowanych = 0
    kolejka = []
    n = n
    for i in range(0, n):
        kolejka.append([i])
    while len(kolejka) != 0:
        if len(kolejka[0]) == n:
            if not czyBije(kolejka[0]):
                print(f"Znaleziono rozwiązanie: {kolejka[0]}")
                sprawdzonych += 1
                break
            else:
                kolejka.pop(0)
                sprawdzonych += 1
        else:
            x = generujpotomka(kolejka[0], n)
            wygenerowanych += n
            for i in range(0, len(x)):
                kolejka.append(x[i])
            kolejka.pop(0)
    end = timer()
    czas_wykonania = end - start
    return wygenerowanych, sprawdzonych, czas_wykonania
    # print(f"Wygenerowanych potomków: {wygenerowanych}")
    # print(f"Sprawdzonych stanów: {sprawdzonych}")
    # print(f"Czas wykonania: {end - start} s")


def rozwiazNHetmanow_kolejka(n: int) -> (int, int, int):
    """
    Funkcja służąca do uruchomienia rozwiązywania problemu N-hetmanów. Funkcja ta korzysta z Kolejek.

    Args:
        n: Liczba określająca liczbę hetmanów na planszy oraz rozmiar szachownicy nxn.

    Returns:
          wygenerowanych (int): Liczba wygenerowanych potomków
          sprawdzonych (int): Liczba sprawdzonych stanów
          czas_wykonania (int): Czas wykonania zadania
    """
    start = timer()
    sprawdzonych = 0
    wygenerowanych = 0
    kolejka = Queue(maxsize=0)
    n = n
    for i in range(0, n):
        kolejka.put([i])
    while not kolejka.empty():
        if len(kolejka.queue[0]) == n:
            if not czyBije(kolejka.queue[0]):
                print(f"Znaleziono rozwiązanie: {kolejka.queue[0]}")
                sprawdzonych += 1
                break
            else:
                kolejka.get()
                sprawdzonych += 1
        else:
            x = generujpotomka(kolejka.get(), n)
            wygenerowanych += n
            for i in range(0, len(x)):
                kolejka.put(x[i])

    end = timer()
    czas_wykonania = end - start
    return wygenerowanych, sprawdzonych, czas_wykonania
    # print(f"Wygenerowanych potomków: {wygenerowanych}")
    # print(f"Sprawdzonych stanów: {sprawdzonych}")
    # print(f"Czas wykonania: {czas_wykonania} s")


if __name__ == '__main__':
    n4_wygenerowanych, n4_sprawdzonych, n4_czas = rozwiazNHetmanow_kolejka(4)
    print()
    n5_wygenerowanych, n5_sprawdzonych, n5_czas = rozwiazNHetmanow_kolejka(5)
    print()
    n6_wygenerowanych, n6_sprawdzonych, n6_czas = rozwiazNHetmanow_kolejka(6)
    print()
    n7_wygenerowanych, n7_sprawdzonych, n7_czas = rozwiazNHetmanow_kolejka(7)

    wygenerowanych_wyniki = [n4_wygenerowanych, n5_wygenerowanych, n6_wygenerowanych, n7_wygenerowanych]
    sprawdzonych_wyniki = [n4_sprawdzonych, n5_sprawdzonych, n6_sprawdzonych, n7_sprawdzonych]
    czas_wyniki = [n4_czas, n5_czas, n6_czas, n7_czas]
    n = [4, 5, 6, 7]
    wyniki = np.array([(n4_wygenerowanych, n4_sprawdzonych, n4_czas),
                       (n5_wygenerowanych, n5_sprawdzonych, n5_czas),
                       (n6_wygenerowanych, n6_sprawdzonych, n6_czas),
                       (n7_wygenerowanych, n7_sprawdzonych, n7_czas)])
    df = pd.DataFrame(wyniki,
                      columns=['Wygenerowanych potomków',
                               'Sprawdzonych stanów',
                               'Czas wykonania [s]'],
                      index=['n = 4', 'n = 5', 'n = 6', 'n = 7']
                      )
    display(df)

    xticks = np.arange(4, 7+1)
    plt.plot(n, wygenerowanych_wyniki)
    plt.plot(n, sprawdzonych_wyniki)
    plt.plot(n, czas_wyniki)
    plt.legend(['Wygenerowanych potomków', 'Sprawdzonych stanów', 'Czas wykonania [s]'])
    plt.title("n-hetmanów BFS")
    plt.xlabel("n (x10^6)")
    plt.xticks(xticks)
    plt.show()

