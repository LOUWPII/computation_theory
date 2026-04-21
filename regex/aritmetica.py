import re

#(Entero o float) (+ o -) (entero o float)
patron = r"(\d+\.?\d*)([\+\-])(\d+\.?\d*)"

try:
    with open("expresiones.txt", "r") as archivo:
        for linea in archivo:
            #Se quita el \n
            linea = linea.strip()
            #Se verifica si el patron coincide
            match = re.search(patron, linea)
            if match:
                #Se asigna el operando 1, el operador y el operando 2
                #Le hcamemos un cast al n1 y al n2
                n1, op, n2 = float(match.group(1)), match.group(2), float(match.group(3))
                
                resultado = n1 + n2 if op == "+" else n1 - n2
                print(f"{linea} = {resultado}")
            else:
                print(f"Línea inválida: {linea}")
except FileNotFoundError:
    print("no existe archio")
