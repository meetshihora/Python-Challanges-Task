''' Task 1: Take subject marks as command line arguments

        example: 
        python3 cmd.py --physics 60 --chemistry 70 --maths 90 '''

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--physics', type=int)
parser.add_argument('--chemistry', type=int)
parser.add_argument('--maths', type=int)

args = parser.parse_args()

physics = args.physics
chemistry = args.chemistry
maths = args.maths

print(f"Physics: {physics}, Chemistry: {chemistry}, Maths: {maths}")

# Task 2: Find average marks for the three subjects using command line input of marks.

if (physics and chemistry and maths):
    average = (physics + chemistry + maths) / 3
    print(f"Average: {average}")
else:
    print("Please provide marks for all subjects")
