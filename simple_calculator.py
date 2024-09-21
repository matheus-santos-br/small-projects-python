def add(a,b):
    answer = int(a)+int(b)
    print(str(a) + " + " + str(b) + " = " + str(answer))


def sub(a,b):
    answer = int(a)-int(b)
    print(str(a) + " - " + str(b) + " = " + str(answer))

def mult(a,b):
    answer = int(a)*int(b)
    print(str(a) + " * " + str(b) + " = " + str(answer))


def div(a,b):

    if(int(b) == 0):
        print("Cannot divide by 0.")
        return

    answer = int(a)/int(b)
    print(str(a) + " / " + str(b) + " = " + str(answer))

print("A. Addition")
print("B. Subtraction")
print("C. Multiplication")
print("D. Division")
print("E. Exit")

choice = input("Input your choice: ")

choice = choice.upper()

while(choice != "E"):

    if choice == "A":
        a = input("1º number: ")
        b = input("2º number: ")
        add(a,b)
        choice = input("Input your choice: ")
        choice = choice.upper()
    elif choice == "B":
        a = input("1º number: ")
        b = input("2º number: ")
        sub(a,b)
        choice = input("Input your choice: ")
        choice = choice.upper()
    elif choice == "C":
        a = input("1º number: ")
        b = input("2º number: ")
        mult(a,b)
        choice = input("Input your choice: ")
        choice = choice.upper()
    elif choice == "D":
        a = input("1º number: ")
        b = input("2º number: ")
        div(a,b)
        choice = input("Input your choice: ")
        choice = choice.upper()
    else:
        choice = input("Input your choice: ")
        choice = choice.upper()
