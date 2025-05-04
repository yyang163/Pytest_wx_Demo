# 字符串拼接语法
# s1 = 72
# s2 = 85
# r = (s2 - s1) / s1 * 100
# print(f"小明的成绩提升了{r:.1f}")
# n = 123
# f = 456.789
# s1 = 'Hello, world'
# s2 = 'Hello, \'Adam\''
# s3 = r'Hello, "Bart"'
# s4 = r'''Hello,
# Bob!'''
# print(s2)
import inspect


# 列表切片
# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Bob']
# ]
#
# # 打印Apple:
# print(L[0][0])
# # 打印Python:
# print(L[1][1])


# 打印变量类型
# a = ()
# b = (1)
# c = [2]
# d = (3,)
# e = (4, 5, 6)
# print(type(e))

# if else语句
# age = 3
# if age >= 18:
#     print('adult')
# elif age >= 6:
#     print('teenager')
# else:
#     print('kid')
# age = 20
# if age >= 6:
#     print('teenager')
# elif age >= 18:
#     print('adult')
# else:
#     print('kid')
# hight = 1.75
# weight = 80.5
# bmi = weight / (hight ** 2)
# if bmi < 18.5:
#     print("体重过轻")
# elif bmi > 18.5 and bmi < 25:
#     print("体重正常")
# elif bmi > 25 and bmi < 28:
#     print("重")
# elif bmi > 28 and bmi < 32:
#     print("肥")
# elif bmi > 32:
#     print("超肥")
# else:
#     print("找不到")
# hight = float(input("请输入hight："))
# weight = float(input("请输入weight："))
# bmi = weight / (hight ** 2)
# if bmi < 18.5:
#     print("体重过轻")
# elif bmi > 18.5 and bmi < 25:
#     print("体重正常")
# elif bmi > 25 and bmi < 28:
#     print("重")
# elif bmi > 28 and bmi < 32:
#     print("肥")
# elif bmi > 32:
#     print("超肥")
# else:
#     print("找不到")
# score = 60
# if score == 30:
#     print(f'score is {score}')
# elif score == 40:
#     print(f'score is {score}')
# elif score == 60:
#     print(f'score is {score}')
# else:
#     print('invalid score.')


# math case用法
# score = 70
#
# match score:
#     case 40:
#         print(f'score is {score}')
#     case 50:
#         print(f'score is {score}')
#     case 60:
#         print(f'score is {score}')
#     case _: # _表示匹配到其他任何情况
#         print('score is ???.')
# age = int(input("请输入年龄:"))
#
# match age:
#     case x if x < 10:
#         print(f'年龄为： {x}')
#     case 10:
#          print(f'年龄为： {age}')
#     case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
#          print(f'年龄为11~18 years old')
#     case 19:
#          print(f'年龄为： {age}')
#     case _:
#         print('not sure.')
# args = ['gcc', 'hello.c','acc','bdd']
# match args:
#     # 如果仅出现gcc，报错:
#     case ['gcc']:
#         print('false')
#     case ['gcc', 'hello.c',a1]:
#         print('true')
#     case _:
#         print("找不到")

# 出现gcc，且至少指定了一个文件:
# case ['gcc', file1, *files]:
#     print('gcc compile: ' + file1 + ', ' + ', '.join(files))
# # 仅出现clean:
# case ['clean']:
#     print('clean')
# case _:
#     print('invalid command.')


# 循环用法
# args = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sum=0
# for x in args:
#     sum=sum+x
#     print(sum)

# sum =0
# for i in range(101):
#    sum=sum+i
#    print(sum)

# sum = 0
# n = 99
# while n > 0:
#     sum = sum + n
#     n = n - 2
# print(sum)


# sum_odd = sum(range(1, 101, 2))  # 从1开始，步长为2
# print("100以内所有奇数之和:", sum_odd)
# L = ['Bart', 'Lisa', 'Adam']
# for x in L:
#     print(f'HELLO {x}')
# n = 1
# while n <= 100:
#     print(n)
#     n = n + 1
# print('END')
# n = 1
# while n <= 100:
#     if n > 10: # 当n = 11时，条件满足，执行break语句
#         break # break语句会结束当前循环
#     print(n)
#     n = n + 1
# print('END')
# d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# print([d.get('Bob', None)])
# print([d.get('pyttrb', None)])

# 转换成十六进制 hex函数
# n1 = 255
# n2 = 1000
# print(hex(n2))


# 定义函数
# 一元二次方程求解
# import math
#
#
# def quadratic(a, b, c):
#     # 计算判别式的值
#     discriminant = (b ** 2) - (4 * a * c)
#     # 检查判别式的值
#     if discriminant < 0:
#         return None  # 没有实数解
#     elif discriminant == 0:
#         # 一个实数解
#         return -b / (2 * a)
#     else:
#         # 两个实数解
#         root1 = (-b + math.sqrt(discriminant)) / (2 * a)
#         root2 = (-b - math.sqrt(discriminant)) / (2 * a)
#         return root1, root2


# 求函数x的n次方
# x=int(input("请输入x的值:"))
# n=int(input("请输入n的值:"))
# def power(x, n):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
# print( power(x, n))


# 求a2 + b2 + c2 + …
# 方法一：

# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum =sum+( n * n)
#     return sum
#
# # 调用函数时可以传入任意数量的参数
# print(calc(1,2,3))  # 输出: 14
# print(calc())  # 输出: 0


# 方法二：
#
# def calc_square_sum(*numbers):
#     total = 0
#     for n in numbers:
#         total += n * n  # 计算每个数的平方并累加
#     return total
#
# # 测试函数
# result = calc_square_sum(1, 2, 3, 4)  # 1² + 2² + 3² + 4² = 1 + 4 + 9 + 16 = 30
# print(result)  # 输出: 30

# 递归函数 n！=1*2*3*...*n
# def fact(n):
#     if n==1:
#         return 1
#     return n * fact(n - 1)
# print(fact(2))


# def queryDetailAllList(m, n):
#     print("调用a方法:参数m = " + m)
#     print("调用a方法:参数m = " + n)
#     # raise '错误了'
#
#
# def assertAsync(request, **kwargs):
#     func = inspect.signature(request)
#     request_params, assert_params = dict(), dict()
#     for name, value in kwargs.items():
#         for k, v in func.parameters.items():
#             if name == k:
#                 request_params[name] = value
#             else:
#                 if name not in func.parameters.keys():
#                     assert_params[name] = value
#
#     # print(func.parameters.items())
#     # print(kwargs['m'])
#     request(**request_params)
#
#
# assertAsync(queryDetailAllList, m="30", n="30", sum=60)

# queryDetailAllList("20")


# def my_sum(nums, times):
#     total = 0
#     for i in range(times):
#         for j in nums:
#             total = total + j
#     return total
#
#
# aa = [1, 2, 3]
# bb = 3
# cc=my_sum(aa, bb)
# print(cc)

#计算器
#请输入两个数和一个符号，完成两个数的+ - * / %  // **
a=int(input("请输入第一个数:"))
b=int(input("请输入另一个数:"))
c=str(input("请输入+ - * / %  // ** 中任意一个运算符:"))
