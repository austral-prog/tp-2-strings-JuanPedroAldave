def ficha():

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
