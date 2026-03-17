braille = {
    "a": "⠁", "b": "⠃", "c": "⠉", "d": "⠙", "e": "⠑",
    "f": "⠋", "g": "⠛", "h": "⠓", "i": "⠊", "j": "⠚",
    "k": "⠅", "l": "⠇", "m": "⠍", "n": "⠝", "o": "⠕",
    "p": "⠏", "q": "⠟", "r": "⠗", "s": "⠎", "t": "⠞",
    "u": "⠥", "v": "⠧", "w": "⠺", "x": "⠭", "y": "⠽",
    "z": "⠵",

    "1": "⠼⠁", "2": "⠼⠃", "3": "⠼⠉",
    "4": "⠼⠙", "5": "⠼⠑", "6": "⠼⠋",
    "7": "⠼⠛", "8": "⠼⠓", "9": "⠼⠊",
    "0": "⠼⠚",

    " ": " "
}
# La nueva funcion agregada sirve para avisar caracteres no soportados
def verificar_caracteres(texto, diccionario):
    errores = [c for c in texto if c not in diccionario]
    if errores:
        print("Atención: Los siguientes caracteres no tienen traducción en Braille:", errores)

palabra = input("Ingrese el texto a traducir: ").lower() #pedimos la palbra
#y pasamos todo a minuscula

# Llamamos la nueva función
verificar_caracteres(palabra, braille)

textoTraducido = "" #aqui guardamos el texto en braile

for caracter in palabra:
    if caracter in braille:
         textoTraducido += braille[caracter]
    else :
         continue


print (textoTraducido)
archivo = open("braille.txt", "w", encoding="utf-8")
archivo.write(textoTraducido)
archivo.close()