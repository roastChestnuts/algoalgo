#9 ~ 18시 까지만 이용가능
#한 회의실은 일정 시간 동안만 점유. 각 회의는 회의실, 시작 종료시각 정보로 나타냄
#회의 시각은 시 단위로만 설정 가능, 회의시간은 겹칠 수 없다. 13-15 / 14-15 불가능
#시작 종료 시각이 같으면 안된다.

# N 회의실 개수(1~50), M 개의 회의 정보(1~100)

#입력예제
# 3 7
# grandeur
# avante
# sonata
# sonata 14 16
# grandeur 11 12
# avante 15 18
# sonata 10 11
# avante 9 12
# grandeur 16 18
# avante 12 15

#출력예제
# Room avante:
# Not available
# -----
# Room grandeur:
# 2 available:
# 09-11
# 12-16
# -----
# Room sonata:
# 3 available:
# 09-10
# 11-14
# 16-18

# [문제해석]
# 각 회의실별로 예약가능한 시간대의 개수와 시간정보를 표기해줘야한다.
# 입력받은 룸마다 배열을 이용하여 사용가능한 시간대를 초기화 해주기[09-18시만 사용가능]
# avante [0,0,0,0,0].... 각 인덱스마다 해당 시간을 의미할 수 있도록

# 요구하는 자료구조는 Map<String, List>형식으로 예상

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
meeting_rooms = dict()

for _ in range(N):
    room_name = input().rstrip()
    meeting_rooms[room_name] = [True for i in range(24)]

for i in range(M):
    room_name, start, end = input().split()
    start = int(start)
    end = int(end)

    for time in range(start, end): #끝 시간은 제외, 9-10시라면 10시부턴 예약이 가능 즉, 9시만 False처리
        meeting_rooms[room_name][time] = False 

#출력(*오름차순으로 출력)

sorted_rooms = sorted(meeting_rooms.keys())

#이제 출력해야하는데 정렬된 순서대로 출력해야하니 sorted_rooms를 기준으로 for를 돌아야함
#마지막 출력인 경우 '-----'가 출력되면 안됨, 따라서 인덱스도 필요함
#시작시간과 종료시간이 한 쌍으로 출력돼야 함 -> 튜플자료형을 이용, 개수도 출력해야하니 리스트에 튜플
#시작시간을 비워놓고서 순회하면서 예약되지 않은 시간이 있다면 시작시간에 담고, 
#예약된 시간을 만나면 리스트에 튜플로 값을 담아주기

for idx, key in enumerate(sorted_rooms):
    start = None
    intervals = []
    check_room = meeting_rooms[key] #현재 순회할 예약실 정보

    for time in range(9, 18):
        if check_room[time] == True:
            if start == None:
                start = time
        else:
            #시작 시간이 존재한다면 종료시간과 함께 리스트에 담아주기
            if start != None:
                intervals.append((start, time))
                #시작시간 초기화
                start = None
    #시작 시간이 존재한다면 17시까지 종료시간을 만나지 못한것이므로 18시까지 예약가능
    if start != None:
        intervals.append((start, 18))

    print(f"Room {key}")
    if len(intervals) == 0:
        print("Not available")
    else:
        print(f"{len(intervals)} available:")
        for start, end in intervals:
            print(f"{start:02d}-{end:02d}")

    if idx != len(intervals)-1:
        print("-----")                