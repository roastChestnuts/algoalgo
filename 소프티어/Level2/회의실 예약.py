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

meeting_room = dict()

#회의실 생성
for _ in range(N):
    room_name = input().rstrip()
    meeting_room[room_name] = list(True for i in range(24))

#회의실 예약시간 입력 후 사용가능 시간대 세팅
for i in range(M):
    room_name, start, end = input().split()
    start = int(start)
    end = int(end)
    for time in range(start, end):
        meeting_room[room_name][time] = False

sorted_room = sorted(meeting_room.keys())
for idx, room in enumerate(sorted_room):
    reserve = meeting_room[room] #정렬된 현재 룸
    start_time = None
    intervals = []
    for time in range(9, 18):
        if reserve[time] == True:
            if start_time == None:
                start_time = time
        else:
            if start_time != None:
                intervals.append((start_time, time))
                start_time = None
    if start_time != None:
        intervals.append((start_time, 18))

    print(f'Room {room}:')
    if len(intervals) == 0:
        print('Not available')
    else:
        print(f'{len(intervals)} available')    
        for start, end in intervals:
            print(f"{start:02d}-{end:02d}")
    if idx != len(sorted_room) - 1 :
        print("-----")        
    