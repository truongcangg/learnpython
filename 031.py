#Kiểu dữ liệu tuple:
'''
Về bản chât, khi ta khai báo 1 tuple thì trình quản lý bộ nhớ của pyhthon sẽ cấp cho chúng ta 1
vùng nhớ duy nhất liền mạch nhau trên ram để lưu header dính liền với 1 mảng con trỏ chứa các con trỏ
lưu địa chỉ dẫn đến vị trí của từng object 
-câu hỏi:Liệu cpu đóng vai trò gì ở đây?

Còn về list, tại vì nó còn có thêm khả năng mở rộng đến từ hàm append cho nên
khối header tách rời với khối con trỏ
'''
my_tuple= (1, 2, 3, 4, 5)
print('My tuple: ',my_tuple)
