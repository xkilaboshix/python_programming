import csv
from termcolor import colored
from termcolor import cprint

def read_csv():
    with open('ranking.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        data = []
        for row in reader:
           data.append(row)
        # print(data)
        # print('#########################')
        # print(data[0])
        # print('#########################')
        # print(data[0]['NAME'])
        # print('#########################')
        # for d in data:
        #     print(d)
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

        # for d in data:
        #      writer.writerow(d)
        # count = 1
        # writer.writerow({'NAME': restaurant, 'COUNT': count})


        for i in range(len(data)):
            if restaurant == data[i - 1]['NAME']:
                data[i - 1]['COUNT'] = int(data[i - 1]['COUNT']) + 1
                for d in data:
                    writer.writerow(d)
                print(data[i - 1]['COUNT'])

        if restaurant not in dic.keys():
             for d in data:
                 writer.writerow(d)
             count = 1
             writer.writerow({'NAME': restaurant, 'COUNT': count})

# def update_count(data, restaurant):
#     for i in range(len(data)):
#         if restaurant == data[i - 1]['NAME']:
#             data[i - 1]['COUNT'] = int(data[i - 1]['COUNT']) + 1


        # if restaurant not in d.values():
        #     print('oooooooooooooooooooooooooo')
        #     for d in data:
        #         print(d.values())
        #     count = 1
        #     writer.writerow({'NAME': restaurant, 'COUNT': count})
        # else:
        # print('#############################')
        # print(dic[restaurant])
        # count = dic[d[restaurant]]
        # count += 1
        # writer.writerow({'NAME': restaurant, 'COUNT': count})


while True:
    cprint('=' * 40, 'green')
    name = input(colored('Hello, I am Roboko. What is your name?\n' + '=' * 40 + '\n', 'green')).capitalize()
    if name:
        break
    cprint('Please enter your name!', 'red')



if data != []:
    dic2 = sorted(dic.items(), key=lambda x:x[1], reverse=True)
    print(dic2)
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

    # print('#############################')



    if restaurant in dic.keys():
        dic[restaurant] = dic[restaurant] + 1
        # print(dic[restaurant])

    fin = colored('Roboko: Thank you so much, {}!\nHave a good day!\n' + '=' * 40 + '\n', 'green')
    print(fin.format(name))
    if restaurant:
        write_csv(data=read_csv(), restaurant=restaurant)
        break

# dic = {}
# for d in data:
#     dic.update({d['NAME']: int(d['COUNT'])})

# print(dic)

# if restaurant in dic.keys():
# #     dic[restaurant] = dic[restaurant] + 1
# #     print(dic[restaurant])
# #     print(dic)

# dic2 = sorted(dic.items(), key=lambda x:x[1], reverse=True)
# print('#########################')
# print(dic2)
# print(len(dic2))
#
# for d in dic2:
#     print(d)
#     print(d[0])
#     while True:
#         recommend = colored('I recommend {} restaurant.\nDo you like it? [Yes/No]\n' + '=' * 40 + '\n', 'green')
#         cprint('=' * 40, 'green')
#         answer = input(recommend.format(d[0])).upper()
#         if answer == 'YES' or answer == 'NO' or answer == 'Y' or answer == 'N':
#             break





