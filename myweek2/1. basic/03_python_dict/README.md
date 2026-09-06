## 기초
- dictionary는 key와 value 이루어져있음
- dictionary 이름["key"] 로 value 값을 불러올 수 있다.
- dictionary를 리스트에 넣어서 자주 사용함.
  예: [{"name": "Alice", "score": 85}, {"name": "Bob", "score": 92}, {"name": "Charlie", "score": 78}, {"name": "David", "score": 95}]


## 응용
- 리스트로 딕셔너리 value 추출
score = [i["score"] for i in students]

결과 : score = [85,92]


- 조건식으로 특정 value 추출
above_average_students = [k["name"]
                              for k in students if average <= k["score"]]

조건 : average = 87.5
결과 : above_average_students = ["Bob","David"]