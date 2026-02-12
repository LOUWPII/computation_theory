s = 'automata'

for char in s:
    print(char)

for i, simbolo in enumerate(s):
    print(f"en la posicion {i} la letra {simbolo}")

def procesar(caracter):
    return f"<<{caracter}>>"
resultado = list(map(procesar, s))
print(resultado)


i = 0
while i < len(s):
    print(s[i])
    i += 1  # Tú controlas el avance

print(s[-3:])

"""
s[::k]: Toda la cadena con un salto de k.

s[i::k]: Empieza en i, va hasta el final con salto k.

s[:j:k]: Desde el inicio hasta j con salto k.

s[i:j:k]: Desde i hasta j con salto k.

"""
"""
s[-1]: El último carácter.

s[-k:]: Los últimos k caracteres (el sufijo).

s[:-k]: Todo excepto los últimos k caracteres.

s[-k:-m]: Rango usando posiciones relativas al final.
"""

"""
s[::-1]: Invierte la cadena completa

s[::-2]: Invierte y salta uno.

s[j:i:-1]: Recorre desde j hasta i (hacia atrás).
"""
