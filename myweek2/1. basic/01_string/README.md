    # 특수기호 제거 후, 소문자
    s = ''.join(e.lower() for e in s if e.isalnum())

    ## 문자열 뒤집기 첫번째 방법 - 파이썬 슬라이싱
    return s == s[::-1]

    ## 문자열 뒤집기 두번째 방법 - 배열 나눠서 파이썬 슬라이싱 진행
    len_s = len(s)
    left  = 0
    mid = len_s//2

     1. 중간값 없을 때
    if len(s) % 2 == 0:
        if s[left:mid] == s[mid:][::-1]:
            return True
        else:
            return False

     2. 중간값 있을 때
    else:
        if s[left:mid] == s[mid+1:][::-1]:
            return True
        else:
            return False


    ## 문자열 뒤집기 세번째 방법 - 투포인터 방식
    len_s = len(s)
    left = 0
    right = len_s-1

    배열의 크기가 홀수일 때도 mid는 어차피 바뀌지 않기 때문에
    왼쪽 인덱스가 오른쪽 인덱스보다 작을때만 루프가 발생하도록 해야함.

    while left < right:
        if s[left] != s[right]:
            return False
        else:
            left += 1
            right -= 1
    return True
    
    
    
    ## 결과:
    첫번째 방법은 시간복잡도 O(n), 공간복잡도 O(n)
    세번째 방법은 시간복잡도 O(n), 공간복잡도 O(1)
    시간복잡도 상으로 같은 값이지만, 첫번째 방법(파이썬 슬라이싱)은 C로 구현된 함수이기에
    인터프리터를 거치지 않고 메모리 블록 통째로 다룸.
    반면 세번째 방법(투포인터 방식)은 인터프리터가 루프문에서 한줄씩 해석하기 때문에
    루프문 도는 비용 자체가 비싸다.


    ## 깨달은점:
    시간복잡도가 같다면 상수배수에서 가른다.
    파이썬에서 상수배수는 C냐 파이썬 루프로 가른다.
    파이썬에서는 내장 함수가 기본.
    투 포인터는 메모리 제한이 걸리거나, 슬라이싱으로 표현이 안 되는 문제(정렬 배열에서 합이 K인 쌍 등)에서 쓴다.