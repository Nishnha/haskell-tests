def higher(num1, num2):
	if num1 > num2:
		return num1
	else:
		return num2

num1 = 60*24*365
num2 = 60*60*1000*24

print("of the numbers " + str(num1) + " and " +  str(num2) + "," + str(higher(num1, num2)) + " is greater")
print("of the numbers {} and {}, {} is greater").format(num1, num2, higher(num1, num2))
#print(higher_of_2)

# i = 3
# s = 'hello'
#
# def concat(a,b):
# 	return str(a) + str(b)
#
# result = concat(i, s)
# print(result)
