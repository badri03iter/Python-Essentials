def sentence_reversal(str1):
    val = str1.strip().split()

    reversal_str = []
    i = len(val)- 1
    while i >=0 :
        reversal_str.append(val[i])
        i-=1

    str_ret = " ".join(reversal_str)
    return str_ret



str = 'Hi John,   are you ready to go?'
print sentence_reversal(str)