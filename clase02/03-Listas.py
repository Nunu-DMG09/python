###
# LISTAS
# Secuencias mutables de elementos. Puden contener elementos de diferentes tipos.
###

# Creacion de listas 
print("\nCrear listas")
lista1 = [1,2,3,4,5] #Lista de enteros
lista2 = ["manzanas", "peras", "platanos"] #Lista de cadenas
lista3 = [1,"hola", 3.14, True] # Lista de tipos mixtos

lista_vacia = []
lista_de_listas = [[1,2],['calcetin',4]]
matrix = [[1,2],[3,4],[4,5]]

print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)
print(matrix)

# Acceder a elementos por indices
print("\nAcceder a elementos por indices")
print(lista2[0]) # manzanas
print(lista2[1]) # peras
print(lista2[-1]) # platanos
print(lista2[-2]) # peras

print(lista_de_listas[1][0])

# Slicing (rebanado) de listas 

lista1 = [1,2,3,4,5]
print(lista1[1:4]) #[2, 3, 4]

 