import os
import csv
from termcolor import colored
from termcolor import cprint

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
        current_path = os.getcwd()  # カレントディレクトリパスを取得
        file_name = 'ranking.csv'  # 検索ファイル名を指定
        file_path = os.path.join(current_path, file_name)
        myCheck = os.path.isfile(file_path)
        with open('ranking.csv', 'a') as csv_file:
            fieldnames = ['NAME', 'COUNT']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            if not myCheck:
                writer.writeheader()
                writer.writerow({'NAME': restaurant, 'COUNT': 1})
                break
            else:
                writer.writerow({'NAME': restaurant, 'COUNT': 1})
                break


