# 1. 딕셔너리 구조

stack = []
for i in s:
    # in 딕셔너리는 딕셔너리의 키 값만 가져온다.
    if i in CLOSE_AND_OPEN:
        if not stack or stack.pop() != CLOSE_AND_OPEN[i]:
            return False
    else:

        stack.append(i)
return not stack # 스택이 비어있느면 True, 안비어있으면 False


# 2. 튜플 구조

stack = []
for i in s:
    if i in "({[": # 시간 : in list < in set 
        stack.append(i)
    else:
        if not stack or (stack.pop(), i) not in PAIRS:
            return False
return not stack


# 중요한점 :
- 항상 마지막에 스택이 비어있는지 확인한다.