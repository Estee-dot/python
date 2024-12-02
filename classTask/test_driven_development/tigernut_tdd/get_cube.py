def get_cube(numbers):
	cube = []
	for number in numbers:
		cube.append(number**3)
	return cube


def cube_list():
	return get_cube([i for i in range(1,6)])

print(cube_list())


def get_cube(numbers):
	return[(num**3) for num in numbers]


print(get_cube(uzo()))