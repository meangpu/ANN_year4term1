"""
P3
Student name: Nattapong Tangsatheanrapap
613040128-7
"""


def read_to_list(file_name: str) -> list:
    file = open(file_name, "r")
    lines = file.readlines()
    lines = [line.strip() for line in lines]
    file.close()
    return lines


def eeg_sequence():
    answer_list = []
    file_name = input("File: ")
    series = input("Series: ").lower().strip()
    series = series.split(" ")

    all_line_list = read_to_list(file_name)

    # ['#', 'co2a0000364.rd'], ['#', '120', 'trials,', '64', 'chans,', '416', 'samples', '368', 'post_stim', 'samples']
    all_line_list = [line.split(" ") for line in all_line_list]

    for i in all_line_list:
        if i[0] == series[0] and i[1].lower() == series[1]:
            answer_list.append(float(i[3]))

    print(answer_list)


if __name__ == '__main__':
    # "shorten_co2a0000364.rd.000"
    eeg_sequence()
