a = 12
b = 18

temp1 = a
temp2 = b

while b:
    a, b = b, a % b

gcd = a

lcm = (temp1 * temp2) // gcd

print("LCM:", lcm)