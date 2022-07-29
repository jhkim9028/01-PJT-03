import sys

sys.stdin = open("_문자열의거울상.txt")

# 'b', 'd', 'p', 'q'

# 입력
# 테스트 케이스 T
# 문자열

#출력
# 거울에 비친 문자열 출력

# 테스트 케이스 선언
T = int(input())

# 거울에 비친 모습을 딕셔너리에 저장
dict_ = {
    'b' : 'd',
    'd' : 'b',
    'p' : 'q',
    'q' : 'p'
    }
# 근데 순서도 바뀐다.
# 마지막 출력할 때 순서 바꿔서 출력

# T만큼 반복
a =''
for t in range(1, T+1):
    word = input()
    mirror = []
    a = ''
    for i in word:
        if i in dict_.keys():
            a += dict_.get(i)
    print(f'#{t} {a[::-1]}')