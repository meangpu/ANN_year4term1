"""
P7. SIR model.
Student name: Thiranat Kanchanophat
"""

if __name__ == "__main__":
    S, I, R = input("Initial S, I, R: ").split()
    c, r = input("c, r: ").split()
    S = float(S)
    I = float(I)
    R = float(R)
    c = float(c)
    r = float(r)
    periods = int(input("periods: "))

    # spread_or_not = (c * S * I) - (r * I)

    if c*S > r:
        print("--> It is spreading!")
    else:
        print('--> It is contained! ')

    with open("epidemic.txt", "w") as f:
        m = "0: S = {:.0f}; I = {:.0f}; R = {:.0f}\n".format(S, I, R)
        f.write(m)

        for n in range(periods):
            # Write your code here!
            S_new = -c * S * I
            I_new = (c * S * I) - (r * I)
            R_new = r * I

            S += S_new
            I += I_new
            R += R_new

            m = "{}: S = {:.0f}; I = {:.0f}; R = {:.0f}\n".format(n+1, S, I, R)

            f.write(m)

