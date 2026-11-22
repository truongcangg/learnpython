def count(danhsach):
    chan=0
    le=0
    for i in danhsach:
        if i%2==0:
            chan+=1
        else:
            le+=1
    return le,chan
try:
    danhsach=[]
    n=int(input('Số lượng số bạn muốn nhập:'))
    for i in range(n):
        k=int(input(f'Nhập số nguyên thứ {i+1} '))
        danhsach.append(k)
    le,chan=count(danhsach)
    print('Số số lẻ:',le)
    print('Số số chẵn: ',chan)
except ValueError:
    print('Số đã nhập không hợp lệ!')