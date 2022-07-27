from CalculateTax import calculate_tax

while True:
    try:
        tax = int(input("Please input your income\n"))
    except ValueError:
        print("Please give a number!\n")
        continue

    print("Your tax is", calculate_tax(tax))

    answer = input("What do you want to do?\n"
        "Press yes to calculate again\n"
        "Press no to quit\n")

    if answer.lower() == "yes":
        continue
        print(answer)
    elif answer.lower() == "no":
        break
        print(answer)
    else:
        print("Please give yes or no!\n")
        continue

