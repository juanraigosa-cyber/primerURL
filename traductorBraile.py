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

palabra = input("Ingrese el texto a traducir: ").lower() #pedimos la palbra
#y pasamos todo a minuscula

textoTraducido = "" #aqui guardamos el texto en braile

for caracter in palabra:
    if caracter in braille:
         textoTraducido += braille[caracter]
    else :
         print ("no pudimos traducir")


print (textoTraducido)
