import random



def czyBije(tablica: list) -> False:
    """
    Funkcja sprawdza podaną tablicę na podstawie warunku |i - j| == |arr[i] - arr[j]|

    Args:
        tablica: Lista do sprawdzenia zawierająca współrzędne hetmanów.

    Returns: False, jeśli nie nastąpiło bicie hetmanów. W przeciwnym razie zwraca True

    """
    for i in range(0, len(tablica)):
        for j in range(i+1, len(tablica)):
            if tablica[i] == tablica[j]:
                print(f"Bicie!, i = {i + 1} oraz j = {j + 1}")
                return True
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


def generujpotomka1(n: int):
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


def generujpotomka(arr: [list], n: int):
    """
    Funkcja generuje permutacje podanej tablicy dwuwymiarowej od 0 do n.

    Args:
        arr: Tablica dwuwymiarowa, dla której generujemy permutacje.
        n: Granica wygenerowanych permutacji.

    Returns:

    """
    temp1 = []
    for i in range(0, n):
        temp = arr + [i]
        # arr.append(temp)
        temp1.append(temp)
    return temp1


if __name__ == '__main__':
    kolejka = []
    n = int(input("n="))
    for i in range(0, n):
        kolejka.append([i])
    print(kolejka)
    while len(kolejka) != 0:
        if len(kolejka[0]) == n:
            if not czyBije(kolejka[0]):
                print(f"Znaleziono rozwiązanie: {kolejka[0]}")
                break
            else:
                kolejka.pop(0)
        else:
            x = generujpotomka(kolejka[0], n)
            for i in range(0, len(x)):
                kolejka.append(x[i])
            kolejka.pop(0)


