def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """
    base = int(input())
    altura = int(input())
    print(f"Base: {base}")
    print(f"Altura: {altura}")
    area = base * altura
    perimetro = base*2 + altura*2
    print(f"Area: {area}")
    print(f"Perimetro: {perimetro}")
    pass
