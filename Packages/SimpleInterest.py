from calc import mul, div

p = int(input("Enter principal: "))
r = int(input("Enter rate: "))
t = int(input("Enter time: "))

result = mul(p, r)
result = mul(result, t)
si = div(result, 100)

print("Simple Interest is:", si)