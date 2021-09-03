"""

"""


# # File_name = input("File: ")
# File_name = "shorten_co2a0000364.rd.000"
# series = input("Series: ").lower().split(" ")
#
# ans_list = []
#
# file = open(File_name, "r")
# s = file.readlines()
# for item in s:
#     item = item.lower().split(" ")
#     if item[1] == series[1] and item[0] == series[0]:
#         ans_list.append(float(item[3].strip()))
# file.close()
#
# print(ans_list)


if __name__ == "__main__":
    # File_name = input("File: ")
    File_name = "shorten_co2a0000364.rd.000"
    series = input("Series: ").lower()

    ans_list = []

    file = open(File_name, "r")
    s = file.readlines()
    for item in s:
        item = item.lower()
        if item[0:5] == series:
            ans_list.append(float(item[8:].strip()))
    file.close()

    print(ans_list)


