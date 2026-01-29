caracteresNombre = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ._0123456789'
caracteresDominio = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.0123456789'
letras = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def leer_archivo(archivo):
    with open(archivo, "r", encoding="utf-8") as file:
        correos = file.readlines()
        for i, correo in enumerate(correos):
                print(f"Correo : {correo} : {verificar_correo(correo)}")

def verificar_correo(cadena):
    split_cadena = cadena.split('@')
    nombre = split_cadena[0]
    dominio = split_cadena[1].strip()
    print(split_cadena)
    if len(nombre) < 1 or len(dominio) < 1:
        return False
    if nombre[0] not in letras:
        return False
    for i in nombre:
        if i not in caracteresNombre:
            return False
    for i in dominio:
        if i not in caracteresDominio:
            return False
    if not verificar_puntos(dominio):
        return False
    return True
def verificar_puntos(dominio):
    if "." not in dominio:
        return False
    if dominio[0] == ".":
        return False
    if dominio[-1] == ".":
        return False
    for i, letra in enumerate(dominio):
        if dominio[i] == "." and dominio[i+1] == ".":
            return False
    return True

leer_archivo("correos.txt")