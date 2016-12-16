#!/usr/bin/env python
# pylint: disable-msg=C0103
from __future__ import print_function
with open('primos.txt', 'w') as f1:
#Lista de primos que ya sabemos primos de un digito para generar la lista al vuelo de los siguientes
    lista_por_probar = [2, 3, 5, 7]
    def is_prime_number(n):
        """Returns True if n is prime."""
        if n == 2:
            return True
        if n == 3:
            return True
        if n % 2 == 0:
            return False
        if n % 3 == 0:
            return False

        i = 5
        w = 2

        while i * i <= n:
            if n % i == 0:
                return False

            i += w
            w = 6 - w

        return True
    indice = 0
    cant_primos = 1
    #Optimizacion para no recorrer el arreglo  siempre para contar los elementos
    tam_arreglo = len(lista_por_probar)
    print ("Empieza el ciclo", file=f1)
    primo = lista_por_probar[indice]
    print(str(primo), end="\n", file=f1)
    while indice <= tam_arreglo:
        for num in range(1, 9):
            aux = int(str(num)+str(primo))
            if is_prime_number(int(aux)):
                lista_por_probar.append(aux)
                print(str(aux), end="\n", file=f1)
                cant_primos = cant_primos +1
                tam_arreglo = tam_arreglo + 1
                if tam_arreglo % 10 == 0:
                    print("Llevas "+str(tam_arreglo)+ " primos")
        indice = indice + 1
        if indice <= tam_arreglo - 1:
            primo = lista_por_probar[indice]
            print(str(primo), end="\n", file=f1)
    print ("Se cierra el ciclo", end="\n", file=f1)
    print ("La lista de primos por probar contiene " + str(len(lista_por_probar)) + " elemento(s)")
    for elem in lista_por_probar:
        print (str(elem)+ ",", end="")
