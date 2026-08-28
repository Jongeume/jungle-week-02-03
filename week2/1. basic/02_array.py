"""
[배열 - 2차원 배열 회전]

문제 설명:
- N x N 크기의 2차원 배열을 시계방향으로 90도 회전시킵니다.
- 배열의 인덱스 변환 규칙을 이해하는 문제입니다.

입력:
- matrix: N x N 크기의 2차원 리스트

출력:
- 시계방향으로 90도 회전된 2차원 리스트

예제:
입력:
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

출력:
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]

힌트:
- 회전 후 위치: (i, j) -> (j, n-1-i)
- 새로운 배열을 만들어 값을 채워넣으세요
"""


def rotate_matrix_90(matrix):
    """
    2차원 배열을 시계방향으로 90도 회전

    Args:
        matrix: N x N 2차원 리스트

    Returns:
        회전된 2차원 리스트
    """
    n = len(matrix)

    # TODO: n x n 크기의 새로운 배열을 생성하세요 (0으로 초기화)

    # newArr = []
    # for i in range(n):
    #     row = []
    #     for j in range(n):
    #         row.append(0)
    #     newArr.append(row)

    #  newArr = [[0]*n] * n
    #  얕은 복사이기에 [0, 0, 0] 인 하나의 리스트가 3개 들어감
    #  문제는 이 리스트가 같은 하나의 리스트여서
    #  리스트 안의 첫번째 값을 변경하면
    #  newArr[0][0] = 1
    #  [1, 0, 0]
    #  [1, 0, 0]
    #  [1, 0, 0]
    #  모든 행의 첫번째 값이 변경이 된다.

    newArr = [[0] * n for _ in range(n)]
    # print(newArr)
    # TODO: 원본 배열의 각 요소를 회전된 위치에 배치하세요
    # 힌트: (i, j) 위치의 요소는 회전 후 (j, n-1-i) 위치로 이동
    for i in range(n):
        for j in range(n):
            newArr[j][n-1-i] = matrix[i][j]
    # print(newArr)

    return newArr


def print_matrix(matrix):
    """배열을 보기 좋게 출력하는 헬퍼 함수"""
    for row in matrix:
        print(row)


# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1: 3x3 배열
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print("원본 배열:")
    print_matrix(matrix1)
    print("\n회전 후:")
    rotated1 = rotate_matrix_90(matrix1)
    print_matrix(rotated1)
    print()

    # 테스트 케이스 2: 4x4 배열
    matrix2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    print("원본 배열:")
    print_matrix(matrix2)
    print("\n회전 후:")
    rotated2 = rotate_matrix_90(matrix2)
    print_matrix(rotated2)
