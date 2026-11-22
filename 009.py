def checksonguyento(number):
    if number== 1 or number==2 :
        return True
    for i in range(2,number):
        if number%i==0:
            return False
    return True

danhsach=[x for x in range(1,101)]
for i in danhsach:
    if checksonguyento(i):
        print(f'{i} là số nguyên tố')