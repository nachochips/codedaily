def solution(str1, str2):
    answer = ""
    l = len(str1)
    for i in range(l):
        answer += (str1[i] + str2[i])     
    return answer


#improved version by Chat GPT 
def solution(str1, str2):
    answer = [str1[i] + str2[i] for i in range(len(str1))]
    return ''.join(answer)
