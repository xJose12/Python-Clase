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