# Definir la lista de nombres
nombres = ["Harry Houdini", "Newton", "David Blaine",
           "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]

# Separar los nombres en tres grupos
magos = ["Harry Houdini", "David Blaine", "Teller"]
cientificos = ["Newton", "Hawking", "Einstein"]
otros = [nombre for nombre in nombres if nombre not in magos and nombre not in cientificos]

# Definir la función hacer_grandioso


def hacer_grandioso():
    for i in range(len(magos)):
        magos[i] = "El gran " + magos[i]

# Definir la función imprimir_nombres


def imprimir_nombres():
    for nombre in nombres:
        print(nombre)


# Imprimir la lista completa de nombres antes de ser modificados
print("                          ")
print("Lista completa de nombres:")
print("                          ")
imprimir_nombres()
print("                          ")

# Modificar los nombres de los magos
hacer_grandioso()

# Imprimir los nombres de los magos grandiosos, los nombres de los científicos, y los restantes
print("                          ")
print("Nombres de los magos grandiosos:")
print("                          ")
for mago in magos:
    print(mago)
print("                          ")
print("Nombres de los científicos:")
print("                          ")
for cientifico in cientificos:
    print(cientifico)

print("                          ")
print("Nombres de los otros:")
print("                          ")
for otro in otros:
    print(otro)
