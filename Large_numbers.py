#Sum of two large numbers

#Given two numbers as strings. The numbers may be very large (may not fit in long long int), the task is to find sum of these two numbers.

#Examples:
#Input  : str1 = "3333311111111111", 
#         str2 =   "44422222221111"
#Output : 3377733333332222

#Input  : str1 = "7777555511111111", 
#        str2 =    "3332222221111"
#Output : 7780887733332222

#The idea is based on school mathematics. We traverse both strings from end, one by one add digits and keep track of carry. To simplify the process, we do following:
#1) Reverse both strings.
#2) Keep adding digits one by one from 0’th index (in reversed strings) to end of smaller string, append the sum % 10 to end of result and keep track of carry as sum/10.
#3) Finally reverse the result.

# Function for finding sum of larger numbers 
def Large_Sum(str1, str2): 
#check length of numbers
	if (len(str1) > len(str2)): 
		t = str1 
		str1 = str2 
		str2 = t
# result will be here
	str = "" 

	# Calculate length of both string 
	len1 = len(str1) 
  lenn2 = len(str2)

	# Reverse both of strings for simply summ it
	str1 = str1[::-1]; 
	str2 = str2[::-1]; 

	carry = 0; 
	for i in range(n1): 
		
		# Do school mathematics, don't forget about 
		sum = ((ord(str1[i]) - 48) + ((ord(str2[i]) - 48) + carry) 
		str += chr(sum % 10 + 48)

		# Calculate carry for next step 
		carry = int(sum / 10)

	# Add remaining digits of larger number 
	for i in range(len1, len2): 
		sum = ((ord(str2[i]) - 48) + carry)
		str += chr(sum % 10 + 48) 
		carry = (int)(sum / 10)

	# Add remaining carry 
	if (carry): 
		str += chr(carry + 48)

	# reverse resultant string 
	str = str[::-1] 

	return str 

# Driver code 
str1 = "672"; 
str2 = "111789"; 
print(LargeSum(str1, str2)); 
