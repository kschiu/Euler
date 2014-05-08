#Find the difference between the sum of the squares of the first one hunder natural numbers and the sum of the square.

def p6(n):
	sum_sq = (n * (n + 1) * (2*n + 1))/6
	sq_sum = ((n * (n + 1)) / 2) ** 2
	return sq_sum - sum_sq

#Solved in O(1) time with mathematical formulas.
