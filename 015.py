#hàm tính tổng các chữ số của một số
def tongchuso(number):
    A= str(number)
    result=0
    for i in A:
        result += int(i)
    return result
try:
    number=int(input("Nhập số n: "))
    print(f'Tổng các chữ số của {number} là: {tongchuso(number)}')
except ValueError:
    print('Số đã nhập không hợp lệ!')

