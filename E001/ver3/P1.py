"""
P1
Student name: Nattapong Tangsatheanrapap
613040128-7
"""


def letter_to_dir():
    final_word = "facing "
    direction = input("observe: ")
    direction = direction.strip().lower()

    if direction == "u":
        final_word += "east"
    elif direction == "d":
        final_word += "west"
    elif direction == "r":
        final_word += "south"
    elif direction == "l":
        final_word += "north"

    elif direction == "ul":
        final_word += "north-east"
    elif direction == "ur":
        final_word += "south-east"

    elif direction == "dl":
        final_word += "north-west"
    elif direction == "dr":
        final_word += "south-west"

    elif direction == "ru":
        final_word += "south-east"
    elif direction == "rd":
        final_word += "south-west"

    elif direction == "lu":
        final_word += "north-east"
    elif direction == "ld":
        final_word += "north-west"

    else:
        final_word = "error"

    return final_word


if __name__ == '__main__':
    print(letter_to_dir())
