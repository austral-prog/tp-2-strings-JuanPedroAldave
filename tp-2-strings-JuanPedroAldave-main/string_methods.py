def string_methods():
    """Demuestra el uso de métodos de string: strip, lstrip, rstrip, upper, lower,
    title, find, replace, count, operador in, slicing con paso, reverso,
    f-strings y strings multilínea.
    """
    nombre = "   Grace Hopper   "
    frase = "Python es un gran lenguaje de programacion"
    multilinea = """Linea 1
    Linea 2
    Linea 3"""
    strip = nombre.strip()
    rstrip = nombre.rstrip()
    lstrip = nombre.lstrip()
    upper = frase.upper()
    lower = frase.lower()
    title = frase.title()
    find = frase.find("gran")
    replace = frase.replace("programacion","desarrollo")
    count = frase.count("a")
    contienepython = "Python" in frase
    contienejava = "Java" in frase
    slice = frase[0:6]
    paso = slice[::2]
    reverso = slice[::-1]
    formato = f"{strip} sabe {slice}"
    print(f"Strip: {strip}")
    print(f"Lstrip: {lstrip}")
    print(f"Rstrip: {rstrip}")
    print(f"Upper: {upper}")
    print(f"Lower: {lower}")
    print(f"Title: {title}")
    print(f"Find: {find}")
    print(f"Replace: {replace}")
    print(f"Count: {count}")
    print(f"Contiene Python: {contienepython}")
    print(f"Contiene Java: {contienejava}")
    print(f"Slice: {slice}")
    print(f"Paso: {paso}")
    print(f"Reverso: {reverso}")
    print(f"Formato: {formato}")
    print(multilinea.replace("    ",""))
string_methods()

