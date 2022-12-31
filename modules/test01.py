# coding:utf-8
from random import randint

inputvector = [randint(-5, 5) for i in range(10)]
print("Input values\n:")
print(inputvector)


def mymin(u: list = []):
    minimum = u[0]
    for i in u:
        if i < minimum:
            minimum = i
    return minimum


def remove_element(element, u: list) -> list:
    newarray = u[:]
    for position, i in enumerate(u):
        if i == element:
            newarray.pop(position)
            return newarray


def ordenar(data: list) -> list:
    newdata = data[:]
    res = []
    for elements in range(len(data)):
        res.append(mymin(newdata))
        newdata = remove_element(res[-1], newdata)
    return res


if __name__ == "__main__":
    # testing
    # print(mymin([1,2,2,2,1,1,2]))
    # print(remove_element(4, [0,1,2,3,4]))
    print(ordenar(inputvector))
