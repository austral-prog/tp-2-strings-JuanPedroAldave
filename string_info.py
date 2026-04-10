def string_info():
    """Dada la palabra 'Programacion', imprime su longitud, primera y última letra,
    la palabra repetida 3 veces y decorada con '***'.
    """
    palabra = "Programacion"
    print(f"Palabra: {palabra}")
    longitud = len(palabra)
    print(f"Longitud: {longitud}")
    primerletra = palabra[0]
    print(f"Primera letra: {primerletra}")
    ultimaletra = palabra[-1]
    print(f"Ultima letra: {ultimaletra}")
    palabrarepetida = palabra*3
    print(f"Repetida: {palabrarepetida}")
    decoracion = "***"
    palabradecorada = decoracion + palabra + decoracion
    print(f"Decorada: {palabradecorada}")
