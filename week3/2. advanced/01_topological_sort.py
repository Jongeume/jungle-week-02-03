"""
[위상 정렬 - Topological Sort]

문제 설명:
- 방향 그래프에서 순서를 정합니다.
- 선행 작업이 먼저 오도록 정렬합니다.
- 예: 과목 선수과목, 작업 순서

입력:
- graph: 방향 그래프
- vertices: 정점 개수

출력:
- 위상 정렬 순서

예제:
과목:
0(기초) → 1(중급) → 3(고급)
0(기초) → 2(응용)

위상 정렬: [0, 1, 2, 3] 또는 [0, 2, 1, 3]

힌트:
- 진입 차수(in-degree) 사용
- 진입 차수가 0인 정점부터 시작
- 큐 사용
"""

from collections import deque


def topological_sort(vertices, edges):
    """
    위상 정렬 (Kahn's Algorithm)

    Args:
        vertices: 정점 개수
        edges: (출발, 도착) 간선 리스트

    Returns:
        위상 정렬 순서
    """
    # TODO: 그래프와 진입 차수 초기화
    indgree = [0]*(vertices)
    graph = {v: [] for v in range(vertices+1)}
    que = deque()

    # TODO: 그래프 구성 및 진입 차수 계산
    for s, e in edges:
        graph[s].append(e)
        indgree[e] += 1

    # que = deque()
    # TODO: 진입 차수가 0인 정점들을 큐에 추가
    for i in range(vertices):
        if indgree[i] == 0:
            que.append(i)

    result = []

    # TODO: 큐가 빌 때까지 반복
    # 큐에서 정점 꺼내기
    # 인접한 정점들의 진입 차수 감소
    while que:
        current_vertices = que.popleft()
        if current_vertices not in result:
            result.append(current_vertices)
        for next_vertices in graph[current_vertices]:
            indgree[next_vertices] -= 1
            if indgree[next_vertices] == 0 and next_vertices not in que:
                que.append(next_vertices)

    # 사이클 감지
    return result if vertices == len(result) else print("사이클")


# 테스트 케이스
if __name__ == "__main__":
    # 과목 선수과목 예제
    vertices = 4
    edges = [
        (0, 1),  # 0 → 1
        (0, 2),  # 0 → 2
        (1, 3),  # 1 → 3
    ]

    print("=== 위상 정렬 ===")
    print("과목 관계:")
    print("  0(기초) → 1(중급) → 3(고급)")
    print("  0(기초) → 2(응용)")
    print()

    result = topological_sort(vertices, edges)
    print(f"수강 순서: {result}")
