from termcolor import colored

while True:
    name = input(colored('Hello, I am Roboko. What is your name?\n', 'green'))
    if name:
        restaurant = input(colored(name + ', which restaurants do you like?\n', 'green'))
        if restaurant:
            fin = colored('Roboko: Thank you so much, {}!\nHave a good day!', 'green')
            print(fin.format(name))
            break