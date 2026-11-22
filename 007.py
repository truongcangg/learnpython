def namnhuan(nam):
    if nam%4==0 and nam %100==0:
        print(f'Năm {nam} là năm nhuận')
    elif nam%400==0:
        print(f'Năm {nam} l55à năm nhuận')
    else:
        print(f'Năm {nam} không phải năm nhuận')

try:
    nam=int(input('Nhập năm bạn muốn tra cứu: '))
    namnhuan(nam)
except ValueError:
    print('Năm nhập không hợp lệ!')

