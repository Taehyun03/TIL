# 모음 제거
# 2026-10-02
# 최대한 문자열을 잘 갖고 놀아야 하는 문제
# replace 메서드를 활용한다. 

def solution(my_string):
    words = ['a','e','i','o','u']
    for word in words:
        my_string = my_string.replace(word,"")
    return my_string