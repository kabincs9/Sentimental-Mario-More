# for input and type in -1 and press enter...should reject this input as invalid, as by re-prompting the user to type in another number.
# for a prompt for input.and type in 0 and press enter. should reject this input as invalid, as by re-prompting the user to type in another number.
# run your program as python mario.py and wait for a prompt for input.and type in 1 and press enter..should generate the below output... sure that the pyramid is aligned to the bottom-left corner of your terminal, and that there are no extra spaces at the end of each line.
# so < 1 and > 8 and if less than 0 break
# to define the number of coloumn to print and row to print

from cs50 import get_int

# to get the required height
while True:
    n = get_int("Height: ")  # make sure prompt matches exactly with required format
    if 1 <= n <= 8:
        break

# for printing rows
for i in range(n):  # to run for n to n-1
    for j in range(n - i - 1):
        # eg two space for row 0 if n is 3 or like i is 0 at first if i one space so one space keep adding with one space
        print(" ", end="")

    # left side
    for j in range(i + 1):  # to print two space and # symbol again like if i is zero print 1
        print("#", end="")  # print one # symbol

    # for the gap
    print("  ", end="")  # two spaces for CS50 more version

    # right pyramid
    for j in range(i + 1):  # must match the same number of hashes as left
        print("#", end="")  # print one # staying on same line

    # new line
    print()
    # so like it starts fresh after pressing enter
    # like i is 0 then " #  # "
    # if one " ##  ## "
    # if three " ####  #### "...
