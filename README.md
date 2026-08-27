# SW-AI 컴퓨팅 사고로의 전환 - 레포지토리 템플릿 (Week 2 / Week 3)

## 📂 폴더 구조

```
SW-AI-W02-03-TEMPLATE/
├── week2/
│   ├── 1. basic/             # 기본 개념 학습 (총 15개 문제)
│   │   ├── 01_string.py             # 문자열 (가장 친숙한 자료형부터)
│   │   ├── 02_array.py              # 배열
│   │   ├── 03_python_dict.py        # 파이썬 기본 문법 (딕셔너리)
│   │   ├── 04_brute_force.py        # 완전 탐색
│   │   ├── 05_recursion.py          # 재귀 (팩토리얼/피보나치)
│   │   ├── 06_backtracking.py       # 백트래킹 (조합 생성)
│   │   ├── 07_complexity.py         # 시간복잡도
│   │   ├── 08_bubble_sort.py        # 버블 정렬 (대표 O(n²) 정렬)
│   │   ├── 09_number_theory.py      # 정수론
│   │   ├── 10_binary_search.py      # 이분 탐색
│   │   ├── 11_divide_conquer.py     # 분할정복 (최댓값 찾기)
│   │   ├── 12_stack.py              # 스택
│   │   ├── 13_queue.py              # 큐
│   │   ├── 14_linked_list.py        # 연결 리스트
│   │   ├── 15_hash_table.py         # 해시 테이블
│   │   └── check.py                 # 자동 탐지 채점기 (15개)
│   └── 2. advanced/          # 심화 문제 (난이도 오름차순)
│       ├── 01_quick_sort.py         # 분할정복 응용
│       ├── 02_merge_sort.py         # 분할정복 응용
│       ├── 03_priority_queue.py     # 힙 자료구조 응용
│       ├── 04_hanoi_tower.py        # 재귀 응용 (Lucas, 1883, PD)
│       ├── 05_n_queen.py            # 백트래킹 응용 (Bezzel, 1848, PD)
│       └── check.py                 # 자동 탐지 채점기 (5개)
├── week3/
│   ├── 1. basic/             # 기본 개념 학습 (총 9개 문제)
│   │   ├── 01_binary_tree.py        # 이진 트리
│   │   ├── 02_bst.py                # 이진 탐색 트리
│   │   ├── 03_graph_basic.py        # 그래프 기초
│   │   ├── 04_bfs.py                # 너비 우선 탐색
│   │   ├── 05_dfs.py                # 깊이 우선 탐색
│   │   ├── 06_dp_fibonacci.py       # DP - 피보나치 (top-down memoization)
│   │   ├── 07_dp_stairs.py          # DP - 계단 오르기 (bottom-up tabulation)
│   │   ├── 08_greedy_coin.py        # 그리디 - 거스름돈
│   │   ├── 09_greedy_meeting.py     # 그리디 - 회의실 배정 (Activity Selection)
│   │   └── check.py                 # 자동 탐지 채점기 (9개)
│   └── 2. advanced/          # 심화 문제 (난이도 오름차순, 자체 지문 + 자체 테스트)
│       ├── 01_topological_sort.py   # 그래프 + 큐 + 진입차수
│       ├── 02_lcs.py                # 2차원 DP (최장 공통 부분수열)
│       ├── 03_dijkstra.py           # 그래프 + heap 최단경로
│       └── check.py                 # 자동 탐지 채점기 (3개)
└── README.md                 # 본 문서
```

> ℹ️ **현재 문제 구성 요약**
> | 폴더 | 문제 수 | 번호 범위 | 비고 |
> |---|---|---|---|
> | `week2/1. basic` | 15 | 01 ~ 15 | 문자열/배열/딕셔너리부터 자료구조까지 |
> | `week2/2. advanced` | 5 | 01 ~ 05 | 분할정복·재귀·백트래킹 응용 |
> | `week3/1. basic` | 9 | 01 ~ 09 | 트리/그래프/DP/그리디 입문 |
> | `week3/2. advanced` | 3 | 01 ~ 03 | 그래프 응용 + 고급 DP |


## ⚙️ 실행 환경 준비 (Python 3 설치)

이 저장소의 모든 문제는 **외부 라이브러리 없이 순수 표준 Python 만으로** 풀 수 있습니다.
추가로 `pip install` 해야 하는 패키지는 없습니다.

### 필요한 것

- **Python 3.8 이상** (권장: 최신 3.x)
- 채점기(`check.py`)가 내부적으로 `python3` 명령을 호출하므로, `python` 이 아니라 **`python3` 명령이 사용 가능해야** 합니다.
- (선택) 저장소 제출용 **Git**, 코드 편집용 에디터(VS Code / Cursor 등)

### 설치 방법 (운영체제별)

**macOS**

```bash
# Homebrew 사용 (권장)
brew install python

# 설치 확인
python3 --version
```

