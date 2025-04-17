#일차적으로 정렬 후에(오름차순)
#현재 순회하는 값의 좌측 인덱스들을 순회
#좌측 인덱스의 처음과 끝 값 을 바라보는 포인터를 만들기

import sys

input = sys.stdin.readline

count = 0
n = int(input())

numbers = list(map(int, input().split()))

numbers.sort() #정렬(O logN)

for i in range(2, n):
    start_idx = 0
    end_idx = n-1
    while start_idx < end_idx:
        if numbers[i] == numbers[start_idx] + numbers[end_idx]:
            count += 1
            break
        elif numbers[i] < numbers[start_idx] + numbers[end_idx]:
            end_idx -= 1
        elif numbers[i] > numbers[start_idx] + numbers[end_idx]:    
            start_idx += 1

        if start_idx == i:
            start_idx += 1
        if end_idx == i:
            end_idx -= 1

print(count)
    
    

