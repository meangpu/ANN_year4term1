"""
P7. SIR model.
Student name: Nattapong Tangsatheanrapap
613040128-7
"""


def write_list_to_file(file_name: str, list_data: list):
    file = open(file_name, "w")

    for line in list_data:
        file.writelines(line + "\n")

    file.close()


def sir_func(outcome="epidemic.txt"):
    text_line_list = []
    S, I, R = input("Initial S, I, R: ").split()
    c, r = input("c, r: ").split()

    # for debug ####
    # S, I, R = "50000 32 0".split()
    # c, r = "4.2e-6 0.04".split()

    S = float(S)
    I = float(I)
    R = float(R)
    c = float(c)
    r = float(r)
    periods = int(input("periods: "))

    if c*S > r:
        print("--> It is spreading! ")
    else:
        print("--> It is contained! ")

    text_line_list.append(f"0: S = {S:.0f}; I = {I:.0f}; R = {R:.0f}")
    for time_pass in range(periods):
        time_pass += 1
        new_S = S - (c*S*I)
        new_I = I + ((c*S*I) - (r*I))
        new_R = R + (r*I)
        text_line_list.append(f"{time_pass}: S = {new_S:.0f}; I = {new_I:.0f}; R = {new_R:.0f}")
        S = new_S
        I = new_I
        R = new_R

    write_list_to_file(outcome, text_line_list)


if __name__ == "__main__":
    out_text_name = "epidemic.txt"
    sir_func(out_text_name)

