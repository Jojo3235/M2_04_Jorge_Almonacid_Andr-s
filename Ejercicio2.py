#Ejercicio 2
idiomas={"chino","inglés","español","francés"}      #Creamos un set y un diccionario
clases={
    "Álgebra": "Eduardo",
    "Análisis": "Alfredo",
    "Discreta": "Edgar",
    "Programación": "Rubén"
}

print(idiomas)                                  #Los imprimimos
print(clases)

#No se puede mostrar un elemento de un set
print(clases["Álgebra"])            #Decimos que nos imprima el valor asociado a la clave Álgebra

#No se pueden cambiar elementos de un set
clases["Álgebra"]= "Ed"         #Redefinimos el valor asociado a Álgebra y volvemos a imprimir el diccionario
print(clases)

print(len(idiomas))             #Imprimimos la longitud del set y del diccionario
print(len(clases))

idiomas.add("alemán")           #Agregamos un nuevo elemento al set
clases["Análisis II"]="Alfredo"         #Agregamos una nueva clave al diccionario con un valor asociado
print(idiomas)
print(clases)

idiomas.clear()             #Eliminamos todos los elementos del set
print(idiomas)
clases.clear()              #Eliminamos todos los elementos del diccionario
print(clases)