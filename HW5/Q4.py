def B(a,b,c,d):
    return ((a&b&c)|((~a)&(~b)&d)|((~a)&(~c)))&1


def C(a,b,c,d):
    return (((~a)|b)&((~c)|d)&((~a)|(c))&(a|(~b)|(~c)))&1


import itertools
s = [0,1]
for i in itertools.product(s,repeat =4):
    a,b,c,d = i
    print(a,b,c,d,"|",B(a,b,c,d),C(a,b,c,d))