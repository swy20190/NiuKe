### Algo NC 6
python max()函数参数可以是列表
```python
a = max(1, 2, 3, 4) # a=4
```

另外这题注意路径是任意的，不算从一个叶子到另一个叶子

### Algo NC 12
python list截取注意-1
```python
a = [1, 2, 3, 4, 5, 6]
b = a[3:-1] # b=[4, 5]
c = a[3:]   # c=[4, 5, 6]
```

### Algo NC 15
使用全局变量保存结果，dfs也能返回层序遍历的结果

### Algo NC 190
python set
```python
test = set()
test1 = set([1, 2, 3])
test2 = list(test1)
test1.add(4)  # 添加元素
test1.discard(4) # 删去元素， 元素不存在不报错

x = set('eleven')
y = set('twelve')
# x,y ({'l', 'e', 'n', 'v'}, {'e', 'v', 'l', 't', 'w'})
x & y  #交集
#{'l', 'e', 'v'}
x | y  #并集
#{'e', 'v', 'n', 'l', 't', 'w'}
x - y  #差集
# {'n'}
y -x   #差集
# {'t', 'w'}
x ^ y  #补集
# {'t', 'n', 'w'}
y ^ x  #补集
#{'w', 'n', 't'}

```

### HJ 3
python

```python
try:
    n = input()
except:
    print(1)
```
或者
except(EOFError):

还有输入的所有值都是string，记得转化

列表去重：
```python
new_list = list(set(old_list))
```
### HJ 5 进制转换
其他进制转十进制：
int(n, 2/8/16或者任何数字)
十进制转其他进制
bin(n)
oct(n)
hex(n)

### HJ 6 质因数分解
python不换行输出：
print(num, end=" ")
注意end=


### HJ 8 
字典排序
```python
# 声明字典
    key_value ={}     
 
    # 初始化
    key_value[2] = 56       
    key_value[1] = 2 
    key_value[5] = 12 
    key_value[4] = 24
    key_value[6] = 18      
    key_value[3] = 323 
 
    print ("按键(key)排序:")   
 
    # sorted(key_value) 返回重新排序的列表
    # 字典按键排序
    for i in sorted (key_value) : 
        print ((i, key_value[i]), end =" ") 
```

```python
# 声明字典
    key_value ={}     
 
    # 初始化
    key_value[2] = 56       
    key_value[1] = 2 
    key_value[5] = 12 
    key_value[4] = 24
    key_value[6] = 18      
    key_value[3] = 323 
 
 
    print ("按值(value)排序:")   
    print(sorted(key_value.items(), key = lambda kv:(kv[1], kv[0])))   
```

### HJ 11
string 没有 reverse()方法，需要使用list(string)转化为list才行

### HJ 24
动态规划-二分查找优化
python 输入一行以空格分隔的树：
```python
input_list = list(map(int, input().split()))
```

### HJ 80
数组去重：
```python
old_list = [1, 1, 4, 5, 1, 4]
new_list = list(set(old_list))
```

### HJ 82
埃及分数

令c=int(a/b)+1

则

a/b = 1/c + (a*c-b)/b*c

### HJ 97
保留小数点后两位
```python
n = 114.514
new_n = round(n, 2) # new_n = 114.51
```

### HJ 108
math库求最大公因数：
```python
import math
a = 114
b = 514
c = math.gcd(a, b)
```

### NC 11
python 里面最小值，相当于c++里的INT_MIN：
```python
float("-inf")
```