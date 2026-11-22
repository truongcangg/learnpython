A=[i for i in range(100)]
n=int(input('Nhập phần tử bạn muốn xóa khỏi danh sach: '))
if n in A:
    A.remove(n)
    print(A)
else:
    print(f'Phần tử {n} không có trong danh sách')