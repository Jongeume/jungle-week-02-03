"""
[그리디 - 회의실 배정]

문제 설명:
- 하나의 회의실에 여러 회의를 배정합니다.
- 각 회의는 시작 시간과 종료 시간이 있습니다.
- 최대한 많은 회의를 배정하려고 합니다.

입력:
- meetings: [(시작, 종료), ...] 회의 리스트

출력:
- 배정된 회의 개수

예제:
입력: [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
출력: 4개
선택: [(1, 4), (5, 7), (8, 11), (12, 14)]

힌트:
- 종료 시간이 빠른 회의부터 선택!
- 이전 회의가 끝난 후에 시작하는 회의만 선택
"""


def select_meetings(meetings):
    """
    회의실 배정 (그리디)

    Args:
        meetings: [(시작, 종료)] 리스트

    Returns:
        (배정된 회의 개수, 선택된 회의 리스트)
    """
    # # TODO: 회의가 없으면 0 반환
    # if not meetings:
    #     return 0

    # # TODO: 종료 시간 기준으로 정렬
    # meetings.sort(key=lambda x: x[1])

    # selected = []

    # # TODO: 첫 번째 회의 선택
    # selected.append(meetings[0])

    # # TODO: 나머지 회의들 확인
    # # 이전 회의가 끝난 후 시작하는 회의만 선택
    # i = 0
    # for s, e in meetings[1:]:
    #     if selected[i][1] < s:
    #         i += 1
    #         selected.append((s, e))

    # return len(selected), selected

    # sorted를 사용했을 때
    if not meetings:
        return 0

    sorted_meetings = sorted(meetings, key=lambda x: (x[1], x[0]))

    selected = []

    selected.append(sorted_meetings[0])

    last_end_time = sorted_meetings[0][1]
    for s, e in meetings[1:]:
        if s >= last_end_time:
            selected.append((s, e))
            last_end_time = e

    return len(selected), selected


# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    meetings1 = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9)]
    count1, selected1 = select_meetings(meetings1)
    print("=== 테스트 케이스 1 ===")
    print(f"전체 회의: {meetings1}")
    print(f"배정된 회의 개수: {count1}개")
    print(f"선택된 회의: {selected1}")
    print()

    # 테스트 케이스 2
    meetings2 = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9),
                 (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
    count2, selected2 = select_meetings(meetings2)
    print("=== 테스트 케이스 2 ===")
    print(f"전체 회의: {len(meetings2)}개")
    print(f"배정된 회의 개수: {count2}개")
    print(f"선택된 회의: {selected2}")
