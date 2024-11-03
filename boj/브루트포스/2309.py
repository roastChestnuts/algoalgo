people = [int(input()) for _ in range(9)]
total_sum = sum(people)

found = False
for i in range(8):
    for j in range(i + 1, 9):
        if total_sum - people[i] - people[j] == 100:
            first, second = people[i], people[j]
            people.remove(first)
            people.remove(second)
            found = True
            break
    if found:
        break

people.sort()
print(*people)
