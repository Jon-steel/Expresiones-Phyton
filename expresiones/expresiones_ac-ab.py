import re
expresion = r'^ac|ab$'
resultado = re.compile(expresion)
prueba = raw_input("Entrada: ")
busqueda = re.search(resultado,prueba)
if busqueda:
    print busqueda.group()
else:
    print"qR"


