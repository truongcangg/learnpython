#hàm kiểm tra một chuỗi có phải là palindrome không
def check(chuoi):
    for i in range(int(len(chuoi)/2)):
        if chuoi[i] == chuoi[len(chuoi)-i-1]:
            continue
        else:
            return False
    return True
try:
    chuoi=input('Nhập một chuỗi bất kì: ')
    if check(chuoi):
        print(f'{chuoi} là một chuỗi palindrome')
    else:
        print("Chuỗi vừa nhập không phải một chuỗi palindrome")
except ValueError:
    print("Lỗi khi nhập dữ liệu!")

