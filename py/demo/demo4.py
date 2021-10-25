goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]

money = int(input('请输入总资产: '))
price = 0
count = []
for i in range(len(goods)):
    print(goods[i]['name'])
    Y = input('是否加入购物车 数量： ')
    # price += goods[i]['price']*int(Y)
    count.append(int(Y))

while 1:
    price = int(count[0]*1999+count[1]*10+count[2]*20+count[3]*998)
    print('购物车：电脑：{},鼠标：{},游艇：{},美女：{},总价格：{}'.format(count[0],count[1],count[2],count[3],price))
    if money >= price:
        print('success, 余额：{}'.format(money-price))
        break
    else:
        print('持有额度：{}'.format(money))
        print('failed, 余额不足，是否充值？')
        money += int(input('充值额度: '))