> macOS 에는 시스템 Python 이 없거나 오래된 경우가 있으므로 Homebrew 로 설치하는 것을 권장합니다.

**Windows**

1. [python.org/downloads](https://www.python.org/downloads/) 에서 설치 파일 다운로드
2. 설치 시 **"Add Python to PATH"** 옵션을 반드시 체크
3. 확인 (PowerShell / CMD):

```powershell
python --version
py --version
```

> Windows 에서는 `python3` 대신 `python` 또는 `py` 를 사용합니다.
> 채점 시 `python3` 대신 `python check.py ...` 형태로 실행하세요.

**Linux (Ubuntu/Debian)**

```bash
sudo apt update
sudo apt install python3

# 설치 확인
python3 --version
```

### 설치 확인

아래 명령이 버전 정보를 출력하면 준비 완료입니다.

```bash
python3 --version
# 예: Python 3.13.4
```


## 저장소 설정하기

이 템플릿을 본인의 GitHub 저장소로 복사합니다.

```bash
# 템플릿 클론 후 새 저장소로 초기화
git clone <템플릿-저장소-URL>
cd <템플릿-저장소-URL>
rm -rf .git
git init
git remote add origin <본인-저장소-URL>
git add .
git commit -m "Initial commit"
git branch -M main
git push -u origin main
```

## 📝 문제 풀이 방법

각 폴더의 `check.py` 는 같은 폴더 안의 `NN_*.py` 파일을 자동으로 찾아 채점합니다.
번호가 늘어나거나 줄어들어도 스크립트를 수정할 필요 없이 그대로 사용할 수 있습니다.

### 모든 문제 한 번에 테스트

```bash
# Week 2 기본 문제 전체 (01~15) 채점
cd "week2/1. basic"
python3 check.py --all
# 인자 없이 실행해도 동일하게 전체 채점됩니다
python3 check.py

# Week 2 심화 문제 전체 (01~05: 퀵정렬, 머지정렬, 우선순위 큐, 하노이, N-Queen) 채점
cd "../2. advanced"
python3 check.py --all

# Week 3 기본 문제 전체 (01~09: 트리/그래프/DP/그리디) 채점
cd "../../week3/1. basic"
python3 check.py --all

# Week 3 심화 문제 전체 (01~03: 위상정렬, LCS, 다익스트라) 채점
cd "../2. advanced"
python3 check.py --all
```

### 특정 문제만 테스트

```bash
cd "week2/1. basic"

# 예시: week2 의 01_string.py 만 테스트
python3 check.py 01_string.py

# 예시: 분할정복 입문 문제 (최댓값 찾기) 테스트
python3 check.py 11_divide_conquer.py

# 예시: advanced 의 퀵 정렬만 테스트
cd "../2. advanced"
python3 check.py 01_quick_sort.py

# 예시: week3 의 그리디 - 회의실 배정만 테스트
cd "../../week3/1. basic"
python3 check.py 09_greedy_meeting.py

# 예시: week3 의 다익스트라만 테스트
cd "../2. advanced"
python3 check.py 03_dijkstra.py
```


## 📜 Advanced 문제 출처

### week2/2. advanced (5문제)

| 번호 | 문제 | 분류 | 원전 / 출처 | 라이선스 |
|---|---|---|---|---|
| 01 | 퀵 정렬 | 분할정복 응용 | 1961년 C. A. R. Hoare 가 발표한 표준 알고리즘 | 알고리즘 자체는 공지된 표준 기법 |
| 02 | 머지 정렬 | 분할정복 응용 | 1945년 John von Neumann 이 제안한 표준 알고리즘 | 알고리즘 자체는 공지된 표준 기법 |
| 03 | 우선순위 큐 | 힙 자료구조 응용 | 1964년 J. W. J. Williams 의 Heap (heapsort) | 알고리즘 자체는 공지된 표준 기법 |
| 04 | 하노이의 탑 | 재귀 응용 | 1883년 Édouard Lucas (고전 퍼즐) | Public Domain |
| 05 | N-Queen | 백트래킹 응용 | 1848년 Max Bezzel (고전 퍼즐) | Public Domain |

### week3/2. advanced (3문제)

| 번호 | 문제 | 분류 | 원전 / 출처 | 라이선스 |
|---|---|---|---|---|
| 01 | 위상 정렬 | 그래프 + 큐 + 진입차수 | 1962년 Arthur Kahn 알고리즘 (표준 기법) | 알고리즘 자체는 공지된 표준 기법 |
| 02 | LCS | 2차원 DP (문자열) | 컴퓨터 과학의 표준 DP 문제 | 알고리즘 자체는 공지된 표준 기법 |
| 03 | Dijkstra | 그래프 + heap 최단경로 | 1959년 Edsger W. Dijkstra | 알고리즘 자체는 공지된 표준 기법 |

각 `.py` 파일의 지문과 테스트 케이스는 백준/LeetCode 등 외부 사이트의
지문을 복사하지 않고 본 학습 자료를 위해 자체적으로 작성된 것입니다.