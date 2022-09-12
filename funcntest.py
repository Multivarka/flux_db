# 
# def set_num1(num1=None):
#     num_1 = 10
#     print(num_1,' first')
#     if num1:
#         num_1 = num1
#         print(num_1,' second')
#         return num_1
#     print(num_1,' no created')
#     return num_1
# def num2():
#     print(set_num1())
#     num1 = 20
#     print(set_num1(num1))
# 
# 
# num2()

from test import Test

object_delete = Test()
print(object_delete.get_delete_num())
object_delete.set_delete_num(10)
print(object_delete.get_delete_num())
print(object_delete.get_delete_num())
object_delete = Test()
print(object_delete.get_delete_num())