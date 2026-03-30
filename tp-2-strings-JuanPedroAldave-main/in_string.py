def check_vowels():
    """Lee un nombre y verifica si contiene cada una de las vocales (a, e, i, o, u),
    sin distinguir mayúsculas de minúsculas.
    """
    nombre = input().lower()
    A = "a" in nombre
    E = "e" in nombre
    I = "i" in nombre
    O = "o" in nombre
    U = "u" in nombre
    print(f"Contiene a: {A}")
    print(f"Contiene e: {E}")
    print(f"Contiene i: {I}")
    print(f"Contiene o: {O}")
    print(f"Contiene u: {U}")

    pass
