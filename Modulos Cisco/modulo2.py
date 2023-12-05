# Imprimir por pantalla
print("¡Hola, Mundo!")


# La \n salta de linea (nueva linea) y print() solo genera una linea sin nada y continua a la siguiente.
print("La Witsi Witsi Araña\nsubió a su telaraña.")
print()
print("Vino la lluvia\ny se la llevó.")

# Con más de un argumento
print("La Witsi Witsi Araña" , "subió" , "a su telaraña.")

# Evita el salto de linea y añade al final del primer print lo que queramos
print("Mi nombre es", "Python.", end=" ")
print("Monty Python.")

# Añade entre valor y valor lo que pongamos, en este caso un -.
print("Mi", "nombre", "es", "Monty", "Python.", sep="-")

print("Mi", "nombre", "es", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

print("Programming","Essentials","in", sep="***", end="...")
print("Python")

# PRUEBAS CON FLECHAS
print("original version:")
###################
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
###################
print("with fewer 'print()' invocations:")
###################
print("    *\n   * *\n  *   *\n *     *\n***   ***")
print("  *   *\n  *   *\n  *****")
###################
print("higher:")
###################
print("        *")
print("       * *")
print("      *   *")
print("     *     *")
print("    *       *")
print("   *         *")
print("  *           *")
print(" *             *")
print("******     ******")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *******")
###################
print("doubled:")
###################
print("        *        "*2)
print("       * *       "*2)
print("      *   *      "*2)
print("     *     *     "*2)
print("    *       *    "*2)
print("   *         *   "*2)
print("  *           *  "*2)
print(" *             * "*2)
print("******     ******"*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *******     "*2)

# Los numeros se pueden escribir tanto..
print(1111111)
print(1_111_111)
print(-1111111)
print(-1_111_111)

# Numeros octales
print(0o123) # es 83 en decimal, el "0o" dice que los numeros seran del 0..7 y que haga la conversion automatica.
print(0x123) # es 291 en hexadecimal, usa "0x"

# Flotantes
print(4)
print(4.3) # python no acepta comas, se utilizan puntos.
print(4.0)

#Cadenas
print("Me gusta \"Monty Python\"") #poner comillas en una cadena y que se vea
print('Me gusta "Monty Python"')
print('I\'m Monty Python.') #apostrofado
print("I'm Monty Python.")

print("\"I'm\"\n\"\"learning\"\"\n\"\"\"Python\"\"\"") # ESTAS 2 HACEN LO MISMO
print('\n"Estoy"','""apendiendo""','"""Python"""', sep="\n")

#Valores booleanos
print(True > False)
print(True < False)
print(None) # se utiliza para representar la ausencia de un valor.

#Python calculadora
print(2+2)

# ORDEN
# +
# -
# *
# /
# //
# %
# **

#EXPONENTES
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)

#MULTIPLICACION
print(2 * 3) 
print(2 * 3.)
print(2. * 3)
print(2. * 3.)

#DIVISIÓN, SIEMPRE ARROJA NUMERO DE TIPO COMA FLOTANTE
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)

#DIVISION ENTERA, los resultados se redondean y se ajustan a las reglas de entero y flotante como las multiplicaciones.
print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)

print(6 // 4)
print(6. // 4)

print(-6 // 4)
print(6. // -4)

#RESIDUO O MODULO
print(14 % 4)
print(12 % 4.5)

#SUMA
print(-4 + 4)
print(-4. + 8)

#RESTA
print(-4 - 4)
print(4. - 8)
print(-1.1)

#PRIORIDAD DE OPERADORES BASICOS
# 1	**	
# 2	+, - (nota: los operadores unarios a la derecha del operador exponencial enlazan con mayor fuerza.)	unario
# 3	*, /, //, %	
# 4	+, -	binario

print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)

#Palabras clave y que no debemos asignar variables a ellas
# ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 
# 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

#Crear una variable
var = 1
print(var)

var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)
print(var)

#No existe la variable como vemos
var = 1
print(Var)

#Usar print para combinar variables con texto, se usa el + para concatenarlas
var = "3.8.5"
print("Python version: " + var)

#Asignar un nuevo valor a una variables existente
var = 1
print(var)
var = var + 1
print(var)

var = 100
var = 200 + 300
print(var)
 
#Teorema de pitagoras
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)

#EJEMPLO
john = 3
mary = 5
adam = 6

print(john, mary, adam)

total_apples = john + mary + adam

print(total_apples)