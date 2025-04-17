# 제약조건
# 3 ≤ N ≤ 100,000 (참가자 수)

# 입력예제1

# 3
# 40 80 70
# 50 10 20
# 100 70 30

# 출력예제1

# 3 1 2
# 1 3 2
# 1 2 3
# 1 2 3

# 문제해석
# 입력받은 참가자들의 순위를 결정지어 줘야하네
# 만약 중복 점수라면 나보다 점수가 큰 사람의 수 +1 이 나의 등수

# 단순 구현으로 한다면 O(n^2) 시간초과가 남
# 먼저 내림차순으로 정렬 한다(Nlogn)

# 3 2 2 1
# 1 2 2 3
# 각각의 점수가 몇명인지 세어주는 변수가 있으면 좋을 듯?
# [3:1][2:2][1:1]
# dp문제같음
# 첫 시작점이라면 1로 시작
# 다음 점수인데 앞 점수와 같다? 동일 등수, 하지만 카운트는 +1
# 다음 점수인데 앞 점수보다 작다? +1 등수 
# 다음 점수에 진입했는데 앞 점수보다 작아지는 시점에 맵에 담아주면 될듯(값과 등수)

# import sys

# input = sys.stdin.readline

# n = int(input())

# for i in range(3):
#     scores = list(map(int, input().split()))
#     sorted_scores = sorted(scores, reverse=True)
 
#     #시작 순위
#     rank = 0
#     prev_score = -1
#     count = 0
#     rank_table = dict()
#     for score in sorted_scores:
#         if score > prev_score:
#             prev_score = score
#             count += 1
#             rank += 1
#             rank_table[score] = rank
#         elif score == prev_score:
#             count += 1        
#         elif score < prev_score:
#             prev_score = score
#             rank += count
#             count = 1
#             rank_table[score] = rank

#     for score in scores:
#         print(rank_table[score], end=' ')
#     print()    




import sys

input = sys.stdin.readline

n = int(input())
score_list = []
for i in range(3):
    scores = list(map(int, input().split()))
    score_list.append(scores)
#각 사람들의 점수 합계를 담을 빈 리스트 생성    
score_list.append([0 for _ in range(n)])

for i in range(3):
    for j in range(n):
        score_list[3][j] += score_list[i][j]

for scores in score_list:
    sorted_scores = sorted(scores, reverse=True)
 
    #시작 순위
    rank = 0
    prev_score = -1
    count = 0
    rank_table = dict()
    for score in sorted_scores:
        if score > prev_score:
            prev_score = score
            count += 1
            rank += 1
            rank_table[score] = rank
        elif score == prev_score:
            count += 1        
        elif score < prev_score:
            prev_score = score
            rank += count
            count = 1
            rank_table[score] = rank

    for score in scores:
        print(rank_table[score], end=' ')
    print()    
