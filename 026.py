import random




A=[i for i in range(100)]
random.shuffle(A)
print(A, ' ==> ')
A.sort(reverse=True)
print(A)