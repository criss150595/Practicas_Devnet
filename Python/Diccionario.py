numerosingles = {
    "Uno" : "One",
    "Dos" : "Two",
    "Tres" : "Three",
    "Cuatro" : "Four",
    "Cinco" : "Five"}



print("Diccionario original: ",numerosingles)
diccionariocopia = numerosingles.copy()
print("Diccionario copia: ",diccionariocopia)
diccionariocopia.clear()
print("Diccionario copia después del clear: ",diccionariocopia)
print("Valor del cuatro (pop): ", numerosingles.pop("Cuatro"))
print("Diccionario después del pop: ",numerosingles)
print("Elemento al azar con popitem: ", numerosingles.popitem())
print("Diccionario después del popitem: ",numerosingles)