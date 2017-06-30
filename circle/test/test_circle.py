'''
simulation of a simple function to return an area of a circle
'''

from __future__ import division
	
def CircleArea(radius):
    return 3.141 * radius * radius


class TestClass(object):

	# asserts a Right answer... a circle with radius 5 has an area of 78.525
	def test_answer1(self):
		assert CircleArea(5) == 78.525

	# asserts a Wrong answer...
	def test_answer2(self):
		assert CircleArea(5) == 50
	
	# Wrong answer
	def test_answer3(self):
		assert CircleArea(7) == 85
	
	# Wrong answer
	def test_answer4(self):
		assert CircleArea(60) == 182
	
	# Right Answer
	def test_answer5(self):
		assert CircleArea(60) == 11307.6
	
	# entered a string instead of a number
	def test_answer6(self):
		assert CircleArea("circle") == 11307.6