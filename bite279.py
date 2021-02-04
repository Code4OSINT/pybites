# Armstrong numbers
n = 2020
digits = list(str(n))
power = len(digits)
an = 0
for i in digits:
    an += int(i) ** power
    print(i,power, an)
if an == n:
    print("Yes")
else: print("False")

# Beter/korter:
print(n==an)
