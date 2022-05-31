#Declaramos una variable
from errno import EADDRNOTAVAIL


calificacion = input("Introduce tu calificacion del AZ-900: ")

calificacion = int(calificacion)

#pregutamos si la calificacion es menor a 700
if calificacion < 700 : 
    print("Eso te pasa por no estudiar") #si es menor a 700, muestra lo siguiente
elif calificacion > 1000 :
    print("Mientes, no puedes sacar mas de mil")
else : #si el if no se cumple, pasa a esta linea
    print("Felicidades pasa por tu certificado") # se ejecuta si ninguno de los if se cumple


#verificador de edad
edad = input("Introduce tu edad: ")
edad = int(edad)

if edad >= 18 and edad <= 100 :
    print("Bienvenido xd")
elif edad > 100 :
    print("Si vienes acompañado de sus abuelitos, si te podemos fiar")
elif edad < 0 :
    print("Ni que fuera viajero del tiempo")
else :
    print("No puedes llevarte cigarrillos")