def invertirCadena(cadena):
    invertida=""
    for caracter in cadena:
        invertida=caracter+invertida
        print(invertida)
    return invertida
print(invertirCadena(invertirCadena("hola mundo")))
