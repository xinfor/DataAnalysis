# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 20:50:25 2017

@author: XiaoY


name = 'python'   # name就是一个代表字符串常量’python’的变量
one = 1   # one是代表整数型数据常量 1 的变量
a = 1.2   # a是代表浮点型(小数型)数字常量1.2的变量
print(name)   # 打印字符串 ’python’
print(one)   # 打印整型数字 1
print(a)   # 打印浮点数 1.2
print(int('1.2'))

two = 2
three = 3.0
city = 'shanghai'
yes = True

print(two + two) # 4，整数相加
print(two - three) # -1.0，整数与浮点数相减得到浮点数
print(two * 3.0) # 6.0，整数与浮点数相乘得到浮点数
print(5 / two) # 2.5， 整数相除得到浮点数
print(5 // two) # 2，进行整除
print(7 % three) # 1.0, 取余数
print(two ** three) # 8.0，幂运算
print(city + city) # 'shanghaishanghai'，连接字符串
print(city * 2) # 'shanghaishanghai'，字符串乘以整数就是进行自身连接该整数次

two = 2
three = 3.0
city = 'shanghai'

print(0 > two) # False，比较0是否大于2
print(0 < two) # True, 比较0是否小于2
print(2 >= two) # True，比较2是否大于等于2
print(2 <= three) # True，比较2是否小于等于3.0
print(3.0 == three) # True，比较3.0是否等于3.0
print(2 != two) # False，比较2是否不等于2
print(city > 'china') # True，字符串的比较依据字母排序

print(True and True) # True
print(True and False) # False
print(False or True) # True
print(not True) # False

citys = ['shanghai', 'beijing', 'hangzhou'] # 创建列表，每个元素都是字符串
info = ['xiaoming', 30, 178, 'beijing'] # 包含多种数据
infos = [['xiaohei', 28], ['xiaohong', 26]] # 列表的元素是列表
ints = list(range(10))
'''
range(0, 10, 1)生成从0-10步长为1的整数，不包含10
第一个和第三个参数可以不写，默认从0开始，步长为1
即生成0，1，2，3，4，5，6，7，8，9
list将其转换成列表
'''
print(citys)
print(info)
print(infos)
print(ints)
"""

list_remove = ['a', 'b', 'c', 'd', 'e']
list_remove.remove('c') # 删除元素'c'
print(list_remove) # ['a', 'b', 'd', 'e']

list_reverse = [1,2,3,4]
list_reverse.reverse() # 反转元素
print(list_reverse) # [4, 3, 2, 1]

list_sort = [13,4,3,8,1]
list_sort.sort() # 对元素排序
print(list_sort) # [1, 3, 4, 8, 13]

list_clear = [1, 'a', True]
list_clear.clear() # 清空
print(list_clear) # [] 得到空列表

computer = ['cpu', 'gpu', 'screen', 'disk', 'keyboard']
computer[4] = 'mouse' # 修改'keyboard'为'mouse'
print(computer) # ['cpu', 'gpu', 'screen', 'disk', 'mouse']
computer[2:] = ['other'] # 修改索引2后的元素为'other'
print(computer) # ['cpu', 'gpu', 'other']

print(len([1,2,3,4])) # 4 获取列表元素个数 
print(max([3,4,1,7])) # 7 获取列表元素最大值 
print(min(['n', 'f', 'g', 'l'])) # 'f' 获取列表元素最小值
print(list('hello')) # ['h', 'e', 'l', 'l', 'o'] 将字符串转换为列表 

tuple_create_int = (1, 2, 3, 4) # 创建一个元组
tuple_create_tuple = (0, (1, 2, 3), 4) # 创建嵌套元组
print(tuple_create_int) # (1, 2, 3, 4)
print(tuple_create_tuple) # (0, (1, 2, 3), 4)

print(len((1,2,3,4))) # 4 获取元组元素个数 
print(max((3,4,1,7))) # 7 获取元组元素最大值 
print(min(('n', 'f', 'g', 'l'))) # 'f' 获取元组元素最小值
print(tuple('hello')) # ('h', 'e', 'l', 'l', 'o') 将字符串转换为元组
print(tuple([1,2,3,4])) # (1, 2, 3, 4) 将列表转换为元组
print(list((1,2,3,4))) # [1, 2, 3, 4] 将元组转换为列表

people = {'name':'my name', 'age':30, 'height':178} # 定义字典
print(people) # {'name': 'my name', 'age': 30, 'height': 178}
person = {'xiaoming':{'age':28, 'height':176, 'city':'上海'}, 'xiaohei':{'age':30, 'height':174, 'city':'上海'}} # 嵌套字典
print(person) # {'xiaoming': {'age': 28, 'height': 176, 'city': '上海'}, 'xiaohei': {'age': 30, 'height': 174, 'city': '上海'}}
py = dict(name='Python', learn='simple') # 使用dict创建字典
print(py) # {'name': 'Python', 'learn': 'simple'}
print(people['name']) # my name, 通过'name'键获取值
print(person['xiaoming']) # {'age': 28, 'height': 176, 'city': '上海'}，获取字典中的字典
print(person['xiaoming']['city']) # 上海, 获取嵌套字典内的数据

py['learn'] = 'complex' # 修改键是’learn‘的元素
py['type'] = 'big data' # 键'type'不存在，添加新元素
print(py) # {'name': 'Python', 'learn': 'complex', 'type': 'big data'}

'''
clear
copy
get
items
keys
pop
popitem
setdefault
update
values
'''
py_copy = py.copy()
print(py_copy) # {'name': 'Python', 'learn': 'complex', 'type': 'big data'}

print(person.get('xiaoming')) # 获取’xiaoming‘对应的值
print(person.get('xiaolan')) # 当键不存在时，返回None表示没有
print(person.get('xiaolan', {'age':27, 'height':168, 'city':'杭州'})) # 当键不存在时，第二个参数即为默认值

print(list(people.items())) # [('name', 'my name'), ('age', 30), ('height', 178)]
print(list(py.items())) # [('name', 'Python'), ('learn', 'complex'), ('type', 'big data')]

print(list(people.keys())) # ['name', 'age', 'height']
print(list(person.keys())) # ['xiaoming', 'xiaohei']

print(people.pop('name')) # 删除'name'对应的值
print(people) # {'age': 30, 'height': 178}
#print(people.pop('a')) # 删除不存在的键会报错
print(people.pop('a', 1)) # 当传入第二个参数时，删除不存在的键时不会报错，返回指定的值

print(py) # {'name': 'Python', 'learn': 'complex', 'type': 'big data'}
print(py.popitem()) # ('type', 'big data') 随机删除
print(py) # {'name': 'Python', 'learn': 'complex'}
print(py.popitem()) # ('learn', 'complex') # 随机删除
print(py) # {'name': 'Python'}

print(py) # {'name': 'Python'}
py.update(a=1,b=2) # 当键值不存在时进行添加元素
print(py) # {'name': 'Python', 'a': 1, 'b': 2}
py.update({'a':'a', 'b':'b'}) # 当键值存在时进行更新元素
print(py) # {'name': 'Python', 'a': 'a', 'b': 'b'}

print(py) # {'name': 'Python', 'a': 'a', 'b': 'b'}
print(list(py.values())) # ['Python', 'a', 'b']

for color in ['红', '蓝', '黑', '白']:
    print('此时使用的颜色是：' + color)
print('颜色循环结束')

py = {'name': 'Python', 'learn': 'complex', 'type': 'big data'}
for key, value in py.items(): # 字典的items函数获得的是，每个键值对合成一个元组，这些元组组成了一个集合，而通过for循环就可以获得集合中的每个键值对
    print(key + ' 对应的值是 ' + value)
print('字典循环结束')

for index, var in enumerate(range(10, 16)):
    # enumerate函数获取集合中的值与对应的位置索引, 然后通过for循环依次取出
    print('位置 ' + str(index) + ' 的值是 ' + str(var) )
print('enumerate函数循环结束')

for i in range(10):
    if i%2 == 1:
        continue # 如果是奇数时进入下一次循环
    if i > 8:
        break # 如果取出的数字大于8时跳出循环
    print(i**2) # 打印数字的平方
print('循环结束')


def func_name():
    '''
    这里是函数的文档
    # 三个引号的字符串可作为多行注释
    '''
    print('这是一个无参函数')
    a = 1
    b = 2
    print('计算 a + b = ' + str(a+b))
    return a+b # return后面就是函数的返回值，若没有return, 接收返回值是空
# 上面定义了一个函数，但并不会被执行，只有调用才会执行
#func_name()

def output_info(name, age):
    '''
    name : 人名
    age : 年龄
    '''
    print('打印一个人的年龄')
    print(name + ' 的年龄是 ' + str(age))
# 调用函数
output_info('小明', 39)
# 可进行指定参数传入
output_info(age = 26, name = '小黑')

def learn(name, lang='Python'):
    print(name + ' 正在学习 ' + lang + ' 语言')
# 可以在参数指定一个值，若调用时不传入该参数，则使用默认
learn('小刚')
learn('小红', 'C')

def my_sum(a, c = 2, *b):
    # 加上星号的参数可以接收多个传入参数，并以元组保存
    print(b)
    sum = a
    for value in b:
        sum = sum + value # 将所有参数相加
    print(sum)
    return sum
sum_1 = my_sum(1,2,3,4)
print(sum_1)
sum_2 = my_sum(1,2,3,4,5)
print(sum_2)
    
def output_infos(name, **kwargs):
    '''
    两个星号的kwargs可以接收多个命名参数传入，并以字典形式保存
    '''
    print('个人信息：')
    for key, value in kwargs.items():
        print(name + ' 的 ' + str(key) + ' 信息为 ' + str(value))
output_infos('小明', age=28, height=178, addr='上海')

mul = lambda x,y: x*y # 定义匿名函数并赋值于变量s，调用s就是调用该匿名函数
result = mul(3, 4) # 接收匿名函数的返回值
print(result) # 12
'''
上面的匿名函数作用等效于下面的函数
def mil(x, y):
    return x*y
result = mul(3)
print(result)
'''
# 匿名函数的使用
result = map(lambda x:x*2, [1,2,3,4])
print(list(result)) # [2, 4, 6, 8]
'''
map函数第一个参数传入只有一个参数的函数，该参数函数对后面集合的每个元素进行操作
'''

class People:
    '''
    这里是People类的文档
    '''
    sex = '男' # People类具有性别属性，并且默认是男
    def __init__(self, name):
        '''
        类进行实例化调用此初始化函数
        '''
        self.name = name

    def set_age(self, age):
        '''
        设置一个人的年龄
        '''
        self.age = age

    def get_age(self):
        '''
        获取一个人的年龄
        '''
        if hasattr(self, 'age'): # hasattr函数判断一个类是否具有某属性
            return self.age
        else:
            print('未设置年龄，请调用set_age设置年龄')
            return None

    def get_sex(self):
        '''
        获取这个人的性别
        '''
        print(self.name + '的性别是' + self.sex)
        return self.sex

    def speak(self, msg):
        '''
        让这个人说一句话
        '''
        print(self.name + ' 说: ' + msg)
    def __add__(self, other):
        '''
        在对象进行相加操作时可以任意实现
        我们使用年龄相加后返回一个新的People对象
        '''
        if isinstance(other, People):
            if hasattr(self, 'age')  and hasattr(other, 'age'):
                age = self.age + other.age
                new_people = People(self.name + '与' + other.name + '相加对象')
                new_people.set_age(age)
                return new_people
            else:
                print('请检查年龄是否设置')
        else:
            print('人不能与非人对象相加')
            return None
    def __str__(self):
        info = self.name+'的性别是'+self.sex
        if hasattr(self, 'age'):
            info = info + ', 年龄是' + str(self.age)
        return info

xiaoming = People('小明') # 实例化类People的一个对象小明
# 调用类本身的属性sex
print(People.sex) # 正常获取性别
# print(People.name) 由于name是实例化才有的属性，该调用出错
print(xiaoming.sex) # 对象是具有类的属性的，正常
# 类中函数具有self的方法都是实例方法，对象才可以正常调用
xiaoming.set_age(29) # 正常设置小明的年龄
#People.set_age(29) # 报错

xiaoming.age = 20 # 通过实例对象设置年龄
print(xiaoming.age) # 通过实例对象获取年龄
xiaoming.sex = '女' # 通过实例对象设置性别
print(xiaoming.sex) # 通过实例对象获取性别
xiaoming.height = 178 # 给对象新建一个身高属性等于178
print(xiaoming.height) # 获取新建的属性

xm_age = xiaoming.get_age() # 通过对象方法获取年龄
print(xm_age)
xiaoming.speak('我在学习Python')

class Man(People):
    sex = '男'

class Women(People):
    sex = '女'

xiaohong = Women('小红') # 实例化一个Women小红
xiaohei = Man('小黑') # 实例化一个Man小黑
print(xiaohong.get_sex()) # 调用小红的获取性别方法，由于子类未实现该方法，则会调用父类的
print(xiaohei.get_sex()) # 调用小黑的获取性别方法
print(isinstance(xiaohei, Man)) # 使用isinstance函数判断xiaohei是否是Man的实例
print(isinstance(xiaohei, People)) # 由于Man继承自People，所以xiaohei也是People的实例
print(issubclass(Man, People)) # 使用issubclass判断Man是否是People的子类

xiaozi = People('小紫') # 实例化一个People对象小紫
xiaolan = People('小蓝') # 实例化一个People对象小蓝
#zilan = xiaozi+xiaolan # 作加法，由于没有设置年龄返回空值
xiaozi.set_age(24)
xiaolan.set_age(26)
zilan = xiaozi+xiaolan
print(zilan) # 小紫与小蓝相加对象的性别是男, 年龄是50
