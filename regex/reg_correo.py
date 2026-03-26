import re

"""
usuario = r"[a-zA-Z]+([a-zA-Z\_\.])+"
dominio = r"[a-zA-Z\d]+(\.[a-zA-Z\d]+)+"
patron_correo = usuario + r"@" + dominio

prueba = "Ma___.dfjkq@hotakld.dfq.eqe.de"
if re.fullmatch(patron_correo, prueba):
    print("El correo es valido")
else:
    print("El correo es invalido")

"""

"""
========================================================
                   RUTAS DE ARCHIVO
========================================================
"""
prueba = "C:\\usuarios\\documentos"
directorios = r"(\\[a-zA-Z]+\s+[a-zA-Z]+)+"
patron_ruta = r"C:" + r"(\\[a-zA-Z]+\s+[a-zA-Z]+)+" + r"[a-zA-Z]+\.[a-zA-Z]+|[a-zA-Z]+\.[a-zA-Z]+"
if re.fullmatch(patron_ruta, prueba):
    print("La ruta es valida")
else:
    print("La ruta es invalida")





