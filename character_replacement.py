name = 'Matheus'
print(name)

def replace_word():
    text = "Matheus"
    letter_to_replace = input("Enter the letter to replace: ")
    letter_replacement = input("Enter the letter replacement: ")
    print(text.replace(letter_to_replace,letter_replacement))

replace_word()