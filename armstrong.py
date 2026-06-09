n = int(input())

temp = n
sum = 0
digits = len(str(n))

while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp //= 10

if sum == n:
    print("Armstrong")
else:
    print("Not Armstrong")