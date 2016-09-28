def uni_char(str):
    dict={}
    cnt=0
    for i in str:
        if dict.has_key(i):
            return False
        else:
            dict[i]=1
            cnt+=1
    if cnt == len(str):
        return True


print uni_char("absde")