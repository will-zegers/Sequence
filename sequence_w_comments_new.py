# Sequence.py: Takes a sequence of numbers and a target number, and checks
# what sequence of positive and negative numbers will sum up to the target.
# Can be adjusted to use a range instead of a single number.

import sys

if (len(sys.argv) <= 1):		# Input validation
	print("Usage: numbers.py number1 number2 [number3...] target")
	sys.exit(0)

numbers = []
for arg in sys.argv:
	numbers.append(arg)
numbers.pop(0)

target = int(numbers.pop(len(numbers)-1))

dec_num = 0							# Dec_num will enumerate through all possible
while (dec_num<2**len(numbers)):	# binary combinations, and each combo will
									# be used to determine the signage of the 
									# sequence of numbers (1s for neg, 0s for pos)
									# i.e 101001 = (neg, pos, neg, pos, pos, neg)
	seq = []
	dec_copy = dec_num				# Copies dec_num, so a binary sequence can
									# can be generated but leave the number intact
	
	while (dec_copy > 0):				# Using a (relatively) well-known algorithm
		for num in numbers:				# that generates each binary digit of a decimal
			if (dec_copy%2 == 1):		# number. If the generated digit is a '1', the
				seq.append(-int(num))	# corresponding number for that digit's place
			else:						# is negative; positive otherwise
				seq.append(int(num))
			dec_copy /= 2
			
	print((seq))
	if (sum(seq) == target):		# With the sequence of negative and positive,
		print(seq)					# sum them all up and compare them to the target.
									# Print if its a match
									
	dec_num += 1					# Next binary number sequence