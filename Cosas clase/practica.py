#
coste_manzana = 10
print("El coste de las manzanas es:" + str(coste_manzana))
manzanas = input("cuantas manzanas quieres?")
total = coste_manzana * int(manzanas)
print("Total a pagar:" + str(total))

#
age = int(input("Cuantos años tienes?"))
if age >= 18:
    print("Eres un adulto independiente")
else:
    print("Aun sigues siendo un niño")
    
#
año2 = int(input("Dame tu año de nacimiento"))
año_actual = 2023
total2 = año_actual - año2
if total2 > 18:
    print("Tienes " + str(total2) + " años")
    print("Eres un adulto independiete")
elif total2 == 18:
    print("Acabas de cumplir la mayoria de edad")
else:
    print("Tines " + str(total2) + " años")
    print("Aun sigues siendo un niño")
    
#
numero = 3
adivinar = int(input("Dime el numero a acertar: "))

while adivinar != numero:
    print("Lo siento ese no era el numero")
    adivinar = int(input("Dime el numero a acertar: "))

print("Has adivinado el numero!!  enhorabuena")

#
for i in range(5):
    if(i == 2):
        break
    print("i is: ", i)
    
#
contador = int(input("Dime un numero: "))

for i in range(100):
    if(i == contador):
        break
    print("i is: ", i)

#
paises = ["España", "Paises Bajos", "EEUU", "Francia", "Portugal"]
print(paises[2])
print(len(paises))
del paises[1]
print(paises)

#
paises = ["España", "Paises Bajos", "EEUU", "Francia", "Portugal"]
print(paises[2])
print(len(paises))
del paises[1]
print(paises)
paises.append("Spain")
paises.insert(3, "Italia")
print(paises)