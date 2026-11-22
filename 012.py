#hàm tính tổng các số từ 1 đến n
def tong(n):
    value = 0
    for i in range(1,n+1):
        value += i
    return value
try:
    while 1:
        n =int(input('Nhập số nguyên dương n: '))
        if n>0:
            break
        else:
            print('Hãy nhập số nguyên lớn hơn 0')
    print(f'Tổng các số từ một đến {n} là: {tong(n)}')
except ValueError:
    print('Số đã nhập không hợp lệ!')
