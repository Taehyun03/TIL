# 최댓값 만들기 
# 2026-10-02
# 처음 시도는 반복문과 .pop() 함수를 활용해 첫번째 큰수와 두번째 큰수를 곱하려고 했다
# 하지만 복잡하고 코드가 지저분하다.
def solution(numbers):
    max = numbers[0]
    k = 0
    for i in range(len(numbers)):
        if max < numbers[i]:
            max = numbers[i]
            k = i
    t = numbers.pop(k)
    min = numbers[0]
    for i in range(len(numbers)):
        if min < numbers[i]:
            min = numbers[i]
    return max * min

# 가장 쉬운방법 -> 그냥 정렬후에 -1, -2 번째 곱하면 됨
def solution(numbers):
    numbers.sort()
    return numbers[-2] * numbers[-1]
# 역 인덱싱 하는 것, 그리고 .sort() 정렬 메서드 기억해두자.