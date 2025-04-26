

def sumar(a: float, b: float)-> float:
    suma = a + b
    return suma

def multiplicar(a: float, b: float)-> float:
    multiplicacion = a * b
    return multiplicacion 

def dividir(a: float, b: float)-> float:
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    division = a / b
    return division

def resta(a: float, b: float)-> float:
    resta = a - b
    return resta

if __name__ == "__main__":
    print("Ejemplo de uso de las funciones:")
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    print(f"Suma: {sumar(a, b)}")
    print(f"Multiplicación: {multiplicar(a, b)}")
    print(f"División: {dividir(a, b)}")
    print(f"Resta: {resta(a, b)}")
    print("Fin del programa")
