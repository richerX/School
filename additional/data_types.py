mas_1 = [1, 2, 3]  # массив|list, changeable (c++ - vector)
mas_2 = list((1, 2, 3))
print(type(mas_1), type(mas_2), "changeable")
print("mas_1: ", mas_1)
print("mas_2: ", mas_2)
print()


tuple_1 = (1, 2, 3)  # кортеж|tuple, unchangeable
tuple_2 = tuple("hello")
print(type(tuple_1), type(tuple_2), "unchangeable")
print("tuple_1: ", tuple_1)
print("tuple_2: ", tuple_2)
print()


set_1 = {1, 2, 3}  # множество|set, changeable (c++ - set)
set_2 = set()
set_2.add(1)
print(type(set_1), type(set_2), "changeable")
print("set_1: ", set_1)
print("set_2: ", set_2)
print()


dict_1 = {"a": 1, "b": [2, 3]}  # словарь|dictionary, changeable (c++ - map)
dict_2 = dict()
dict_2["a"] = 1
print(type(dict_1), type(dict_2),"changeable")
print("dict_1: ", dict_1)
print("dict_2: ", dict_2)
print()