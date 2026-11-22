def findmax(danhsach):
    max = 0
    for i in danhsach:
        if i>max:
            max=i
    return max
try:
    danhsach = []
    n=int(input('Nhập số các số của danh sách: '))
    for i in range(n):
        k=int(input(f'Nhập số nguyên thứ {i+1} : '))
        danhsach.append(k)
    print(f'Số lớn nhất trong danh sách là: {findmax(danhsach)}')
except ValueError:
    print("Số đã nhập không hợp lệ!")