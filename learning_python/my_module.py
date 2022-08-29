def test_func(content):
	print(f'this is an imported function with the parameter: {content}')

test_var = 'test'

class my_class:
	def __init__(self):
		self.name = 'My App'
		self.value = 12

	def do_something(self):
		print('hello')
		#click command and click the top to see both at the same time
		#create a sum calc function with unlimited arguments 


def sum_calc(*nums):
		#star before category tells python to unpack
	return sum(nums)


print(__name__)
print(':)')