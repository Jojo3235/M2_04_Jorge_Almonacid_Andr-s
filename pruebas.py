x=(2,3 ,3)
y=(3,3,3)
z=x+y
print(z)
colores_luz=[]
colores_luz.append("verde")
print(colores_luz)
solido=("s","o","l","i")
solido2=("d","o")
solido_total=solido+solido2
print(solido_total)
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
print(elemento1 in colores_luz)