#Ejercicio 1
from re import S


colores_luz = ["azul", "rojo", "verde"]         #Creamos una lista
sólidos_platónicos = ("tetraedro", "cubo", "octaedro", "dodecaedro", "icosaedro")       #Creamos una tupla

print("La lista contiene los siguientes elementos:",colores_luz)           #Imprimimos el contenido de la lista y la tupla
print("La tupla contiene los siguientes elementos",sólidos_platónicos,"\n")

print("El segundo elemento de la lista es:", colores_luz[1], "\nEl penúltimo elemento de la tupla es:", sólidos_platónicos[-2],"\n")
#Imprimimos el segundo elemento de la lista y el penúltimo de la tupla

colores_luz[2]="amarillo"   #Redefinimos el elemento en la posición 2
sólidos_platónicos=("esfera", "cubo", "octaedro", "dodecaedro", "icosaedro")    #Para cambiar un elemento de una tupla habría que redefinir esta
print(colores_luz)
print(sólidos_platónicos,"\n")

print("La longitud de la lista es de:",len(colores_luz))    #Imprimimos la longitud de la lista y la tupla
print("La longitud de la tupla es de:",len(sólidos_platónicos))

elemento1 = input("¿Qué elemento quieres buscar en la lista?: ")
if elemento1 in colores_luz:
    print(True,"\nEl elemento se encuentra en esta lista")          #Si el elemento1 está dentro de la lista nos devuelve True, en caso negativo nos devuelve False
else:
    print(False,"\nEl elemento no se encuentra en esta lista")

elemento2 = input("¿Qué elemento buscas?: ")
if elemento2 in sólidos_platónicos:
    print(True,"\nEl elemento se encuentra en esta tupla")          #Lo mismo que la lista pero en la tupla
else:
    print(False,"\nEl elemento no se encuentra en esta tupla\n")

colores_luz.append("verde")      #Añadimos un elemento nuevo a la lista
sólidos_platónicos_y_más=sólidos_platónicos + ("tetraedro", "patata")   #Para aádir elementos en una tupla tenemos que sumarle otra tupla 
print(colores_luz)
print(sólidos_platónicos_y_más)
tupla3=([3,4,2], 2)             #También podemos añadir elementos a una lista dentro de una tupla
tupla3[0].append(3)
print(tupla3,"\n")

#No podemos eliminar los elementos de una tupla
colores_luz.clear()             #Eliminamos todos los elementos de la lista
print("Estos son los elementos de la lista:", colores_luz)

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

#Ejercicio 3
lista_numeros=list()   #Creamos una lista vacía
i=0     #Creamos una variable y la igualamos a 0
while i<3:  #Mientras que la i sea menor que 3 se reitera el proceso
    i+=1   #Sumamos 1 cada vez que se repita el bucle
    numero1=float(input("Introduce un número: "))  #Pedimos que introduzca un número
    lista_numeros.append(numero1)  #Añadimos el número introducido a la lista
else:
    pass            #Cuando i = 3 decimos que pase el bucle 
sumatorio = sum(lista_numeros)      #Definimos la variable sumatorio como la suma de los términos de la lista
print("La suma de todos los números es",sumatorio)        #Imprimimos el sumatorio

#Ejercicio 4
media=sumatorio/len(lista_numeros)  #Creamos una función llamada media en la que dividimos la suma entra la longitud de la lista
print("La media de todos los números es",media)    #Imprimimos la media