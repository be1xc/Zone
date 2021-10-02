#   有如下值集合 [11,22,33,44,55,66,77,88,99,90]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。
#    即： {'k1': 大于66的所有值, 'k2': 小于66的所有值}

list = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
kdic = {'k1': [], 'k2': []}
list1, list2 = [], []
[list1.append(x) if x > 66 else list2.append(x) for x in list]
kdic['k1'].append(list1)
kdic['k2'].append(list2)
print(kdic)
