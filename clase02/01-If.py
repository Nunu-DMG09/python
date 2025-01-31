###
# SENTENCIAS CONDICIONALES (IF - ELSE - ELIF)
# Permiten ejecutar bloques de codigo si se cumplen ciertas condiciones 
###

import os # IMPORTAR MODULOS DEL SISTEMA OPERATIVO
os.system("clear")  


print("\n Sentencia simple condicional")
edad = 19
if edad >= 18:
    print("Eres mayor de edad")



print("\n Sentencia condicional con ELSE")
edad = 15
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")



print("\n Sentencia condicional con ELIF")
nota = 9
if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Bueno")
elif nota >= 5:
    print("Regular")
else:
    print("Reprobaste")



print("\n Condiciones multiples")
edad = 25
licencia_conducir = True
if edad >= 18 and licencia_conducir: # con operador logico -> AND 
    print("Puedes conducir")
else:
    print("No puedes conducir, estas detenido 👮‍♀️")


if edad >= 18 or licencia_conducir: # con operador logico -> OR 
    print("Puedes ingresar a Peru")
else:
    print("No puedes ingresar, al menos a que pagues al policia")



fin_semana = False
if not fin_semana:  # con operador logico -> NOT
    print("Estas trabajando")



print("\n Anidar condicionales")
edad = 20
tiene_dinero = True
if edad >= 18:
    if tiene_dinero:
        print("Puedes comprar un automovil")
    else:
        print("No tienes suficiente dinero")
else:
    print("No puedes comprar un automovil, estas detenido ��‍��️")

# FORMA MAS FACIL 

# if edad < 18: 
#    print("No puedes comprar un automovil, estas detenido ��‍��️")
# elif: tiene_dinero:
#    print("Puedes comprar un automovil")
# else:
#    print("No tienes suficiente dinero")



