class CoffeeMachine():
    water = 400
    milk = 540
    beans = 120
    cups = 9
    money = 550
    default_message = 'Write action (buy, fill, take, remaining, exit):'
    current_state = 'choosing an action'
    get_command = ''

    def user_input(self, command_line):
        CoffeeMachine.get_command = command_line

    def __str__(self):
        if CoffeeMachine.get_command == 'exit':
            CoffeeMachine.exit_machine(self)
            return 'exit'
        if CoffeeMachine.get_command == 'remaining':
            CoffeeMachine.current_state = 'choosing an action'
            return CoffeeMachine.remaining(self)
        if CoffeeMachine.get_command == 'take':
            CoffeeMachine.current_state = 'choosing an action'
            return CoffeeMachine.take_money(self)
        if CoffeeMachine.get_command == 'buy':
            CoffeeMachine.current_state = 'buying'
            return 'What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:'
        if CoffeeMachine.current_state == 'buying':
            if CoffeeMachine.get_command == '1':
                CoffeeMachine.current_state = 'choosing an action'
                return CoffeeMachine.espresso(self)
            if CoffeeMachine.get_command == '2':
                CoffeeMachine.current_state = 'choosing an action'
                return CoffeeMachine.latte(self)
            if CoffeeMachine.get_command == '3':
                CoffeeMachine.current_state = 'choosing an action'
                return CoffeeMachine.cappuccino(self)
        if CoffeeMachine.get_command == 'fill':
            CoffeeMachine.current_state = 'filling water'
            return 'Write how many ml of water do you want to add:'
        if CoffeeMachine.current_state == 'filling water':
            CoffeeMachine.water += int(CoffeeMachine.get_command)
            CoffeeMachine.current_state = 'filling milk'
            return 'Write how many ml of milk do you want to add:'
        if CoffeeMachine.current_state == 'filling milk':
            CoffeeMachine.milk += int(CoffeeMachine.get_command)
            CoffeeMachine.current_state = 'filling beans'
            return 'Write how many grams of coffee beans do you want to add:'
        if CoffeeMachine.current_state == 'filling beans':
            CoffeeMachine.beans += int(CoffeeMachine.get_command)
            CoffeeMachine.current_state = 'filling cups'
            return 'Write how many disposable cups of coffee do you want to add:'
        if CoffeeMachine.current_state == 'filling cups':
            CoffeeMachine.cups += int(CoffeeMachine.get_command)
            CoffeeMachine.current_state = 'choosing an action'
            return f'{CoffeeMachine.default_message}'
        if CoffeeMachine.current_state == 'choosing an action':
            return f'{CoffeeMachine.default_message}'
        return f'{CoffeeMachine.current_state}'

    def exit_machine(self):
        CoffeeMachine.current_state = 'exit'

    def remaining(self):
        remain = (f'The coffee machine has:\n'
                        + f'{CoffeeMachine.water} of water\n'
                        + f'{CoffeeMachine.milk} of milk\n'
                        + f'{CoffeeMachine.beans} of coffee beans\n'
                        + f'{CoffeeMachine.cups} of disposable cups\n'
                        + f'{CoffeeMachine.money} of money\n\n{CoffeeMachine.default_message}')
        return remain

    def take_money(self):
        get_money = CoffeeMachine.money
        CoffeeMachine.money = 0
        return f'I gave you ${get_money}\n\n{CoffeeMachine.default_message}'

    def espresso(self):
        if CoffeeMachine.water >= 250 and CoffeeMachine.beans >= 16 and CoffeeMachine.cups >= 1:
            CoffeeMachine.water -= 250
            CoffeeMachine.beans -= 16
            CoffeeMachine.cups -= 1
            CoffeeMachine.money += 4
            return f'I have enough resources, making you a coffee!\n\n{CoffeeMachine.default_message}'
        else:
            if CoffeeMachine.water < 250:
                return f'Sorry, not enough water!\n\n{CoffeeMachine.default_message}'
            elif CoffeeMachine.beans < 16:
                return f'Sorry, not enough coffee beans!\n\n{CoffeeMachine.default_message}'
            elif CoffeeMachine.cups < 1:
                return f'Sorry, not enough cups!\n\n{CoffeeMachine.default_message}'

    def latte(self):
        if CoffeeMachine.water >= 350 and CoffeeMachine.beans >= 20 and CoffeeMachine.cups >= 1 and CoffeeMachine.milk >= 75:
            CoffeeMachine.money += 7
            CoffeeMachine.water -= 350
            CoffeeMachine.milk -= 75
            CoffeeMachine.beans -= 20
            CoffeeMachine.cups -= 1
            return f'I have enough resources, making you a coffee!\n\n{CoffeeMachine.default_message}'
        else:
            if CoffeeMachine.water < 350:
                return f'Sorry, not enough water!\n\n{CoffeeMachine.default_message}'
            elif CoffeeMachine.beans < 20:
                return f'Sorry, not enough coffee beans!\n\n{CoffeeMachine.default_message}'
            elif CoffeeMachine.cups < 1:
                return f'Sorry, not enough cups!\n\n{CoffeeMachine.default_message}'
            elif CoffeeMachine.milk < 75:
                return f'Sorry, not enough milk!\n\n{CoffeeMachine.default_message}'

    def cappuccino(self):
        if CoffeeMachine.water >= 200 and CoffeeMachine.beans >= 12 and CoffeeMachine.cups >= 1 and CoffeeMachine.milk >= 100:
            CoffeeMachine.money += 6
            CoffeeMachine.water -= 200
            CoffeeMachine.milk -= 100
            CoffeeMachine.beans -= 12
            CoffeeMachine.cups -= 1
            return f'I have enough resources, making you a coffee!\n\n{CoffeeMachine.default_message}'
        else:
            if CoffeeMachine.water < 200:
                return f'Sorry, not enough water!\n\n{CoffeeMachine.default_message}'
            elif CoffeeMachine.beans < 12:
                return f'Sorry, not enough coffee beans!\n\n{CoffeeMachine.default_message}'
            elif CoffeeMachine.cups < 1:
                return f'Sorry, not enough cups!\n\n{CoffeeMachine.default_message}'
            elif CoffeeMachine.milk < 100:
                return f'Sorry, not enough milk!\n\n{CoffeeMachine.default_message}'


while True:
    cm = str(CoffeeMachine())
    if cm == 'exit':
        break
    print(cm)
    CoffeeMachine().user_input(input())