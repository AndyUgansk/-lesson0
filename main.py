# 1st program
print(9 ** 0.5 * 5)
# 2nd program  variant 1
if 9.99 > 9.98 and 1000 != 1000.1:
    print(True)
else:
    print(False)
# 2nd program variant 2
print(9.99 > 9.98 and 1000 != 1000.1, "(второй вариант решения)")
# 3rd program
a = 1234
b = 5678
a1 = a % 1000 // 10
b1 = b % 1000 // 10
print(a1 + b1)
# 4th program
a = 13.42
b = 42.13
a1 = int(a // 1)
a2 = int(a*100-a1*100)
b1 = int(b // 1)
b2 = int(b*100-b1*100)
print(a1==b2 or a2==b1)