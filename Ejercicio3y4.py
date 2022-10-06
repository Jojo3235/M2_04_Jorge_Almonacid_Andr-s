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