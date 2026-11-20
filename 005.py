def average(score):
    sum = 0
    for i in score:
        sum += i
    value = sum/len(score)
    if value < 4 and value>=0:
        return 'yếu',value
    elif value >=4 and value < 5.5:
        return 'trung bình',value
    elif value >= 5.5 and value< 7:
        return 'khá',value
    elif value >= 7 and value < 8.5:
        return 'giỏi',value
    elif value >= 8.5 and value <= 10:
        return 'xuất sắc',value
try:
    r=True
    score = []
    name=str(input('Nhập tên của học sinh '))
    while r==True:
        n=int(input(f'Nhập số lượng môn học của {name} '))
        if n>0:
            r=False
        else:
            r=True
            print("Số lượng môn phải lớn hơn 0!")
    for i in range(n):
        h=1
        while h==1:
            k=float(input(f'Nhập điểm môn thứ {i+1}: '))
            if k < 0 or k>10:
                print("Hãy nhập điểm hợp lệ")
                h=1
            else:
                h=2
        score.append(k)
    a, b = average(score)
    print(f'Điểm trung bình của {name} là {b}')
    print(f"{name} là học sinh {a}")
except ValueError:
    print('Hãy nhập lại!')


