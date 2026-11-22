import random

A = [random.randint(1,5) for i in range(20)]
try:
    n=int(input("Nhập phần tử bạn muốn đếm: "))
    print(f'{n} xuất hiện {A.count(n)} lần trong {A}')
except ValueError:
    print('Số bạn đã nhập không hợp lệ!')