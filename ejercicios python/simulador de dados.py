import random
count=0
def lanzar_dado():
    return random.randint(1, 6)

def main():
    global count
    while True:
        
        input("Presiona Enter para lanzar los dados...")
        resultado1= lanzar_dado()
        resultado2 = lanzar_dado()
        print(f"Has lanzado un {resultado2} y un {resultado1}!")
        count+=1
        if resultado1 == resultado2:
            print(f"los dados son iguales, Haz Ganado en {count} intentos!!")
            break
        else:
            continuar = input("¿Quieres lanzar de nuevo? (s/n): ").lower()
            if continuar != 's':
                
                break

if __name__ == "__main__":
    main()
