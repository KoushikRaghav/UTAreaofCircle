import math

def areaofcircle(radius):
	area = math.pi * radius**2
	print area
	return area

if __name__ == '__main__':
	radius=int(input("Enter radius: "))
	areaofcircle(radius)