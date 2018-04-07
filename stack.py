def push(x):
	l.append(x)

def pop():
	l.pop()

def peek():
	return l[-1]

def min_stack():
	return min(l)

if __name__=='__main__':
	l = []
	push(2)
	push(3)
	push(4)
	print("peeking",peek())
	print(min_stack())
	pop()
	print("peeking",peek())