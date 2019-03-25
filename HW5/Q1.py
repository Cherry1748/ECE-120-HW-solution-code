def f(h4,h3,h2,h1,h0):
    return ((~(h1^h3))|h4)&((~h2)|h4)&((~h0)|(~h1)|(~h2))&(h0|h1|h2|(~h4))&1


print(" h4,h3,h2,h1,h0, function value\n")
for i in range(24):
    h4,h3,h2,h1,h0 = '{:05b}'.format(i)
    h4 = int(h4)
    h3 = int(h3)
    h2 = int(h2)
    h1 = int(h1)
    h0 = int(h0)
    print("  ",h4," ",h3," ",h2," ",h1," ",h0," ",f(h4,h3,h2,h1,h0),i)
    