apple_price = 2
grape_price = 1
orange_price = 3

apple_total = 0
grape_total = 0
orange_total = 0


print("Welcome to the GC Fruit Market!")
print("What is your name?")
name = input()


while True:
    print(f"Welcome {name}, Which fruit would you like to buy? ")
    print("1. Apple $2")
    print("2. Grape $1")
    print("3. Orange $3")
    fruit_option = input("Choose 1,2, or 3: ")

    if fruit_option == "1":
        apple_total += 1
        print(f"You bought one apple at ${apple_price}")
    elif fruit_option == "2":
        grape_total += 1
        print(f"You bought 1 grape at ${grape_price}")
    elif fruit_option == "3":
        orange_total += 1
        print(f"You bought 1 orange at ${orange_price}")
    else:
        print("Please enter a valid selection")
        continue

    continueOrder = print("Would you like to buy another piece of fruit? y/n")
    continueOrder = input()
    while continueOrder.lower() not in ["y", "n"]:
        print("Please enter a valid selection")
        continueOrder = print("Would you like to buy another piece of fruit? (y/n) ")
        continueOrder = input()


    if continueOrder.lower() != "y":

        break


print(f"Order for {name}")
print(f"{apple_total} apple(s) at ${apple_price} a piece")
print(f"{grape_total} grape(s) at ${grape_price} a piece")
print(f"{orange_total} orange(s) at ${orange_price} a piece")

sub_total = (apple_total * apple_price) + (grape_total * grape_price) + (orange_total * orange_price)
pre_tax = "Sub Total: ${:.2f}"
print(pre_tax.format(sub_total))
tax = sub_total * .05
final_tax= "5% Tax: ${:.2f}"
print(final_tax.format(tax))
order_total = sub_total + tax
order_summary = "Total: ${:.2f}"
print(order_summary.format(order_total))
#


#use while loop for ""
