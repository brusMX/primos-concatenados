  #!/usr/bin/env python
from __future__ import print_function
lista_probados = []
lista_por_probar = [2,3,5,7]
j = 1

#TODO sustituir prueba de primalidad con una de verdad y rapida
def is_prime_number(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
	return False
    return True

print ("Empieza el ciclo")
primo = lista_por_probar[0]
print(str(primo) + ', ', end="")
while primo != None and lista_por_probar:
    for num in range(1,9):
        aux = int(str(num)+str(primo))
        if is_prime_number(int(aux)):
            lista_por_probar.append(aux)
            j=j+1
    lista_probados.append(primo)
    lista_por_probar.remove(primo)
    if not lista_por_probar:
        primo = None
    else:
        primo = lista_por_probar[0]
        print(str(aux) + ', ', end="")

print ("\nSe cierra el ciclo", end="\n")
print (str(j) + " primos encontrados")

print ("La lista de probados contiene " + str(len(lista_probados)) + " elemento(s)")
print("\nCOMIENZA")
for elem in lista_probados:
    print (str(elem) + "," , end="") 
print("\nFIN")
print ("La lista de probados contiene " + str(len(lista_por_probar)) + " elemento(s)")
for elem in lista_por_probar:
    print (str(elem) + "," , end="") 
