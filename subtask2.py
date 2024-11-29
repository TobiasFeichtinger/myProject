n = 0
s = 0
m = 10**31

while True:
    x = int(input("Type in a sequence of numbers seperated by , and terminated by -1: "))
    if x == -1:
        break
    n = n + 1
    s = s + x
    if m > x:
        m = x
n = n - 1

if n == 0:
    m = -1
    a = -1
    s = 0
else:
    a = s/n

print(f"Count n is: {n}")
print(f"Sum s is: {s}")
print(f"Minimum m is: {m}")
print(f"Mean a is: {a}")
