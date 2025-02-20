## Day 15

# 105 coffee machine project
"""
3 hot flavours

espresso  - 50ml water, 18g coffee              - 1.50
latte     - 200ml water, 24g coffee, 150ml milk - 2.50
cappuccino- 250ml water, 24g coffee, 100ml milk - 3.00

starts at
300ml water
200ml milk
100g coffee


Coin operated
penny - 1 cent
dime  - 10 cents
nickel- 5 cents
quarter-25 cents

print Report - should print the existing resources and the money gained
check resources sufficient
and if there are not enough resources, it should say not available

Should process coins
should say please insert coins
and asks for the respective types

if not enough money for the product, then refund it
and start the process again

so it should check for the successful transaction

if enough coins then make coffee and deduct the resources and add money
"""

MENU = {
    "espresso" : {
        "ingredients" : {
            "water" : 50,
            "milk" : 0,
            "coffee" : 18
        },
        "cost" : 1.5
    },
    "latte" : {
        "ingredients" : {
            "water" : 200,
            "milk" : 150,
            "coffee" : 24
        },
        "cost" : 2.5
    },
    "cappuccino" : {
        "ingredients" : {
            "water" : 200,
            "milk" : 150,
            "coffee" : 24
        },
        "cost" : 3.0
    }
}

resources = {
    "water" : 300,
    "milk" : 200,
    "coffee" : 100,  #Python automatically ignores the trailing comma
}

money = 0
## TODO: 1 """ Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
#a. Check the user’s input to decide what to do next.
#b. The prompt should show every time action has completed, e.g. once the drink is
#dispensed. The prompt should show again to serve the next customer."""


# will output the ingredients
# print(MENU["espresso"]["ingredients"]["water"])

# will output the cost
# print(MENU["espresso"]["cost"])
# print(resources["water"])


# prints the cost of the product from the menu
#print(MENU["cappuccino"]["cost"])


# prints water from the resources
#print(resources["water"])

# prints the required water to make the product
#print(MENU["espresso"]["ingredients"]["water"])

# checking if the values are being subtracted
#print(resources["water"] - MENU["espresso"]["ingredients"]["water"])
#print(resources["water"])


def print_resources():
    print(
        f"Water : {resources["water"]}ml\n"
        f"Milk : {resources["milk"]}ml\n"
        f"Coffee : {resources["coffee"]}g\n"
        f"Money : ${money}"
    )


def check_resources(uc):
    if uc == "espresso":
        if resources["water"] <= MENU["espresso"]["ingredients"]["water"] or resources["milk"] <= \
                MENU["espresso"]["ingredients"]["milk"] or resources["coffee"] <= MENU["espresso"]["ingredients"][
            "coffee"]:
            print("\nNot enough resources\n")
            print("\n\n Coffee machine will be shut down untill the resources have been fulfilled.\nThanks for using our product")
            machine_is_on = False
        else:
            print("\nMachine has enough resources\n")

    elif uc == "latte":
        if resources["water"] <= MENU["latte"]["ingredients"]["water"] or resources["milk"] <= \
                MENU["latte"]["ingredients"]["milk"] or resources["coffee"] <= MENU["latte"]["ingredients"]["coffee"]:
            print("\nNot enough resources\n")
            print("\n\n Coffee machine will be shut down untill the resources have been fulfilled.\nThanks for using our product")
            machine_is_on = False

        else:
            print("\nMachine has enough resources\n")

    elif uc == "cappuccino":
        if resources["water"] <= MENU["cappuccino"]["ingredients"]["water"] or resources["milk"] <= \
                MENU["cappuccino"]["ingredients"]["milk"] or resources["coffee"] <= MENU["cappuccino"]["ingredients"][
            "coffee"]:
            print("\nNot enough resources\n")
            print("\n\n Coffee machine will be shut down untill the resources have been fulfilled.\nThanks for using our product")
            machine_is_on = False

        else:
            print("\nMachine has enough resources\n")

    elif uc == "report":
        print("\n")
        print_resources()
        print("\n")
   # if uc != "report":
    #    print("\nMachine has enough resources\n")


def process_coins(pennies, nickels, dimes, quarters):
    dollars = 0
    dollars = pennies*0.01 + nickels*0.05 + dimes*0.10 + quarters*0.25
    return dollars


#a = process_coins(2,1,2,1)
#print(a)       works




machine_is_on = True

while machine_is_on:

    uc = input("What would you like? (espresso/latte/cappuccino):")

    check_resources(uc)
    if uc != "report":
        print(f"{uc} costs {MENU[uc]["cost"]}")
        quarters = int(input("How many quarters? : "))
        dimes = int(input("How many dimes? : "))
        nickels = int(input("How many nickels? : "))
        pennies = int(input("How many pennies? : "))

    this_total = process_coins(pennies=pennies,nickels = nickels, dimes=dimes,quarters=quarters)

    if uc == "report":
        print("Just reporting pal")
    elif this_total < MENU[uc]["cost"] and uc in ["espresso","latte","cappuccino"]:
        print("\nNot enough money\nYour money is refunded")
    else:
        if this_total > MENU[uc]["cost"] and uc in ["espresso","latte","cappuccino"]:
            money += MENU[uc]["cost"]
            print("transaction successful")
            print(f"Here is your change ${round(this_total - MENU[uc]["cost"],2)} since you paid ${this_total} which is more than required\n")
            resources["water"] -= MENU[uc]["ingredients"]["water"] # comas are not required...just like the dictionary it will understand
            resources["milk"] -= MENU[uc]["ingredients"]["milk"] # comas are not required...just like the dictionary it will understand
            resources["coffee"] -= MENU[uc]["ingredients"]["coffee"] # comas are not required...just like the dictionary it will understand
        else:
            if uc in ["espresso","latte","cappuccino"]:
                money += MENU[uc]["cost"]
                print("transaction successful")
                resources["water"] -= MENU[uc]["ingredients"]["water"] # comas are not required...just like the dictionary it will understand
                resources["milk"] -= MENU[uc]["ingredients"]["milk"] # comas are not required...just like the dictionary it will understand
                resources["coffee"] -= MENU[uc]["ingredients"]["coffee"] # comas are not required...just like the dictionary it will understand



