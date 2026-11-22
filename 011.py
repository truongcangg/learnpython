#hàm tính giai thừa của 1 số n nguyên dương


def giaithua(n):
    result=1
    for i in range(1,n+1):
        result *= i
    return result
try:
    while 1:
        n=int(input('Nhập một số nguyên dương: '))
        if n>0:
            print(f'Giai thừa của {n} là {giaithua(n)}')
            break
        else:
            print("Dữ liệu bạn nhập không hợp lệ, hãy nhập lại!")
except ValueError:
    print('Dữ liệu nhập không hợp lệ!')

