import os

a = os.path.dirname(os.path.abspath(__file__))
print(a)
b = os.path.join(a, "../")
print(b)
