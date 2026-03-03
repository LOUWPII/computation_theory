import re


def validar_correo_pro(correo):
    # EXPLICACIÓN DEL PATRÓN:
    # ^[a-zA-Z]          -> Obliga a empezar con una letra.
    # [a-zA-Z\d._]* -> Permite letras, dígitos, puntos o _ (0 o más veces).
    # @                  -> Símbolo arroba.
    # [a-zA-Z\d]+        -> Primera parte del dominio (letras/números, al menos uno).
    # (\.[a-zA-Z\d]+)+   -> Obliga a al menos un punto, seguido de letras/números.
    #                       Esto evita puntos seguidos y puntos al final.

    patron = r"^[a-zA-Z][a-zA-Z\d._]*@[a-zA-Z\d]+(\.[a-zA-Z\d]+)+$"

    if re.fullmatch(patron, correo):
        return True
    else:
        return False

def validar_ruta(ruta):
    patron = r"^[a-zA-Z]:\\([a-zA-Z0-9\s._-]+\\)*[a-zA-Z0-9\s._-]+(\.[a-zA-Z0-9]+)?$"
    if re.fullmatch(patron, ruta):
        return True
    else:
        return False



# --- Casos de prueba ---
test_emails = [
    "g.emini_2026@google.com",  # Válido (empieza letra, tiene . _ y números)
    "a1@u2.edu.co",  # Válido (mínima expresión con números)
    "1user@gmail.com",  # Inválido (empieza por número)
    "_admin@empresa.com",  # Inválido (empieza por underscore)
    "user@dominio..com",  # Inválido (puntos adyacentes)
    "usuario@99.com"  # Válido (dominio con números)
]

print(f"{'Correo':<25} | {'¿Válido?'}")
print("-" * 40)
for email in test_emails:
    res = "✅ SÍ" if validar_correo_pro(email) else "❌ NO"
    print(f"{email:<25} | {res}")

test_rutas = [
    r"C:\Users\Invitado\LICENSE",      # SIN extensión -> OK
    r"D:\Musica\pista01.mp3",         # CON extensión -> OK
    r"E:\backup\\",                     # En la raíz sin extensión -> OK
    r"C:\Windows\System32\drivers\etc\hosts" # Ruta larga sin extensión -> OK
]

for r in test_rutas:
    if validar_ruta(r):
        print(f"VALOR: {r} -> ✅ ACEPTADA")
    else:
        print(f"VALOR: {r} -> ❌ RECHAZADA")
