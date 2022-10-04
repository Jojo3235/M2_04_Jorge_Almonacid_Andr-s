#Ejercicio 1
from re import S


colores_luz = ["azul", "rojo", "verde"]
sólidos_platónicos = ("tetraedro", "cubo", "octaedro", "dodecaedro", "icosaedro")

print("La lista contiene los siguientes elementos:",colores_luz)
print("La tupla contiene los siguientes elementos",sólidos_platónicos,"\n")

print("El primer elemento de la lista es:", colores_luz[1], "\nEl penúltimo elemento de la tupla es:", sólidos_platónicos[-2],"\n")

colores_luz[2]="amarillo"
sólidos_platónicos=("esfera", "cubo", "octaedro", "dodecaedro", "icosaedro")        #Para cambiar un elemento de una tupla es necesario redefinir esta
print(colores_luz)
print(sólidos_platónicos,"\n")

print("La longitud de la lista es de:",len(colores_luz))
print("La longitud de la tupla es de:",len(sólidos_platónicos))

elemento1 = input("¿Qué elemento quieres buscar en la lista?: ")
if elemento1 in colores_luz:
    print(True,"\nEl elemento se encuentra en esta lista")
else:
    print(False,"\nEl elemento no se encuentra en esta lista")

elemento2 = input("¿Qué elemento buscas?: ")
if elemento2 in sólidos_platónicos:
    print(True,"\nEl elemento se encuentra en esta tupla")
else:
    print(False,"\nEl elemento no se encuentra en esta tupla\n")

colores_luz.append("verde") 
sólidos_platónicos_y_más=sólidos_platónicos + ("tetraedro", "patata")
print(colores_luz)
print(sólidos_platónicos_y_más)
tupla3=([3,4,2], 2)
tupla3[0].append(3)
print(tupla3,"\n")


colores_luz.clear()
print("Estos son los elementos de la lista:", colores_luz)