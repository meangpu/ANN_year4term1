"""
P2. Online averaging.
Student name: Pongpisit Deesarapan
"""

count = 0
sum = 0
number = 1

while number >= 0:
    number = float(input(f"x{count+1}: "))
    sum += number
    count += 1
    print(f"mean:{(sum/count):.4f}")
