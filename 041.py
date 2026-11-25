'''
dictionary là kiểu dữ liệu mutable, bao gồm key và value, và vì được xây dựng
trên mảng băm ( Hash Table) nên nếu dùng toán tử in sẽ có độ phức tạp O(1)
Cú pháp:
my_dict={
    <key1> : <value1>,
    <key2> : <value2>,
          ...
     }
Các key phải là các immutable, nếu gán lại khóa đã tồn tại thì python sẽ giữ nguyên
vị trí khóa đó và ghi đè giá trị mới lên giá trị cũ
 Lưu ý: 1 == 1.0 == True và cả ba có cùng mã băm

 '''
my_dict = {}
my_dict['name'] = 'Cang'
my_dict[ 'year old'] = '18'
print(my_dict)