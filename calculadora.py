print("Hola si soy la calculadora que calcula calculadamente todos los calculos que hayan que calcular.")
print(" ")
print("Porfa digame que operación necesita realizar. En caso de una suma, presione 1, en caso de una resta, pulse 2, si se trata de una división, presione 3. En caso de una multiplicación, presione 4")
print(" ")
Operacion = input("Digite su opción seleccionada: ")



def sumar():
    x = float(input("Digite el primer numero a sumar: "))

    y = float(input("Digite el segundo numero a sumar: "))

    resultado = x + y


    print("El resultado es: " + str(resultado))

def restar():
    x = float(input("Digite el primer numero a restar: "))

    y = float(input("Ahora el segundo: "))

    resultado = x - y

    print("Su resultado es: " + str(resultado)) 

def division():
    x = float(input("Digame cual es el dividendo: "))

    y = float(input("Ahora digame el divisor: "))

    if y == 0:
        while y == 0:
            print("Epa papi, eso no se puede, dividir por 0 es imposible y puede tener consecuencias nefastas en este nuestro plano de la realidad")

            y = float(input("Pruebe otra vez: "))

            if y != 0:
                break
    
    resultado = x / y

    print("Su resultado es: " + str(resultado))

def multiplicar ():
    x = float(input("Multiplicador: "))

    y = float(input("Multiplo"))

    resultado = x * y
    
    print("Su resultado es: " + str(resultado))

match Operacion:
    case "1":
        sumar()
    case "2":
        restar()
    case "3":
        division()
    case "4":
        multiplicar()
    

