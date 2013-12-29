# Sequence.py: Takes a sequence of numbers and a target number, and checks
# what sequence of positive and negative numbers will sum up to the target.
# Can be adjusted to use a range instead of a single number.

import sys, time

tot_seq = 0	

def main(argv):

	if (len(argv) <= 1):
		print("Usage: numbers.py number1 number2 [number3...] target")
		sys.exit(0)

	numbers = []

	for arg in argv:
		numbers.append(int(arg))
					
	target = int(numbers.pop(len(numbers)-1))
	
	findSequence(numbers, target, 0, 2**len(numbers))
	
	sys.stdout.write('Total sequences: {0}'.format(tot_seq))

def findSequence(numbers, target, start, stop):
	global tot_seq
	signage = start								

	while (signage < stop):
		sign_copy = signage
		sequence = []
		
		if((sign_copy == 0) and (sum(numbers) == target)):
			print(numbers)
			tot_seq += 1
		else:
			while (sign_copy > 0):
				for num in numbers:
					if (sign_copy%2):
						sequence.append(-int(num))
					else:
						sequence.append(int(num))
					sign_copy = sign_copy // 2
				
				print(sum(sequence))
				if (sum(sequence) == target):
					print(sequence)
					tot_seq += 1
			signage += 1
	
if __name__ == "__main__":
	main(sys.argv[1:])