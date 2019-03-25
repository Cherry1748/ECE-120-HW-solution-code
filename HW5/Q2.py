def w(b, s0,s1,s2):
    return s1&b&(s0|(~s2))&1


def x(b, s0,s1,s2):
    return s2&(~s0)&1


def y(b, s0,s1,s2):
    return (s0|(~s2))&(s1|(~b))&(s0|b)&1


def z(b, s0,s1,s2):
    return (s0|b)&(s2|(~s1)|b)&(s2|(~s1)|s0)&((~s2)|(~s0)|(~b))&1


import itertools


a = [0,1]
for i in itertools.product(a,repeat =4):
    b, s0,s1,s2 = i
    print(b, s0,s1,s2,"|",w(b, s0,s1,s2),x(b, s0,s1,s2),y(b, s0,s1,s2),z(b, s0,s1,s2))