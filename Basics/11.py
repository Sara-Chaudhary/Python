def fun(x):
    if not x:
        return 0
    else:
        return 1 + fun(x[1:])
print(fun([3,4,5,6,7, "hi"]))







