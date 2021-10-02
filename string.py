def reverse_string(strng):
    rev_str = ''
    for i in strng:
        rev_str = i + rev_str
        
    return rev_str
        


def is_sub_string_or_not(sub, main_str):
    result=False
    for i in range(0, (len(main_str) - len(sub)+1)): #exhaustive iterable
        if main_str[i] == sub[0]:           
            if sub== main_str[i:i+len(sub)]:
                result=True
                break
    return result
