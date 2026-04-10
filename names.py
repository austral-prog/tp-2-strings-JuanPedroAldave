def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    Nombre = input("Ingrese el nombre: ")
    Apellido = input("Ingrese el apellido: ")
    texto1 = f"{Nombre} {Apellido}"
    print(texto1.lower())
    print(texto1.title())
    print(texto1.upper())
    print("\t"+texto1.lower())
    pass
names()
