S = float(input("S: "))
a = float(input("a: "))
e = float(input("e: "))

ans = ((1-a)*S/e*5.67e-8)
print(ans)
new = ans ** 0.25
print("T = {:.2f}".format(new))