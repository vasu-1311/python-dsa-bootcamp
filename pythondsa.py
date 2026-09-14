# # student={"name":"vasu","age":33,"grade":1}
# # print(student)
# # keys=student.keys()
# # print(keys)
# # values=student.values()
# # print(values)
# # items=student.items()
# # print(items)
# # ##shallow copy
# # student_copy=student
# # print(student)
# # print(student_copy)
# # student["name"]="krishna"
# # print(student)
# # student_copu=student.copy()
# # student["name"]="vasu"
# # print(student)
# # print(student_copu)
# # #iterating over dictionaries
# # ##we can use loops to iterate over dict,keys values
# # for keys in student.keys():
# #     print(keys)
# # for values in student.values():
# #     print(values)
# # for keys,values in student.items():
# #     print(f"{keys}:{values}")
# #nested 
# # student={
# #     "student":{"name":"krish","age":23},
# #     "student2":{"name":"peter","age":34}

# # }
# # print(student)
# # print(student["student"]["name"])
# # print(student["student"]["age"])
# to_dist_list=["buy groceries","clean the house","pay bills"]
# #adding to  task
# to_dist_list.append("Schedule meeting")
# to_dist_list.append("go for a run")
# print(to_dist_list)
# to_dist_list.remove("clean the house")
# print(to_dist_list)
# if "pay bills" in to_dist_list:
#     print("dont forgot to pay the utility bills")

# grades=[56,67,89,90,88]
# grades.append(78)
# avarage_grade=sum(grades)/len(grades)
# print(avarage_grade)
# highest=max(grades)
# lowest=min(grades)
# print(highest)
# print(lowest)
# #managing the inventry
##FUNCTION'
# def function_name(parameters):
#     return expression
# def odd_even(num):
#     """find odd or even"""
#     if num%2==0:
#         print("number is even")
#     else:
#         print("number is odd")
# odd_even(5667)
#multiple  parameter
# def add(a,b):
#     return a+b
# result=add(4,7)

# print(result)
# #default parameters 
# def greet(name="guest"):
#     print(f"hello{name} welcome to the paradise")
# greet()
#variable length arugments
## positionl and keyword arguments
# def print_number(*args2):
#     for number in args:
#         print(number)
# print_number(1,3,4,5,6,7,89)
# def print_int( **kwargs):
#     for key,values in kwargs.items():
#         print(f"{key} {values}")
# print_int(name="lrish",age="32")
# def convert_tem(temp,unit):
# import numpy as np
# arrr2 = np.array([[1,2],[3,4]])
# newarr = np.insert(arrr2, 2, (8,6), axis=0)
# print(newarr)
# import numpy as np
# array_1=np.array([1,2])
# array_2=np.array([3,4])
# new_array1=np.concatenate((array_1,array_2))
# print(new_array1)
#removing element of arrya
# import numpy as np
# arr=np.array([1,2,3,4,5,6])
# arr=np.split(arr,2,axis=0)
# print(arr)
import pandas as pd
si=pd.Series(data=[100,120,130,150],index=list('abcd'))
print(si)
print(si.iloc[1]) 






