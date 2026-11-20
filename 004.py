def cost(km):
    if km >= 0 and km <= 1:
        return 10000*km
    elif km > 1 and km <= 10:
        return 8500*km
    elif km > 10:
        return 7500*km
while True:    
    try:
        km = float(input("Nhập số km đã đi:"))
        print(f"Tổng tiền phải trả:{cost(km)} VNĐ")
    except ValueError:
        print("Lỗi, yêu cầu nhập số hợp lệ")
        
