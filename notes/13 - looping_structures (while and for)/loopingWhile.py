#-----------------------------------------------------------------------------
# Name:        Looping Structures - While (loopingWhile.py)
# Purpose:     To provide information about how while loops work as a looping
#			   structure in Python
#
# Author:      Mr. Seidel, Mr. Brooks
# Created:     17-Aug-2018
# Updated:     21-Sept-2021
#-----------------------------------------------------------------------------

# Using a while loop to count up
count = 1
while count < 10:
	print(f'Counter Value: {count}')
	count = count + 1		# this can also be written as count += 1
	

# Using a while loop to count down
count = 275
while count > 250:
	count = count - 1		# this can also be written as count -= 1
	if count % 2 == 0:
		print(f"{count}: This number is even")


# Creating an infinite loop.  This loop won't stop.
count = 1
while count == 1:
	print("Count is equal to the number 1")
	

# Using an "else" statement with a while loop
count = 1
while count < 10:
	print(f'2*{count} = {2 * count}')
	count += 1
else:
	print("Done")

	
# Breaking out of a loop early
count = 1
while count < 10:
    print(f'Count: {count}')
    if count == 5:
        break
    count += 1

	
# Using Continue to skip certain values
count = 1
while count < 10:
	count += 1
	if count % 2 == 0:	# skip EVEN numbers (and ZERO)
		continue		# immediately jump back to "while count < 10"
	print(f'Count: {count}')
	
# Using pass
count = 1
while count < 10:
	count += 1
	if count % 2 == 0:	# Plan to do something for EVEN numbers (and ZERO)
		pass
	elif count == 5:	# Plan something else for when count is 5
		pass
	print(f'Count: {count}')
	