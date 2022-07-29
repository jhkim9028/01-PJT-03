import sys

sys.stdin = open("_신용카드만들기2.txt")

#3,4,5,6,9 로 시작
# 번호에 - 가 들어갈 수 있고 - 제외하고 16개 숫자

T = int(input())

for i in range(T):
    number = input()
    a = ''
    if '-' in number:
        a += number.replace('-','')
        if len(a) == 16:
            if a.startswith('3'):
                print(f'#{i+1} 1')
                continue
            if a.startswith('4'):
                print(f'#{i+1} 1')
                continue
            if a.startswith('5'):
                print(f'#{i+1} 1')
                continue
            if a.startswith('6'):
                print(f'#{i+1} 1')
                continue
            if a.startswith('9'):
                print(f'#{i+1} 1')
                continue
            else:
                print(f'#{i+1} 0')
        else:
            print(f'#{i+1} 0')
    if '-' not in number:       
        if len(number) == 16:
            if number.startswith('3'):
                print(f'#{i+1} 1')
                continue
            if number.startswith('4'):
                print(f'#{i+1} 1')
                continue
            if number.startswith('5'):
                print(f'#{i+1} 1')
                continue
            if number.startswith('6'):
                print(f'#{i+1} 1')
                continue
            if number.startswith('9'):
                print(f'#{i+1} 1')
                continue
            else:
                print(f'#{i+1} 0')
        else:
            print(f'#{i+1} 0')