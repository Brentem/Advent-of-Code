# TODO: (IMPORTANT) use % operator on input to filter/cap values that are above 100.

DIAL_MIN = 0
DIAL_MAX = 99
OFFSET = 1

input_str_arr = ["", ""]
# dial_point = 50
dial_point = 5

with open("puzzle_input", "r") as file:
    data = file.read()
    input_str_arr = data.split("\n")

test_input_l = 10
if (dial_point - test_input_l) < DIAL_MIN:
    test_input_l = test_input_l - dial_point - OFFSET # = 4
    dial_point = DIAL_MAX - test_input_l # = 95
    print(dial_point)

test_input_r = 10
if (dial_point + test_input_r) > DIAL_MAX:
    test_input_r = (dial_point + test_input_r) - DIAL_MAX # = 6
    dial_point = DIAL_MIN + (test_input_r - OFFSET) # 5
    print(dial_point)

# Different situation for dial left.
test_input_l = 10
dial_point = DIAL_MIN
if (dial_point == DIAL_MIN):
    dial_point = DIAL_MAX - (test_input_l - OFFSET) # 90
    print(dial_point)

# Different situation for dial right.
test_input_r = 10
dial_point = DIAL_MIN
if (dial_point == DIAL_MIN):
    dial_point = dial_point + test_input_r # 10
    print(dial_point)

# Different situation for dial left.
test_input_l = 10
dial_point = DIAL_MAX
if (dial_point == DIAL_MAX):
    dial_point = dial_point - test_input_l # 89
    print(dial_point)

# Different situation for dial right.
test_input_r = 10
dial_point = DIAL_MAX
if (dial_point == DIAL_MAX):
    dial_point = DIAL_MIN + (test_input_r - OFFSET) # 9
    print(dial_point)
