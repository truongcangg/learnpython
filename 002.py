value=0
while value<=0:
    value=int(input(" Enter a number:"))
    if value<=0:
        print(" the number is not positive, please enter a positive number.")
if value == 0:
    print(f'The number is zero.')
elif value%2==0:
    print(f'The number {value} is even.')
else:
    print(f'The number {value} is odd.')