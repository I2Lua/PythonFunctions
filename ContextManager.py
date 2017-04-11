class ListTrakzation():
	def __init__(self, thelist):
		self.thelist = thelist

	def __enter__(self):
		self.workingcopy = self.thelist
		return self.workingcopy

	def __exit__(self, exc, value, traceback):
		if exc is None:
			self.thelist[:] = self.workingcopy
		return False

items = [1, 2, 3]

with ListTrakzation(items) as working:
	working.append(4)
	working.append(5)

print(items)
