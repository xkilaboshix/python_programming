import csv
from termcolor import colored
from termcolor import cprint

def read_csv():
    with open('ranking.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        data = []
        for row in reader:
           data.append(row)
        print(data)
        print('##########')
        for d in data:
            print(d)
        return data

def write_csv(data, restaurant):
    with open('ranking.csv', 'w') as csv_file:
        fieldnames = ['NAME', 'COUNT']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'NAME': restaurant, 'COUNT': 1})
        for d in data:
            writer.writerow(d)
            print(d)



while True:
    cprint('=' * 40, 'green')
    name = input(colored('Hello, I am Roboko. What is your name?\n' + '=' * 40 + '\n', 'green'))
    if name:
        break
    cprint('Please enter your name!', 'red')

while True:
    cprint('=' * 40, 'green')
    restaurant = input(colored(name + ', which restaurants do you like?\n' + '=' * 40 + '\n', 'green'))
    cprint('=' * 40, 'green')
    fin = colored('Roboko: Thank you so much, {}!\nHave a good day!\n' + '=' * 40 + '\n', 'green')
    print(fin.format(name))
    if restaurant:
        write_csv(data=read_csv(), restaurant=restaurant)
        break





