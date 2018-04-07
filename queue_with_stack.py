class stack:
	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def pop_s(self):
		x = self.items.pop()
		return x

	def push(self, x):
		(self.items).append(x)

	def min_ele(self):
		return min(self.items)

	def top(self):
		return self.items[-1]

	def size_st(self):
		return len(self.items)

class queue:
	def __init__(self):
		self.ins = stack()
		self.outs = stack()

	def enqueue(self, x):
		self.ins.push(x)

	def min_ele(self):
		return (self.ins.min_ele())

	def dequeue(self):
		if(self.outs.is_empty()):
			while(1):
				if(self.ins.is_empty()==True):
					break
				self.outs.push(self.ins.pop_s())
		self.outs.pop_s()

	def front(self):
		if(self.outs.is_empty()):
			while(1):
				if(self.ins.is_empty()==True):
					break
				self.outs.push(self.ins.pop_s())
		return self.outs.top()



if __name__ == '__main__':
	q1 = queue()
	q1.enqueue(19)
	q1.enqueue(12)
	q1.enqueue(13)
	q1.enqueue(14)
	q1.enqueue(15)

	print(q1.front())
