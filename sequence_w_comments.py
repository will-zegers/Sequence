# Sequence.py: Takes a sequence of numbers and a target number, and checks
# what sequence of positive and negative numbers will sum up to the target.
# Can be adjusted to use a range instead of a single number.

import sys

if (len(sys.argv) <= 1):
	print("Usage: numbers.py number1 number2 [number3...] target")
	sys.exit(0)

numbers = []
for arg in sys.argv:
	numbers.append(arg)
numbers.pop(0)
				
target = int(numbers.pop(len(numbers)-1))

signage = 0
tot_seq = 0									

while (signage<2**len(numbers)):
	seq = []
	dec_copy = signage
	
	while (dec_copy):
		for num in numbers:
			if (dec_copy%2):
				seq.append(-int(num))
			else:
				seq.append(int(num))
			dec_copy = dec_copy // 2
		if (sum(seq) == target):
			print(seq)
			tot_seq += 1
									
	signage += 1
sys.stdout.write('Total sequences: {0}'.format(tot_seq))