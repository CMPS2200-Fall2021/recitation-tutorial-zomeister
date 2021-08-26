def sum_of_squares(a):
	sum = 0
	for i in range(len(a)):
		sum += (a[i]*a[i])
	return sum

def test_one():
    assert sum_of_squares([1,2,3]) == 14

def test_two():
	assert sum_of_squares([2, 2, 1, 3]) == 18
