

import turtle


winwow = turtle.Screen()
Gero = turtle.Turtle()
Gero.forward(50)
Gero.left(90)
Gero.forward(50)
Gero.left(90)
Gero.forward(50)
Gero.left(90)
Gero.forward(50)
Gero.left(90)

turtle.mainloop()

name = str(input('Cual es tu nombre?'))
print('Hola, ' + name + '!')

cuadrado con funciones
--------------------------------------------------------------------------------
import turtle



def main():
    window = turtle.Screen()
    Gero = turtle.Turtle()
    make_square(Gero)

def make_square(Gero):
    length = int(input('tamaño de cuadro: '))
    
    for i in range(4):
         make_line_and_turn(Gero, length)


def make_line_and_turn(Gero, length):
    Gero.forward(length)
    Gero.left(90)


if __name__ == '__main__':
    main()


turtle.mainloop()    


------------------------------------------------------------------

suma de 2 numeros

numero1 = int(input('introduce un numero'))
numero2 = int(input('introduce otro numero'))

numero1= int(numero1)
numero2= int(numero2)

resultado = numero1 + numero2 
 
print('el resultado de la suma de esos numeros es ' + str(resultado))

Bot

print('BOT de diagnostico medico')
print('HOLA! soy Keno-bi')
print('te hare una encuesta y vas poniendo tus sintomas')
print('elige el numero de el sintoma')
print('todo listo? COMENCEMOS!!')


------------------------------------------------------------------

name = str(input('dime tu nombre'))
year =  int(input('hola ' + name + ' dime tu edad'))

if (year <= 13):
	print("todavia eres un niño :D")



if (year > 13):
	if (year <= 17):
       	 print("eres un adolecente")



if (year > 17):
    print("eres un adulto felicidades")  

input()

------------------------------------------------------------------

print("--------calculadora de divisas--------")
print("pesos mexicanos y colombianos")

E = int(input("ingresa 1 si quieres pesos COL a MEX y 2 de MEX a COL"))

if(E == 1):
    pcol = int(input("dime la cantidad de pesos colombianos")) 
    resultado = pcol * 0.0057
    print("el resultado de tu calculo es " + str(resultado))
if(E == 2):
    pmew = float(input("dime la cantidad de pesos mexicanos"))
    resultado = pmew * 176.54 
    print("el resultado de tu calculo es " + str(resultado))


-----ejercicio 1 resulto---------------------------------------
print("repaso de python")

name = str(input("HOLA!! dime tu nombre"))
year = int(input('hola ' + name + ' dime  tu edad'))

print('tu nombre es ' + name + ' y tu edad es ' + str(year))
--------------------------------------------------------------

-----ejercicio 7 resulto----------------------------------------
print("votacion")
years = int(input("Digite su edad"))
sex = int(input("digite 1 para masculino 2 para femenino"))

if (years > 17):     
    if (sex == 1):
        print("felicidades arriba el patriarcado puedes votar")
    if (sex == 2):
        print("Nel pastel no vas a votar mujer")
        
        
if (years < 17):
    print("largate de aqui niño")
---------------------------------------------------------	
numA =  int(input('dime el primer numero'))
numB =  int(input('dime el segundo numero'))
numC =  int(input('dime el tercer numero'))

if (numA > numB):
    if (numA > numC):
        print('el numero mayor es ' + str(numA))


if (numB > numC):
    if(numB > numC):
        print('el numero mayor es ' + str(numB))


else:
    print('el numero mayor es ' + str(numC))

----------------------------------------------------------
numA =  int(input('dime el Day'))
numB =  int(input('dime el Month'))
numC =  int(input('dime el year'))

if (numA < 32):
    if (numB < 13):
        if(numC < 0):
            print('la fecha es ' + str(numA) +'/'+str(numB)+'/'+str(numC))



else:
    print('esa fecha es imposibleee')
