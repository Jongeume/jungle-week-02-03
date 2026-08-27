"""
[우선순위 큐 - 응급실 환자 관리]

문제 설명:
- 우선순위 큐를 사용하여 환자를 우선순위에 따라 처리합니다.
- 숫자가 작을수록 우선순위가 높습니다 (1 > 2 > 3).

입력:
- patients: (이름, 우선순위) 튜플 리스트

출력:
- 우선순위에 따라 처리된 환자 순서

예제:
입력: [("김철수", 3), ("이영희", 1), ("박민수", 2)]
출력:
처리: 이영희 (우선순위: 1)
처리: 박민수 (우선순위: 2)
처리: 김철수 (우선순위: 3)

힌트:
- heapq 모듈 사용
- heappush(): 힙에 추가
- heappop(): 최소값 제거
"""

import heapq

def process_emergency_room(patients):
    """
    환자를 우선순위에 따라 처리
    
    Args:
        patients: (이름, 우선순위) 리스트
    
    Returns:
        처리된 환자 순서
    """
    # TODO: 빈 힙 생성
    heap = []
    
    
    # TODO: 모든 환자를 힙에 추가
    pass
        
    processed = []
    
    # TODO: 힙이 비어있지 않은 동안 반복
    ## 힙에서 우선순위가 가장 높은 환자 꺼내기
    ## 환자 처리
    pass
        
    return processed

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    patients1 = [
        ("김철수", 3),
        ("이영희", 1),
        ("박민수", 2)
    ]
    print("=== 응급실 환자 처리 ===")
    result1 = process_emergency_room(patients1)
    print(f"처리 순서: {result1}")
    print()
    
    # 테스트 케이스 2
    patients2 = [
        ("환자A", 5),
        ("환자B", 1),
        ("환자C", 3),
        ("환자D", 2)
    ]
    print("=== 응급실 환자 처리 ===")
    result2 = process_emergency_room(patients2)
    print(f"처리 순서: {result2}")


