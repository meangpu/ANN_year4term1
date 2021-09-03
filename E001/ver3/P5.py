"""
P5. Old-time sailor.
Student name: Nattapong Tangsatheanrapap
613040128-7

version 3.2 use teacher template
fix error that happen in: 12:00p
"""


def time2min(time_txt):
    meridiem = time_txt[-1]
    h, m = time_txt[:-1].split(":")
    mins = 0
    if meridiem == 'p':
        mins = 720  # offset the pm time to 720 mins
        # end if
    mins += 60 * (int(h) % 12) + int(m)  # 12:00a = 0:00a
    return mins


if __name__ == "__main__":
    GMT_noon = 720  # noon = 12:00pm = 12*60 = 720 min

    GMT = input("GMT: ")
    minute = time2min(GMT)

    if minute < GMT_noon:
        direction = "E"
    elif minute == GMT_noon:
        direction = ""
    else:
        direction = "W"

    longitude = abs(minute-GMT_noon) / 4

    print("longitude= {:.2f} {}".format(longitude, direction))
