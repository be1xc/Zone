# 查找列表中元素，移除每个元素的空格，并查找以 a或A开头 并且以 c 结尾的所有元素。
li = ["alec", " aric", "Alex", "Tony", "rain"]
tu = ("alec", "aric", "Alex", "Tony", "rain")
dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}
all = []
call = []
ccall = []
[all.append(x) for x in li]
[all.append(x) for x in tu]
[all.append(x) for x in dic.values()]

[call.append(x.replace(' ', ''))
 for x in all if x.replace(' ', '') not in call]

[ccall.append(i) for i in call if i[0] in ('a','A') and i[-1] == 'c']

print(ccall)
