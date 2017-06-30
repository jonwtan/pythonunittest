from __future__ import division

	
def CircleArea(radius):
    return 3.141 * radius * radius

	
R = float(raw_input("Enter a radius of the circle: "))

print "The area of the circle is:", CircleArea(R), "units^2"