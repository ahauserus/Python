import random

jkpt = 1000000

winning = random.choices(range(0, 101), k=6)

lucky = []
count = 1

while count < 7:
    lucky_num = int(input(f"Enter lucky number {count}: "))
    lucky.append(lucky_num)
    count += 1

zipped = list(zip(winning, lucky))

bonus = 0
outcome = []
result = ''

for x in zipped:
    if x[0] == x[1]:
        result = 'W'
    else:
        result = 'L'
    outcome.append(result)

correct = outcome.count('W')

if correct == 0:
    bonus = 0
elif correct == 1:
    bonus = 0.1 * jkpt
elif correct == 2:
    bonus = 0.25 * jkpt
elif correct == 3:
    bonus = 0.4 * jkpt
elif correct == 4:
    bonus = 0.6
elif correct == 5:
    bonus = 0.8 * jkpt
else:
    bonus = 1 * jkpt

print(f"\nWinning Numbers:\t{winning}")
print(f"Your Numbers:\t{lucky}")
print(f"Right guesses:\t{correct}")
print(f"Your bonus:\tKsh {bonus}")


