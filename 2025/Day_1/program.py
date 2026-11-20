# NOTE: Maybe it is better to add or subtract with MAX_POSITIONS instead of OFFSET.
DIAL_MIN = 0
DIAL_MAX = 99
OFFSET = 1
MAX_POSITIONS = 100

def dial_left(dial_point, input):
    if (input >= MAX_POSITIONS):
        raise ValueError("The input is above that of the maximum amount of positions.")

    new_dial_point = dial_point - input
    # NOTE: Example -> 0 - 5 = -5

    if (new_dial_point < DIAL_MIN):
        new_dial_point = (new_dial_point + OFFSET) + DIAL_MAX
        # NOTE: Example -> (-5 + 1) + 99 = 95
        # NOTE: If offset of one wasn't added the result would be 94 and that would not be correct.

    return new_dial_point

def dial_right(dial_point, input):
    if (input >= MAX_POSITIONS):
        raise ValueError("The input is above that of the maximum amount of positions.")

    new_dial_point = dial_point + input
    # NOTE: Example -> 99 + 5 = 104

    if (new_dial_point > DIAL_MAX):
        new_dial_point = (new_dial_point - OFFSET) - DIAL_MAX
        # NOTE: Example -> (104 - 1) - 99 = 4
        # NOTE: If offset of one wasn't subtracted the result would be 5 and that would not be correct.

    return new_dial_point

input_str_arr = ["", ""]
dial_point = 50
dial_zero_counter = 0

with open("puzzle_input", "r") as file:
    data = file.read()
    input_str_arr = data.split("\n")

for item in input_str_arr:
    # NOTE: Last item in array is empty.
    # NOTE: This probably has to do with how the split() function works.
    if (len(item) == 0):
        break

    direction = item[0]
    input = int(item[1:])

    # NOTE: Ignore movement in the hundreds, because a value of hundred will always go to the start position.
    input = input % MAX_POSITIONS 

    if (direction == 'L'):
        dial_point = dial_left(dial_point, input)
    elif (direction == 'R'):
        dial_point = dial_right(dial_point, input)
    else:
        raise ValueError("The direction is invalid.")

    if (dial_point == 0):
        dial_zero_counter += 1

print(f"Answer: {dial_zero_counter}")
