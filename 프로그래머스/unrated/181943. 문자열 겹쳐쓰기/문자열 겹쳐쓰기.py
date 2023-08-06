def solution(my_string, overwrite_string, s):
    original = list(my_string)
    endnumber = len(overwrite_string)+s
    original[s:endnumber] = overwrite_string
    answer = "".join(original)

    return answer