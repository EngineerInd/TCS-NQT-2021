# Python3 program for the above approach 

# Import combinations 
from itertools import combinations 

# Function to check the string pair 
def string_pair(n, nums): 
	words = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 
			4: 'four', 5: 'five', 6: 'six', 7: 'seven', 
			8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 
			12: 'twelve', 13: 'thirteen', 14: 'fourteen', 
			15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 
			18: 'eighteen', 19: 'nineteen', 20: 'twenty', 
			21: 'twentyone', 22: 'twentytwo', 23: 'twentythree', 
			24: 'twentyfour', 25: 'twentyfive', 26: 'twentysix', 
			27: 'twentyseven', 28: 'twentyeight', 29: 'twentynine', 
			30: 'thirty', 31: 'thirtyone', 32: 'thirtytwo', 
			33: 'thirtythree', 34: 'thirtyfour', 35: 'thirtyfive', 
			36: 'thirtysix', 37: 'thirtyseven', 38: 'thirtyeight', 
			39: 'thirtynine', 40: 'forty', 41: 'fortyone', 
			42: 'fortytwo', 43: 'fortythree', 44: 'fortyfour', 
			45: 'fortyfive', 46: 'fortysix', 47: 'fortyseven', 
			48: 'fortyeight', 49: 'fortynine', 50: 'fifty', 
			51: 'fiftyone', 52: 'fiftytwo', 53: 'fiftythree', 
			54: 'fiftyfour', 55: 'fiftyfive', 56: 'fiftysix', 
			57: 'fiftyseven', 58: 'fiftyeight', 59: 'fiftynine', 
			60: 'sixty', 61: 'sixtyone', 62: 'sixtytwo', 
			63: 'sixtythree', 64: 'sixtyfour', 65: 'sixtyfive', 
			66: 'sixtysix', 67: 'sixtyseven', 68: 'sixtyeight', 
			69: 'sixtynine', 70: 'seventy', 71: 'seventyone', 
			72: 'seventytwo', 73: 'seventythree', 74: 'seventyfour', 
			75: 'seventyfive', 76: 'seventysix', 77: 'seventyseven', 
			78: 'seventyeight', 79: 'seventynine', 80: 'eighty', 
			81: 'eightyone', 82: 'eightytwo', 83: 'eightythree', 
			84: 'eightyfour', 85: 'eightyfive', 86: 'eightysix', 
			87: 'eightyseven', 88: 'eightyeight', 89: 'eightynine', 
			90: 'ninety', 91: 'ninetyone', 92: 'ninetytwo', 
			93: 'ninetythree', 94: 'ninetyfour', 95: 'ninetyfive', 
			96: 'ninetysix', 97: 'ninetyseven', 98: 'ninetyeight', 
			99: 'ninetynine', 100: 'hundred'} 

	# Map the string into list of integers 
	nums = list(map(int, nums)) 

	# Temporary lists to store list of count 
	ls, ls1 = [], [] 
	count, c = 0, 0

	# Iterating through the numbers 
	for i in nums: 

		# Stores the textual form of i 
		s = words[i] 
		for a in range(len(s)): 
			vo = ['a', 'e', 'i', 'o', 'u'] 

			# If it is vowel 
			if s[a] in vo: 

				# Increment the count 
				count += 1

		# Append the count 
		ls.append(count) 
		count = 0

	# D = sum(count of vowels) 
	d = sum(ls) 
	for i in nums: 

	# To find the numbers less 
	# that or equal to d, 
	# so as to find the pair sum 
		if i <= d: 

			# Append the numbers 
			# whose sum can be d 
			ls1.append(i) 

	# Stores all possible pairs in the 
	# form of an object list of tuples 
	comb = combinations(ls1, 2) 

	# Traverse all the pairs 
	for i in list(comb): 

		# If sum is equal to d 
		if sum(i) == d: 

			# Increment count 
			c += 1

	# If count exceeds 100 
	if c <= 100: 
		print(words) 

	# Otherwise 
	else: 
		print("greater 100") 


# Driver Code 
if __name__ == '__main__': 

	# Given Length of string 
	n = 5

	# Given array 
	arr = [1, 2, 3, 4, 5] 

	# Function Call 
	string_pair(n, arr) 
