def m1():
    a = [1, 2, 7, 11]
    dict1 = {"a": 1, "b": 3}
    dict2 =1
    target = 18
    for i in range(0, len(a)):
        for j in range(i + 1, len(a)):
            print(f"当前循环 i = {i}, j = {j}")
            if a[i] + a[j] == target:
                print(i, j)
                return


m1()

# def twoSum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):  # 嵌套for循环，遍历数组中的每一个数，并且i不能等于j
#             if target == nums[i] + nums[j]:  # 如果符合题目要求（这里注意if要用比较运算符==）
#                 return [i, j]  # 就输出结果

a=[1,2,3,4]
b=a.index(2,1,3)
print(b)