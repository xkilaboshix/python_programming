import csv
from termcolor import colored
from termcolor import cprint

def read_csv():
    with open('ranking.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        data = []
        for row in reader:
           data.append(row)
        return data

data = read_csv()
dic = {}
for d in data:
    dic.update({d['NAME']: int(d['COUNT'])})


def write_csv(data, restaurant):
    with open('ranking.csv', 'w') as csv_file:
        fieldnames = ['NAME', 'COUNT']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(len(data)):
            if restaurant == data[i - 1]['NAME']:
                data[i - 1]['COUNT'] = int(data[i - 1]['COUNT']) + 1
                for d in data:
                    writer.writerow(d)

        if restaurant not in dic.keys():
             for d in data:
                 writer.writerow(d)
             count = 1
             writer.writerow({'NAME': restaurant, 'COUNT': count})


while True:
    cprint('=' * 40, 'green')
    name = input(colored('Hello, I am Roboko. What is your name?\n' + '=' * 40 + '\n', 'green')).capitalize()
    if name:
        break
    cprint('Please enter your name!', 'red')


if data != []:
    dic2 = sorted(dic.items(), key=lambda x:x[1], reverse=True)
    for d in dic2:
        while True:
            recommend = colored('I recommend {} restaurant.\nDo you like it? [Yes/No]\n' + '=' * 40 + '\n', 'green')
            cprint('=' * 40, 'green')
            answer = input(recommend.format(d[0])).upper()
            if answer == 'YES' or answer == 'NO' or answer == 'Y' or answer == 'N':
                break


while True:
    cprint('=' * 40, 'green')
    restaurant = input(colored(name + ', which restaurants do you like?\n' + '=' * 40 + '\n', 'green')).title()
    cprint('=' * 40, 'green')

    fin = colored('Roboko: Thank you so much, {}!\nHave a good day!\n' + '=' * 40 + '\n', 'green')
    print(fin.format(name))
    if restaurant:
        write_csv(data=read_csv(), restaurant=restaurant)
        break

