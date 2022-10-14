import random
# Funkcja ma generować taką tablice liczb, by nie było bicia

def wygenerujtabele(n: int) -> list:
    """
    Funkcja generuje tabele n liczb losowych od (1,n).

    Args:
        n: Ilość liczb do wygenerowania

    Returns:
        Lista losowo wygenerowanych liczb od (1,n).
    """
    tablica = random.sample(range(1, n+1), n)
    return tablica


if __name__ == '__main__':
    tablica = wygenerujtabele(5)
    print(tablica)

