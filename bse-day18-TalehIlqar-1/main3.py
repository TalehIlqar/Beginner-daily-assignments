from math import isqrt
class fucto():
    def factorial(self, n):
        cem = 1
        for i in range(2, n+1):
            cem *= i
        return cem

    def sum(self, n):
        cem = 0
        for i in range(1, n+1):
            cem+=i
        return cem

    def testPrim(self, n):
        for i in range(2, isqrt(n) + 1):
            if n%i == 0:
                return False
        return True

        


eded = int(input())
c = fucto()
print(c.factorial(eded))

print(c.sum(eded))

print(c.testPrim(eded))