"""
P6
Student name: Nattapong Tangsatheanrapap
613040128-7

# error with 121 and 220
me 121 = 16 and 220 = 24
"""


def calculate_lapse():
    ans = 0
    stone = input("Stones: ").strip()
    for i in range(len(stone)):  # i = 0 1 2
        ans += int(stone[i])*(3**int(len(stone)-(i+1)))

    print(f"Lapses= {ans} ")


if __name__ == '__main__':
    calculate_lapse()
