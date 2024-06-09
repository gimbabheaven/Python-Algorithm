
def solution(str1, str2):
    result = []
    
    length = len(str1)
    
    for i in range(length):
        result.append(str1[i])
        result.append(str2[i])
    
    # 리스트를 문자열로 결합하여 반환
    return ''.join(result)