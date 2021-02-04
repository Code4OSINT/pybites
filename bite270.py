# Most frequent digit in number
# from collections import defaultdict

num = 2020
digits = list(str(num))
dig = {}
for i in range(0, len(digits), 1):
    print(f"i = {i}")
    if digits[i] in dig:
        print(digits[i])
        dig[digits[i]] += 1
    else:
        dig[digits[i]] = 1
print(int(max(dig, key = lambda key: dig[key])))

