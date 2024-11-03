//삼각수를 미리 계산
tri_num = [ (i*(i+1))//2 for i in range(1, 45) ]
arr = [0] * 1001

//배열에 3개의 삼각수의 합으로 표현가능한 항목들을 미리 계산
for i in tri_num:
    for j in tri_num:
        for k in tri_num:
            if i + j + k <= 1000:
                arr[i+j+k] = 1

n = int(input())

for i in range(n):
    check = int(input())
    answer = 0
    
    if arr[check] == 1:
        answer = 1
    print(answer)   
