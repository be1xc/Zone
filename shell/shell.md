## SHELL

shell 脚本格式
```bash
#!/usr/bin/bash #shell脚本开头必须指定解析环境 
# #是注释

# #shell脚本信息
#Author:
#Created:
#release:
#Script Description:
```

shell的特殊符号
```
~   # 家目录
!   # 执行历史命令  !! 执行上一次命令  !num 执行history的命令 !p 执行history中最后一次的p开头的命令
$   变量中取内容符
+ - * / %  数学运算符
&   把代码放入后台执行
*   shell的通配符 匹配所有字符
?   shell的通配符 匹配回车外的一个字符
;   一行中区分多条命令
|   管道符 上个命令的输出作为下一个命令的输入 cat filename | grep "abc"
\   转义字符
``   反引号 命令中执行命令 echo "today is `date +%F`"
' '   单引号 脚本中字符串需要用单引号引起来 但不解释变量
" "   双引号 脚本出现的字符串可以用双引号引起来
```

shell重定向
```bash
echo hehe > filename.txt  #把filename内容清空并输入 hehe
echo hehe >> filename.txt # 追加进filename
wc -l < /etc/passwd #重定向输出
fdisk /dev/sdb << EOF ...... EOF #重定向追加输出
```

shell数学运算
```bash
expr 1 +(-/%) 1
expr 1 \* 1 

# 非整数
echo "scale=2;100/3"|bc

# 双小括号运算
echo $((100/3)) #只返回整数
```

shell格式化输出
```bash
echo [-ne] [字符串]
`-n` 不再最后自动换行
`-e` 若字符串出现以下字符，则特殊处理，不会识别为字符串

\a 发出警告声
\t 插入制表符
\n 插入回车
\b 删除此字符前的一个字符

#颜色代码
echo -e "\033[字背景颜色;文字颜色m字符串\033[0m"
```

shell基本输入
```bash
read [变量]# 接收键盘的输入
-p [字符串] # 打印信息
-t num # 超时 单位s
-s # 不回显输入的字符
-n num # 最大字符数字

#### eg

#! /usr/bin/bash
clear

echo "Ubuntu Linux 20"
echo -e "kernel `uname -r` an `uname -m\n"

echo -n -e "$HOSTNAME login: "
read acc
read -p "password:"
read pw
```

变量

> 变量名和等号值不能有空格  `NAME='name'`
```bash
unset name #取消变量
```

数组

```bash
变量名=(元素1 元素2 元素3 ...)
echo ${变量名[索引]}

arr=(0 1)
#赋值
arr[2]=3 #可以追加赋值
arr=(元1 元2 元3)
arr=(`cat ./filepath`) #读取文件，每行作为一个元素赋值
arr=(`ls`) #每个结果作为元素赋值

#数组查看
declare -a #查看系统数组
echo ${arr[索引]} #查看索引的元素
echo ${arr[@]} #查看数组 == echo ${arr[*]}
echo ${#arr[@]} #统计数组元素个数
echo ${!arr[@]} #获取数组下标
echo ${arr[@]:1} #获取索引1 后的所有元素
echo ${arr[@]:2:num} #获取索引 2 后的 num 个元素
```

关联数组
```bash
declare -A arr  #声明一个关联数组

#赋值
arr[name]='be1xc'
arr=([index1]='fire' [index2]='water')
```

流程控制

```bash
#数学比较运算
-eq  # ==
-gt  # >
-lt  # <
-ge  # >=
-le  # <=
-ne  # !=
```