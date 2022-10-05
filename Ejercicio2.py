#Ejercicio 2
idiomas={"chino","inglés","español","francés"}
clases={
    "Álgebra": "Eduardo",
    "Análisis": "Alfredo",
    "Discreta": "Edgar",
    "Programación": "Rubén"
}

print(idiomas)
print(clases)

#No se puede mostrar un elemento de un set
print(clases["Álgebra"])

#No se pueden cambiar elementos de un set
clases["Álgebra"]= "Ed"
print(clases)

print(len(idiomas))
print(len(clases))

idiomas.add("alemán")
clases["Análisis II"]="Alfredo"
print(idiomas)
print(clases)

idiomas.clear()
print(idiomas)
clases.clear()
print(clases)