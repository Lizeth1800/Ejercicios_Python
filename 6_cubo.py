import math
def seis():
    suma=0
    cad=""
    n = int(input("n numeros para elevar al cubo: "))
    for q in range(1,n+1):
        C=pow(q,3)
        cad=cad+" "+str(C)
        suma+=C
    print(cad)
<<<<<<< HEAD
    print("La suma de cubos es: ", suma)
=======
    print("La suma de los cubos es: ", suma)
>>>>>>> 479628175fa9e9b9b0347b2320615300cbee6f7b
seis()
