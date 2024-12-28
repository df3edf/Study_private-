import time

from 数据结构 import *


# import time
#
#
# test_num = 99999999
# # t1 = time.time()
# # for i in range(test_num):
# #     pass
#
# # print("time1:", time.time() - t1)
#
#
# ll = LinkList()
# ll.init_list(list(range(test_num)))
# t2 = time.time()
# ll.show_list()
# print("time2:", time.time() - t2)


# def euclid_algorithm(a, b, r):
#     """
#
#     :param a:  a num
#     :param b:  a unm
#     :param r:  remainder
#     :return:    common divisor
#     """
#
#     r = a % b
#     if r == 0:
#         return b
#     return euclid_algorithm(b, r, r)
#
# if __name__ == '__main__':
#     a = 224
#     b = 105
#     print(euclid_algorithm(b, a, -1))

# def gcd(a, b):
#     r = a % b
#     while r:
#         a = b
#         b = r
#         r = a % b
#
#     return b
#
#
# print(gcd(112232, 3172))

# import random
#
#
# def is_sort(list_):
#     for i in range(len(list_) - 1):
#         if list_[i] > list_[i+1]:
#             return False
#     return True
#
#
# def bogo_sort(list_):
#     time = 1
#     while True:
#         print(f"第: {time} 次排序。 列表为： ", end=' ')
#         for i in range(len(list_)-1, 0, -1):
#             change_index = random.randint(0, (i - 1))
#             list_[i], list_[change_index] = list_[change_index], list_[i]
#         time += 1
#         print(list_)
#         if is_sort(list_):
#             break
#
#
# list1 = [3, 4, 1, 9, 0, 5, 14, 34, 76, 12]
# bogo_sort(list1)
#
#
# def insertion_sorted(list_, time):
#     for index1 in range(1, len(list_)):
#         time += 1
#         key = list_[index1]
#         index2 = index1 - 1
#         # Move elements of list_[0.index1-1], that are greater than key,
#         # to one position ahead of their current position
#         while index2 >= 0 and list_[index2] > key:
#             list_[index2 + 1] = list_[index2]
#             index2 -= 1
#         list_[index2 + 1] = key
#         print(f"第: {time} 次排序。 列表为： ", end=' ')
#         print(list_)
#
#
# list1 = [3, 4, 1, 9, 0, 5, 14, 34, 76, 12]
# insertion_sorted(list1, 0)

# from multiprocessing import Process
# import time
#
#
# def sleep_sort(num, list_):
#     time.sleep(0.1*num)
#     list_.append(num)
#     print(num, end=' ')
#
#
# if __name__ == '__main__':
#     list2 = []
#     joins = []
#     list1 = [3, 4, 1, 9, 0, 5, 14, 34, 76, 12]
#     for num in list1:
#         p = Process(target=sleep_sort, args=(num, list2))
#         p.start()
#         joins.append(p)
#
#     for join_ in joins:
#         join_.join()
#
#     print('\n', list1)

# from multiprocessing import Process, Manager
# import time
#
#
# def sleep_sort(num, shared_list):
#     time.sleep(num / 10)  # More precise sleep
#     shared_list.append(num)
#
#
# if __name__ == '__main__':
#     with Manager() as manager:
#         shared_list = manager.list()
#         processes = []
#
#         list1 = [3, 4, 1, 9, 0, 5, 14, 34, 76, 12]
#
#         for num in list1:
#             p = Process(target=sleep_sort, args=(num, shared_list))
#             p.start()
#             processes.append(p)
#
#         for p in processes:
#             p.join()
#
#         print("Sorted list:", list(shared_list))


# def func(list_):
#     for i in range(10):
#         list_.append(i)
#
#
#
# list1 = []
# func(list1)
#
# print(list1)

# The sum of an arithmetic sequence

# def arithmetic_sum(first_term: int, d: int, n: int) -> int:
#     # Base case: if n is 0, sum is 0
#     if n == 0:
#         return 0
#     # Recursive case: sum of first n-1 terms plus the nth term
#     return first_term + arithmetic_sum(first_term + d, d, n - 1)
#
#
# # Example usage
# print(arithmetic_sum(4, 2, 6))

