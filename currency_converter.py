def main():
    print("This program converts US dollars to Reais")
    print()

    dollars = eval(input("Enter amount in dollars: "))

    reais = convert_to_reais(dollars)

    print(F"That is {reais} reais.")

convert_to_reais = lambda dollars: dollars * 5.47

main()