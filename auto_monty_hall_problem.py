import random

no_change_success = 0
change_success = 0
no_change_fail = 0
change_fail = 0

for i in range(0,1000000):
    door = [0, 0, 0]

    car = random.randint(0, 2)

    door[car] = 1

    initial_choice = random.randint(0,2)

    open = 0

    while True:
        open = random.randint(0,2)
        if open != initial_choice and door[open] != 1:
            break

    change = random.randint(0, 1)

    final_choice = 0

    # 선택 바꿈 랜덤
    if change == 0:
        while True:
            final_choice = random.randint(0,2)
            if final_choice != open and final_choice != initial_choice:
                break
    else:
        final_choice = initial_choice

    if door[final_choice] == 1:
        if final_choice == initial_choice:
            no_change_success = no_change_success + 1
        else:
            change_success = change_success + 1
    else:
        if final_choice == initial_choice:
            no_change_fail = no_change_fail + 1
        else:
            change_fail = change_fail + 1

    # 선택 바꿈 필수
    # while True:
    #     final_choice = random.randint(0,2)
    #     if final_choice != open and final_choice != initial_choice:
    #         break
    #
    # if door[final_choice] == 1:
    #     change_success = change_success + 1
    # else:
    #     change_fail = change_fail + 1

print("no_change_success:",no_change_success)
print("change_success:",change_success)
print("no_change_fail:",no_change_fail)
print("change_fail:",change_fail)