import sys

sys.stdin = open("_신용카드만들기1.txt")

#4 5 2 0 0 2 0 0 1 9 0 0 4 0 6
# 홀수 자리는 2를 곱하고 자기들끼지 더하고
# 짝수 자리는 짝수자리 끼리 더하고 
#  위에 두개를 더한거에 N을 더하고 % 10 == 0 인 N을 출력

T = int(input())


for t in range(T):
    hol = []
    jjak = []
# 숫자를 리스트로 입력받는다.
    num = list(map(int, input().split()))

    # 반복문을 통해 홀수자리는 2를 곱하고 리스트에 넣는다.
    for i in range(len(num)):
        if i % 2 == 0:
            hol.append(num[i]*2)
        if i % 2 == 1:
            jjak.append(num[i])
    # print(hol) # [8, 4, 0, 0, 2, 0, 8, 12]
    # print(jjak) # [5, 0, 2, 0, 9, 0, 0]
    sum_hol = sum(hol)
    sum_jjak = sum(jjak)
    for j in range(10):
        if (sum_jjak + sum_hol + j) % 10 == 0:
            print(f'#{t+1} {j}')