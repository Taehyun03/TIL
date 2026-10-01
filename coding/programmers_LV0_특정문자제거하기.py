# 특정 문자 제거하기
# 2026-10-01
# 처음 시도는 받은 문자열의 길이만큼 for문을 사용해 각 자릿마다 letter와 비교해 같으면 제외하려고 했다.
# 하지만 문자열은 한 글자만 골라서 바꿀 수 없다.

def solution(my_string, letter):
    result = ''
    for i in range(len(my_string)):
        if my_string[i] != letter:
            result += my_string[i]
            
    return result

# 빈 문자열에 더하는 방법 채택 (letter가 아닐때만) 문자열도 결국 순서가 존재.
