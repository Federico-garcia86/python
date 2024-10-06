numero1 = float(input("Ingresar un numero para la operacion: "))
numero2 = float(input("Ingresar el segundo numero para la operacion que sea distinto de 0 si es divicion:"))
operacion = input("Ingresar la operacion que desea realizar +,-,/ o *:")

match operacion:
    case "+":
        resultado = numero1 + numero2
    case "-":
        resultado = numero1 - numero2
    case "/":
        if numero2 == 0:
            print(f"no tiene resultado al ser dividido por {numero2}")
        else:
            resultado = numero1 / numero2
    case "*":
        resultado = numero1 * numero2
    case _:
        print("Esa operacion es erronea")

# Imprimir el resultado solo si fue calculado (es decir, no es división por cero)
if operacion == "/" and numero2 == 0:
    pass  # No hacer nada, el mensaje de error ya fue impreso
else:
    print(f"el resultado de {numero1} {operacion} {numero2}={resultado}")