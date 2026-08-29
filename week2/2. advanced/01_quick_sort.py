"""
[퀵 정렬 구현]

문제 설명:
- 퀵 정렬(Quick Sort) 알고리즘을 구현합니다.
- 분할 정복(Divide and Conquer) 방식을 사용합니다.
- 피벗(pivot)을 기준으로 작은 값과 큰 값을 분할하여 재귀적으로 정렬합니다.

입력:
- arr: 정렬되지 않은 정수 배열

출력:
- 오름차순으로 정렬된 배열

예제:
입력: [10, 7, 8, 9, 1, 5]
출력: [1, 5, 7, 8, 9, 10]

힌트:
[Lomuto Partition]
- 피벗 선택 (일반적으로 마지막 원소)   
- 피벗보다 작은 원소는 왼쪽, 큰 원소는 오른쪽으로 분할
- 재귀적으로 왼쪽과 오른쪽 부분 정렬

[Hoare Partition] 
"""


def partition(arr, low, high):
    """
    배열을 피벗 기준으로 분할하는 함수

    Args:
        arr: 배열
        low: 시작 인덱스
        high: 끝 인덱스

    Returns:
        피벗의 최종 위치 인덱스
    """
    pivot = arr[high]
    i = low-1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


def quick_sort_helper(arr, low, high):
    """
    퀵 정렬 재귀 함수

    Args:
        arr: 배열
        low: 시작 인덱스
        high: 끝 인덱스
    """
    # TODO: base case - low가 high보다 작을 때만 정렬
    if low < high:
        # 분할하여 피벗 인덱스 얻기
        pivotIndex = partition(arr, low, high)
    # 피벗 왼쪽 부분 재귀 정렬
        quick_sort_helper(arr, low, pivotIndex-1)
    # 피벗 오른쪽 부분 재귀 정렬
        quick_sort_helper(arr, pivotIndex+1, high)


def quick_sort(arr):
    """
    퀵 정렬 메인 함수

    Args:
        arr: 정렬할 배열

    Returns:
        정렬된 배열
    """
    quick_sort_helper(arr, 0, len(arr) - 1)
    return arr


# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    arr1 = [10, 7, 8, 9, 1, 5]
    print("=== 테스트 케이스 1 ===")
    print(f"정렬 전: {arr1}")
    result1 = quick_sort(arr1.copy())
    print(f"정렬 후: {result1}")
    print()

    # 테스트 케이스 2
    arr2 = [64, 34, 25, 12, 22, 11, 90]
    print("=== 테스트 케이스 2 ===")
    print(f"정렬 전: {arr2}")
    result2 = quick_sort(arr2.copy())
    print(f"정렬 후: {result2}")
    print()

    # 테스트 케이스 3: 중복 ~원소
    arr3 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print("=== 테스트 케이스 3: 중복 원소 ===")
    print(f"정렬 전: {arr3}")
    result3 = quick_sort(arr3.copy())
    print(f"정렬 후: {result3}")
    print()

    # 테스트 케이스 4: 이미 정렬된 배열
    arr4 = [1, 2, 3, 4, 5]
    print("=== 테스트 케이스 4: 이미 정렬됨 ===")
    print(f"정렬 전: {arr4}")
    result4 = quick_sort(arr4.copy())
    print(f"정렬 후: {result4}")
    print("이미 정렬된 경우 O(n²) 시간 소요 (최악의 경우)")
