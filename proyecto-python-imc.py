# Calculo de imc con datos del usuario
    # Aqui vamos a agrgar los valores del alumno 
edad = int(input("ingrese la edad: ")) # 24 años 
peso = float(input("ingrese el peso en kilogramos: ")) # 95 aproximadamente
estatura = float(input("ingrese la estatura en metros: ")) # 1.68 normalmente 

# Ahora prepararemos la formula para calcular el imc del alumno
    # Usaremos la formula estandar de peso / estatura esta multimplicada por si misma

imc = peso / (estatura**2)

# Ahora pediremos que exprese el resultado

print(f"Resultado")
print(f"Edad: {edad} años")
print(f"Tu indice de masa corporal es (IMC) es: {imc:.2f}")


