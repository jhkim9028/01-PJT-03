import sys

sys.stdin = open("_직사각형길이찾기.txt")

# a = b일땐 c랑 같고 a= c 일땐 b랑 같고 b=c일때 a랑 같다

T = int(input())

x = 0
cnt = 0
for i in range(1,T+1):
    a = list(map(int, input().split()))
    # print(a)
    if a[-1] == a[-2]:
        x = a[-3]
    if a[-1] == a[-3]:
        x = a[-2]
    if a[-2] == a[-3]:
        x = a[-1]
    cnt += 1
    print(f'#{cnt} {x}')