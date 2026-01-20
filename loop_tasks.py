# loop_tasks.py
# DELIVERABLE: Loop Demonstration Script (With Input)

def print_1_to_100():
    print("\n--- Task 2: For loop (1 to 100) ---")
    for i in range(1, 101):
        print(i, end=" ")
    print()


def countdown_timer():
    print("\n--- Task 3: While loop Countdown Timer ---")
    try:
        start = int(input("Enter countdown starting number: "))
        while start >= 0:
            print(start)
            start -= 1
        print(" Countdown finished!")
    except ValueError:
        print(" Invalid input! Please enter an integer.")


def break_continue_demo():
    print("\n--- Task 4: Break and Continue Demo ---")
    for num in range(1, 21):
        if num == 5:
            print("Skipping number 5 (continue)")
            continue
        if num == 15:
            print("Stopping at 15 (break)")
            break
        print(num)


def iterate_string_chars():
    print("\n--- Task 5: Iterating over String Characters ---")
    text = input("Enter any word: ")
    for ch in text:
        print(ch)


def multiplication_table():
    print("\n--- Task 6: Multiplication Table ---")
    try:
        n = int(input("Enter a number: "))
        for i in range(1, 11):
            print(f"{n} x {i} = {n * i}")
    except ValueError:
        print(" Invalid input! Please enter an integer.")


def range_with_steps():
    print("\n--- Task 7: Range with Steps ---")
    print("Even numbers from 2 to 20:")
    for i in range(2, 21, 2):
        print(i, end=" ")
    print()


def loop_with_conditions():
    print("\n--- Task 8: Loop with Conditions ---")
    print("Numbers from 1 to 50 divisible by 3 AND 5:")
    for i in range(1, 51):
        if i % 3 == 0 and i % 5 == 0:
            print(i, end=" ")
    print()


def main():
    print(" LOOP DEMONSTRATION SCRIPT (loop_tasks.py)")
    print("=" * 45)

    print_1_to_100()
    countdown_timer()
    break_continue_demo()
    iterate_string_chars()
    multiplication_table()
    range_with_steps()
    loop_with_conditions()

    print("\n All loop tasks completed successfully!")


if __name__ == "_main_":
    main()
# loop_tasks.py
# DELIVERABLE: Loop Demonstration Script (With Input)

def print_1_to_100():
    print("\n--- Task 2: For loop (1 to 100) ---")
    for i in range(1, 101):
        print(i, end=" ")
    print()


def countdown_timer():
    print("\n--- Task 3: While loop Countdown Timer ---")
    try:
        start = int(input("Enter countdown starting number: "))
        while start >= 0:
            print(start)
            start -= 1
        print(" Countdown finished!")
    except ValueError:
        print(" Invalid input! Please enter an integer.")


def break_continue_demo():
    print("\n--- Task 4: Break and Continue Demo ---")
    for num in range(1, 21):
        if num == 5:
            print("Skipping number 5 (continue)")
            continue
        if num == 15:
            print("Stopping at 15 (break)")
            break
        print(num)


def iterate_string_chars():
    print("\n--- Task 5: Iterating over String Characters ---")
    text = input("Enter any word: ")
    for ch in text:
        print(ch)


def multiplication_table():
    print("\n--- Task 6: Multiplication Table ---")
    try:
        n = int(input("Enter a number for multiplication table: "))
        for i in range(1, 11):
            print(f"{n} x {i} = {n * i}")
    except ValueError:
        print(" Invalid input! Please enter an integer.")


def range_with_steps():
    print("\n--- Task 7: Range with Steps ---")
    print("Even numbers from 2 to 20:")
    for i in range(2, 21, 2):
        print(i, end=" ")
    print()


def loop_with_conditions():
    print("\n--- Task 8: Loop with Conditions ---")
    print("Numbers from 1 to 50 divisible by 3 AND 5:")
    for i in range(1, 51):
        if i % 3 == 0 and i % 5 == 0:
            print(i, end=" ")
    print()


def main():
    print(" LOOP DEMONSTRATION SCRIPT (loop_tasks.py)")
    print("=" * 45)

    print_1_to_100()
    countdown_timer()          #  asks input
    break_continue_demo()
    iterate_string_chars()     #  asks input
    multiplication_table()     #  asks input
    range_with_steps()
    loop_with_conditions()

    print("\n All loop tasks completed successfully!")


# ✅ VERY IMPORTANT: call main()
if __name__ == "_main_":
    main()