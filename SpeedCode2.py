## Given two integer arrays a, b, both of length >= 1, 
## create a program that returns true 
## if the sum of the squares of each element in a, 
## is strictly greater than the sum of the cubes of each element in b.

def SpeedCode2(a,b):
	return sum(x ** 2 for x in a) > sum(x **3 for x in b)

aye = [3,2,3]
bee = [2,1,1]

print(SpeedCode2(aye,bee))
