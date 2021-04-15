import random

door = [0, 0, 0]

car = random.randint(0, 2)

door[car] = 1

initial_choice = 0

while True:
    initial_choice = int(input("3개의 문 중 몇번쨰를 고르시겠습니까?"))
    if initial_choice>= 1 and initial_choice <= 3:
        break
    else:
        print("1에서 3사이의 수를 입력해주세요.")

initial_choice = initial_choice - 1

open = 0

while True:
    open = random.randint(0,2)
    if open != initial_choice and door[open] != 1:
        print(open + 1, "번 문 안에는 염소가 들어있습니다.")
        break

change = input("선택을 바꾸시겠습니까?(예/ 아니요로만 답하시오)")

final_choice = 0

if change == "예":
    while True:
        final_choice = random.randint(0,2)
        if final_choice != open and final_choice != initial_choice:
            print("최종 선택은", final_choice + 1, "번 문입니다.")
            break
else:
    final_choice = initial_choice

for r in range(0,3):
    temp = door[r]
    if temp == 0:
        print(r + 1, "번 문은 염소가 있었습니다.")
    else:
        print(r + 1, "번 문은 차가 있었습니다.")

if door[final_choice] == 1:
    print("정답을 맞추셨습니다!")
else:
    print("정답을 맞추지 못하셨습니다.")