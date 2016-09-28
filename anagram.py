import re
from collections import defaultdict
def anagram(s1,s2):
    s1new =re.findall("\w",s1.upper())
    s2new =re.findall("\w",s2.upper())
    if len(s1new) != len(s2new ):
        return False
    else :
        dict = {}
        for i in s1new :

            if dict.has_key(i):
                dict[i] +=1
            else :
                dict[i] =1

        for j  in s2new:
            if dict.has_key(j) :
                dict[j] -= 1
            else:
                dict[j] = 1
    valueset = dict.values()
    print valueset
    print sum(valueset)
    if sum(valueset) ==0 :

        return True
    else :
        return False




s1 = "a b c a"
s2= "bc da"
print anagram('clint eastwood','old west action')