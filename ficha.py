def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    NombreCompleto = input()
    nombresinespacio = NombreCompleto.strip().lstrip().rstrip().title()
    Email = input()
    nota1 = int(input())
    nota2 = int(input())
    nota3 = int(input())
    print("========================")
    print("    FICHA DEL ALUMNO")
    print("========================")
    print(f"Nombre: {nombresinespacio}".title())
    print(f"Email: {Email.strip().lower()}")
    caracteres = len(NombreCompleto.strip())
    print(f"Caracteres en nombre: {caracteres}")
    espacio = NombreCompleto.strip().find(" ")
    inicial1 = nombresinespacio[0]
    inicial2 = nombresinespacio[espacio+1]
    print(f"Iniciales: {inicial1}{inicial2}")
    apellido = NombreCompleto.strip()[espacio+1:]
    nombre = NombreCompleto.strip()[0:espacio]
    print(f"Usuario: {apellido.lower()}.{nombre.lower()}")
    contiene = "@" in Email
    print(f"Email valido: {contiene}")
    extraer = Email.find("@")
    extraido = Email[extraer+1:]
    print(f"Dominio: {extraido.lower()}")
    reemplazo = NombreCompleto.strip().replace(" ","_")
    print(f"Nombre para archivo: {reemplazo.title()}")
    contar = NombreCompleto.lower().count("a")
    print(f"Cantidad de a: {contar}")
    invertido = NombreCompleto.strip()[::-1]
    mayusculas = invertido.upper()
    print(f"Codigo secreto: {mayusculas}")
    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")
    suma = nota1 + nota2 + nota3
    print(f"Suma: {suma}")
    promedio = float(suma/3)
    print(f"Promedio: {promedio}")
    entero = int(suma/3)
    print(f"Promedio entero: {entero}")
    print(f"="*24)





    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)

