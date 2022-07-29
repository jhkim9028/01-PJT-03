import sys

sys.stdin = open("_소득불균형.txt")

#입력
# 첫줄은 전체 테스트 케이스 T
# 정수 N
# 정수 N명의 소득

# 출력
# 각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
# 각 테스트 케이스마다 한 줄씩 평균 이하의 소득을 가진 사람들의 수를 출력한다.

# 테스트 게이스 T
T = int(input())
# 7
# 2 7 1 8 2 8 4
cnt = 0
for i in range(T):
    t = int(input())
    money = list(map(int, input().split()))
    avg_ = sum(money) / len(money)
    #print(sum(t) / len(t)) #4.571428571428571

    # 평균이하 인 소득 넣을 리스트
    under = []
    for don in money:
        if don <= avg_:
            under.append(don)
    cnt += 1
    print(f'#{cnt} {len(under)}')