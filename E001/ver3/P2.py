"""
P2
Student name: Nattapong Tangsatheanrapap
613040128-7

*update p2 to use old system
"""


def average_num():
    running = True
    count = 0
    summa = 0
    while running:
        user_num = float(input(f"x{count + 1}: "))

        count += 1
        summa += user_num
        mean = summa/count
        print(f"mean={mean:.4f}")
        if user_num < 0:
            running = False


if __name__ == '__main__':
    average_num()
