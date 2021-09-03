"""
P5. Old-time sailor.
Student name: Tenaciti Kurios
"""
def time2min(timetxt):
    meridiem = timetxt[-1]
    h, m = timetxt[:-1].split(":")
    mins = 0
    if meridiem == 'p':
        mins = 720

    mins += 60 * (int(h) % 12) + int(m)
    print(mins)

    return mins


if __name__ == "__main__":
    GMTnoon = 720  # noon = 12:00pm = 12*60 = 720 min

    GMT = input("GMT: ")
    mins = time2min(GMT)
    print(mins)
    longitude = (mins - GMTnoon) / 4
    if mins < GMTnoon:
        direction = "E"
    elif mins > GMTnoon:
        direction = "W"
    else:
        direction = ""

    # Write your code here!

    print("longitude= {:.2f} {}".format(longitude, direction))

# end __main__
