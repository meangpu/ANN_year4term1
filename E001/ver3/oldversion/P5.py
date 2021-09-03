"""
P5. Old-time sailor.
Student name: Nattapong Tangsatheanrapap
613040128-7

version 2 add white space behind final answer
"""


def word_to_min(time_word: str) -> int:
    time_word = time_word.lower()
    list_time = time_word.split(":")
    hour = int(list_time[0]) * 60
    minute = int(list_time[1][0:-1])
    ans = hour + minute
    if time_word[-1] == "p":
        ans += 720
    if int(list_time[0]) == 12 and minute == 0:
        ans -= 720
    return ans


def gtm_to_longitude():
    adding_word = ""
    gtm = input("GTM: ").strip()
    user_input = word_to_min(gtm)
    if user_input > 720:
        adding_word = "W "
    elif user_input < 720:
        adding_word = "E "

    final_ans = abs(user_input-720)/4
    print(f"longitude= {final_ans:.2f} {adding_word}")


if __name__ == '__main__':
    gtm_to_longitude()
