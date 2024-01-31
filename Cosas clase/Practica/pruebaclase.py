word_without_vowels = ""

user_word = input("Dime una palabra: ")
user_word = user_word.upper()

# Indicar al usuario que ingrese una palabra
# y asignarla a la variable user_word.

for letter in user_word:
    if letter not in "AEIOU":
        word_without_vowels += letter
    # Completa el cuerpo del bucle.

# Imprimir la palabra asignada a word_without_vowels.
print(word_without_vowels)