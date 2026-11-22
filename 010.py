def ucln(a,b):
    if a==b:
        return a
    elif a<b:
        k=1
        for i in range(1,a+1):
            if b%i==0 and a%i==0:
                k=i
        return k
    else:
        j=1
        for i in range(1,b+1):
            if a%i==0 and b%i==0:
                j=i
        return j
try:
    a=int(input('Nhập số nguyên a: '))
    b=int(input('Nhập số nguyên b: '))
    print('UCLN của a và b là :', ucln(a,b))
except ValueError:
    print("Hãy nhập số nguyên!")
