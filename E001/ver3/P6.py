"""
P6
Student name: Nattapong Tangsatheanrapap
613040128-7
problem = 121 = 16 / 220 = 24
"""


def calculate_lapse():
    stone = input("Stones: ")
    ans = int(stone[0]) * 9 + int(stone[1]) * 3 + int(stone[2])
    print(f"Lapse= {ans} ")


if __name__ == '__main__':
    calculate_lapse()
