# Области видимости
def f(a, b):
    a = 10
    print(a)


e = 1
f(e, 999)
# print(e)

a = 1
f(a, 999)
print(a)
  