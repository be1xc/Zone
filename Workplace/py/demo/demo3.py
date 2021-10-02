# 输出商品列表，用户输入序号，显示用户选中的商品
# li = ["手机", "电脑", '鼠标垫', '游艇']


li = ["手机", "电脑", '鼠标垫', '游艇']

[print(i) for i in li] 
a = int(input())
if a in range(1,5):
    print(li[a-1])