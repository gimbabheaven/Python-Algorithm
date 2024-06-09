def solution(my_string, overwrite_string, s):
    front_part = my_string[:s]
    back_part = my_string[s + len(overwrite_string):]
    return front_part + overwrite_string + back_part
