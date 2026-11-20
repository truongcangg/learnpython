def bangcuuchuong():
    for i in range(2,10):
        for j in range(2,10):
            print(f"{j} x {i} = {i*j}", end="     ")
        print(end='\n')
print(bangcuuchuong())