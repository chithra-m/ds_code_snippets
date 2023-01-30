# import math
# n = 7
# i = 1
# while i <= int(math.sqrt(n)):
#     if (n % i) == 0:
#         print(n,i)
#         if (n // i) == i:
#             print(i)
#         else:
#             print(i, n//i)
    
#     i += 1
# A O(sqrt(n)) java program that prints
# all divisors in sorted order
import math

# Method to print the divisors
def printDivisors(n) :
	list = []
	
	# List to store half of the divisors
	for i in range(1, int(math.sqrt(n) + 1)) :
		
		if (n % i == 0) :
			
			# Check if divisors are equal
			if (n / i == i) :
				print ("dyh",i, end =" ")
			else :
				# Otherwise print both
				print ("iam",i, end =" ")
				list.append(int(n / i))
				
	# The list will be printed in reverse
	for i in list[::-1] :
		print (i, end =" ")
		
# Driver method
print ("The divisors of 100 are: ")
printDivisors(100)

# This code is contributed by Gitanjali
