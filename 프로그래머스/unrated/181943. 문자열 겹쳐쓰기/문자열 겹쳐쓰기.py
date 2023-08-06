def solution(my_string, overwrite_string, s):
    original = list(my_string)
    overwrite = list(overwrite_string)
    endnumber = len(overwrite_string)+s
    original[s:endnumber] = overwrite
    answer = "".join(original)

    return answer