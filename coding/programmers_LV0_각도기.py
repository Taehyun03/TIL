# 각도기
# 2026-10-01
# easy
def solution(angle):
    if 0 < angle < 90:
        angle = 1
    elif angle == 90:
        angle = 2
    elif 90 < angle < 180:
        angle = 3
    else:
        angle = 4
    return angle


def solution(angle):
    if angle<=90:
        return 1 if angle<90 else 2
    else:
        return 3 if angle<180 else 4
# 고인물들은 이렇게 함
# 핵심 문법: 값A if 조건 else 값B -> 조건이 참이면 A 거짓이면 B