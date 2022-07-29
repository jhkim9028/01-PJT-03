import sys

sys.stdin = open("_최빈수구하기.txt")

# 총 테스트 케이스는 10
# 각 테스트 케이스마다 번호 부여
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스에 대한 답을 출력한다.

# 최빈수 구하기

# 총 테스트 케이스 수
T = int(input())

# 10, 8, 7, 2, 2, 4, 8, 8, 8, 9, 5, 5, 3
# 숫자들을 넣을 리스트 선언
# ls = [10, 8, 7, 2, 2, 4, 8, 8, 8, 9, 5, 5, 3]

#비교할 딕셔너리 선언
dict_ = {}


for i in range(T):
    t = int(input())
    scores = list(map(int, input(). split()))
# print(t)
# print(scores)
    # 딕셔너리 안에 리스트안의 값과 값마다의 횟수 추가
    for i in scores:
        dict_[i] = 0
    for j in scores:
        dict_[j] += 1
    #print(dict_) #{10: 1, 8: 4, 7: 1, 2: 2, 4: 1, 9: 1, 5: 2, 3: 1}

    # 이제 최빈수를 출력
    # 근데 최빈수가 2개 이상이면 가장 큰 수 출력
    # 가장 큰 점수를 출력해야 하니까 키값을 최종 출력

    # 최빈값
    max_ = max(dict_.values())
    #print(max_) # 4
    score = []
    fin = 0
    # 최빈값이 4인 키값출력
    for k, v in dict_.items():
        if v == max_:
            # print(k) # 8 출력
            score.append(k)
    print(f'#{t} {max(score)}')