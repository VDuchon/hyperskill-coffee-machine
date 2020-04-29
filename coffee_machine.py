import json

water_espresso = 250
beans_espresso = 16
cost_espresso = 4

water_latte = 350
milk_latte = 75
beans_latte = 20
cost_latte = 7

water_cappuccino = 200
milk_cappuccino = 100
beans_cappuccino = 12
cost_cappuccino = 6


class CoffeeMachine:

    def __init__(self):
        self.water_total = 400
        self.milk_total = 540
        self.beans_total = 120
        self.cups = 9
        self.money = 550
        self.status = "main"
        
    def do(self, usr_input):
        if self.status == "main":
            if usr_input == "buy":
                self.status = "coffee"
            elif usr_input == "fill":
                self.status = "add_water"
            elif usr_input == "take":
                coffeeMachine.take()
            elif usr_input == "remaining":
                coffeeMachine.print_machine_status()
        elif self.status == "coffee":
            self.make_coffee(usr_input)
            self.status = "main"
        elif self.status == "add_water":
            self.water_total += int(usr_input)
            self.status = "add_milk"
        elif self.status == "add_milk":
            self.milk_total += int(usr_input)
            self.status = "add_beans"
        elif self.status == "add_beans":
            self.beans_total += int(usr_input)
            self.status = "add_cups"
        elif self.status == "add_cups":
            self.cups += int(usr_input)
            self.status = "main"

    def make_coffee(self, coffee_type):
        if self.cups == 0:
            print("Cannot make coffee - there are no more cups.")
        elif coffee_type == "1":  # espresso
            if self.water_total >= water_espresso and self.beans_total >= beans_espresso:
                self.water_total -= water_espresso
                self.beans_total -= beans_espresso
                self.money += cost_espresso
                self.cups -= 1
            else:
                print("There is not enough ingredients to make an espresso.")
        elif coffee_type == "2":  # latte
            if self.water_total >= water_latte and self.beans_total >= beans_latte and milk_latte:
                self.water_total -= water_latte
                self.beans_total -= beans_latte
                self.milk_total -= milk_latte
                self.money += cost_latte
                self.cups -= 1
            else:
                print("There is not enough ingredients to make an espresso.")
        elif coffee_type == "3":  # cappuccino
            if self.water_total >= water_cappuccino and self.beans_total >= beans_cappuccino and milk_cappuccino:
                self.water_total -= water_cappuccino
                self.beans_total -= beans_cappuccino
                self.milk_total -= milk_cappuccino
                self.money += cost_cappuccino
                self.cups -= 1
            else:
                print("There is not enough ingredients to make an espresso.")
        elif coffee_type == "back":
            pass
        else:
            print("Coffee of unknown type selected.")

    def take(self):
        print("I gave you $", self.money)
        self.money = 0

    def print_machine_status(self):
        print()
        print("The coffee machine has:")
        print(self.water_total, " of water")
        print(self.milk_total, " of milk")
        print(self.beans_total, " of beans")
        print(self.cups, " of disposable cups")
        print("$", self.money, " of money")
        print()

    def print_menu(self):
        print()
        if self.status == "main":
            print("Write action (buy, fill, take, remaining, exit):")
        elif self.status == "coffee":
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        elif self.status == "add_water":
            print("Write how many ml of water do you want to add:")
        elif self.status == "add_milk":
            print("Write how many ml of milk do you want to add:")
        elif self.status == "add_beans":
            print("Write how many grams of coffee beans do you want to add:")
        elif self.status == "add_cups":
            print("Write how many disposable cups of coffee do you want to add:")


coffeeMachine = CoffeeMachine()
while True:
    coffeeMachine.print_menu()
    action = input()
    if action == "exit":
        break
    else:
        coffeeMachine.do(action)
