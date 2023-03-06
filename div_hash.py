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
    return hash_list

print(division(string_to_ord('Helo world!')))