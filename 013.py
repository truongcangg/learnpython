def songuyento(n):
    if n <=1:
        return False
    elif n==2 or n==3 :
        return True
    elif n%2==0 or n%3==0 :
        return False
    for i in range(5,int(n**0.5)):
        if n%i==0:
            return False
    return True
try:
    n=int(input("Nhập số nguyên bạn mốn kiểm thử: "))
    if songuyento(n)==True:
        print(f'{n} là số nguyên tố')
    elif songuyento(n)==False:
        print(f'{n} không phải là số nguyên tố')
except ValueError:
    print('Số đã nhập không hợp lệ')