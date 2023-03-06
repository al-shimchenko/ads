def string_to_ord(string):
    ord_list = []
    for i in string:
        ord_list.append(ord(i))
    return ord_list


def division(array):
    m = len(array)
    hash_list = []
    for k in array:
        hash = k % m
        hash_list.append(hash)
        # hash_list.append(str(hash))
    # hash_list = "".join(hash_list)
    return hash_list


def multiplication(array):
    m = len(array)
    c = (5 ** 0.5 - 1) / 2
    hash_list = []
    for k in array:
        hash = int(m * ((k * c) % 1))
        hash_list.append(hash)
        # hash_list.append(str(hash))
    # hash_list = "".join(hash_list)
    return hash_list


def addition(array):
    hash = sum(array) % 256
    return hash


print(division(string_to_ord('Helo world!')))
# print(multiplication(string_to_ord('Hello world!')))
# print(addition(string_to_ord('Hello world!')))
