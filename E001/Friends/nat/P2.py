# count = 0
# sum = 0
# number = 1
#
# while number >= 0:
#     number = float(input(f"x{count+1}: "))
#     sum += number
#     count += 1
#     print("mean={}".format(sum / count))
#
# else:
#     print("Average: ", sum / (count-1))

count = 0
sum = 0.0
number = 1

while number >= 0:
    number = float(input(f"x{count+1}: "))
    sum = sum + number
    count += 1
    print("Average: ", sum / (count))