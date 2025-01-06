n1 = int(input("enter n1 value:"))

if(n1 < 10) or (n1 > 30):
    print(n1, "is not between 10 and 30")
    quit()
print(n1, "is between 10 and 30")

n2 = int(input("enter n2 value:"))
if(n2 < 10) or (n2 > 30):
    print(n2, "is not between 10 and 30")
    quit()
print(n2, "is between 10 and 30")

s = n1 + n2

d = n1 - n2

p = n1 * n2

m = n1 % n2

print("Sum:", s)
print("Diff:", d)
print("Prod:", p)
