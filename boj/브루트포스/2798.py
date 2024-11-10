n, m = map(int, input().split())

card_list = list(map(int, input().split()))
sum_list = []
max_num = 0

for i in range(len(card_list)-2): #무조건 3개를 골라야하니까, 인덱스 2를빼서 첫 카드로 끝에 3개를 고르지 못하게
    for j in range(i+1, len(card_list)-1):
        for k in range(j+1, len(card_list)):
            if card_list[i]+card_list[j]+card_list[k] > m:
                continue
            else:
                max_num = max(max_num, card_list[i]+card_list[j]+card_list[k])
print(max_num)
