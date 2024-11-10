# 1000개의 숫자 후보를 True로 초기화
num_list = [True for i in range(1000)]

# 123부터 999까지 각 숫자에 대해 조건 검사
for i in range(123, 1000):
  list_i = str(i)
  # 같은 숫자가 있거나 '0'이 포함된 경우 후보 제외
  if list_i[0] == list_i[1] or list_i[1] == list_i[2] or list_i[0] == list_i[2]:
    num_list[i] = False
  elif list_i[0] == '0' or list_i[1] == '0' or list_i[2] == '0':
    num_list[i] = False

# 힌트 개수 입력
n = int(input())

# 각 힌트를 처리
for i in range(n):
  hint, s, b = map(int, input().split())
  hint = str(hint)
  
  # 123부터 999까지의 후보 숫자를 검사
  for num in range(123, 1000):
    chk_s, chk_b = 0, 0
    if num_list[num]:
      str_num = str(num)
      # 스트라이크와 볼 개수 확인
      for j in range(3):
        for k in range(3):
          if str_num[j] == hint[k] and j == k:
            chk_s += 1
          elif str_num[j] == hint[k] and j != k:
            chk_b += 1
      # 힌트 조건을 만족하지 않으면 후보 제외
      if chk_b == b and chk_s == s:
        num_list[num] = True
      else:
        num_list[num] = False

# 가능한 숫자 개수 출력
cnt = 0
for i in range(123, 1000):
  if num_list[i]:
    cnt += 1
print(cnt)
