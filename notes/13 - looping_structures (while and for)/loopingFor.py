#-----------------------------------------------------------------------------
# Name:        Looping Structures - For (loopingFor.py)
# Purpose:     To provide information about how for loops work as a looping
#			   structure in Python
#
# Author:      Mr. Seidel, Mr Brooks
# Created:     17-Aug-2018
# Updated:     21-Sept-2021
#-----------------------------------------------------------------------------

# For loop to count up
for count in range(0, 5, 1):
    print(f'Count: {count}')


# For loop to count down
for count in range(5, 0, -1):
    print(f'Count: {count}')


# Using an "else" statement with a for loop
for count in range(0, 5, 1):
    print(f'Else Example: {count}')
else:
    print("This happens after the for loop ends")


# Breaking out of a loop early
for count in range(0, 5, 1):
    print(f'Count: {count}')
    if count == 2:
        break


# Using Continue to skip certain values
for count in range(0, 5, 1):
    if count % 2 == 0:       # skip EVEN numbers (and ZERO)
        continue             # immediately jump back to "while count < 10"
    print(f'Count: {count}')


# Using pass
for count in range(0, 5, 1):
    if count % 2 == 0:  # Plan to do something for EVEN numbers (and ZERO)
        pass
    elif count == 3:    # Plan something else for when count is 3
        pass
    print(f'Count: {count}')
