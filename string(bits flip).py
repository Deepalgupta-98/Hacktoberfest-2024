# python program to check if a single
# bit can be flipped tp make all ones

# This function returns true if we can
# bits same in given binary string str.
def canMakeAllSame(str):
	zeros = 0
	ones = 0

	# Traverse through given string and
	# count numbers of 0's and 1's
	for i in range(0, len(str)):
		ch = str[i];
		if (ch == '0'):
			zeros = zeros + 1
		else:
			ones = ones + 1

	# Return true if any of the two
	# counts is 1
	return (zeros == 1 or ones == 1);

# Driver code
if(canMakeAllSame("101")):
	print("Yes\n")
else:
	print("No\n")

# This code is contributed by Sam007.
