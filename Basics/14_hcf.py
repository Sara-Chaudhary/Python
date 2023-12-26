def hcf(a,b):
    if b == 0:
        return a
    return hcf(b , a%b)

result=(hcf(48,18))
print("The hcf of 48 anf 18 is",result)