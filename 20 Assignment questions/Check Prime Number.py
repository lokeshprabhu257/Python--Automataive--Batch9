n = int(input())
if n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1)):
    print("Prime")
else:
    print("Not Prime")
