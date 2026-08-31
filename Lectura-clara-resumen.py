# Aguste de datos del usuario para una mejor lectura y comprension
# En esta practica se vera resumida la informacion presentada en palabras y consiente 

nombre = input("ingresa tu nombre: ").title()
apellido = input("ingresa tu apellido:").title()
peso = float(input("ingresa tu peso en kg: "))
estatura = float(input("ingresa tu estatura actual en metros:"))

# Con esto se muestra un orden limpio y organizado haciendo su lectura mas parcatica, ahora vamos en el imc

# Realizaremos una operacion mas rapida y limpia para obtenr el imc del usuario
# Con los datos anterios damos resultado

imc = peso / (estatura ** 2)

# Ahora con esta operacion podemos dar resultado pero agregaremos una condion de 2 desimales y dando uso al f-srings para una lectura clara

resumen = f"usuario: {nombre} {apellido} | imc:{imc:.2f}"

# Ahora vamos con el resultado de nuestra actividad
# Usaremos un contro de resumen para determinar el resultado

print("Resumen de datos")

print(resumen)


