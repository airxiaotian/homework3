from EmployeeD import EmployeeD
import itertools as it
from operator import itemgetter


def get_estate():
    dic = EmployeeD()
    file = open("./unit2/Sacramentorealestatetransactions.csv", "r")
    line = file.readline()
    header = line.split(',')
    for line in file:
        dic[header] = line
        yield dic
        dic = EmployeeD()
    file.close()


def sort_key(dic):
    return dic['type']


def sort_price(dic):
    return dic['price']


estate_group = {}
data = list(get_estate())
data.sort(key=itemgetter('type'), reverse=False)

for key, group in it.groupby(data, key=itemgetter('type')):
    group_data = list(group)
    group_data.sort(key=itemgetter('price'))
    print("the highest price of {0} is {1}, the lowest price of {2} is {3}".format(
        key, group_data[len(group_data)-1]['price'], key, group_data[0]['price']))
