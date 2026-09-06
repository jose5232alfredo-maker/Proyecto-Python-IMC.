# comienza el proyecto final dando conclusion a este aprendizaje 

# Se implentaran codigos y escrituras evitando dejar espacios en error o vacios

def obtener_texto(mensaje):
    "solicitar y validar informacion que no quede vacio"
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto.title()
        print("Error: No se permite dejar el campo vacio. Por favor, ingrese los datos correctamente.")
        
# Se implemete el uso d edatos numericos sin dejar espacios en error o vacios
        
def obtener_numero(mensaje):
    "solicitar y validar los numeros y no quedar en vacio"
    while True:
        entrada = input(mensaje).strip()
        
        if not entrada:
            print("Error: No se permite dejar el campo vacio. Por favor, ingrese el numero correctaamente.")
            continue 
        
        try:
            valor = float(entrada)
            if valor <= 0:
                print("Error: El numero debe ser mayor a cero. Ingrese nuevamente el dato.")
                continue
            return valor
        except ValueError:
                print("Error: Ingrese un numero valido. Por favr intente nuevamente.")
    
def main():
    print("Calculacion de IMC (Indice de Masa Corporal)")
    print("Bienvenido por favor ingresa los datos solicitados:")
    
    # Ahora ingresamos datos personales 
    
    nombre = input("ingresa tu nombre: ").strip()
    apellidos = input("ingresa tus apellidos : ").strip()
    
    # Damos los datos numericos numericos y correspondientes 
    
    edad = obtener_numero("ingresa tu edad en años: ")
    peso = obtener_numero("ingresa tu peso en kilogramos: ")
    altura = obtener_numero("ingresa tu altura en metros: ")
    
    # Ahora usaremos los datos registrados para calcular correctamente el imc
    
    imc = peso / (altura ** 2)
    
    # Ahora con los datos obtenidos seran mostrados
    
    print("\n-- Resumen de los datos --")
    print(f"Nombre: {nombre}")
    print(f"Apellidos: {apellidos}")
    print(f"Edad: {edad} años")
    print(f"Peso: {peso} kg")
    print(f"Altura: {altura} m")
    print(f"IMC: {imc:.2f}")

if __name__ == "__main__":
    main()
    
    
    