x = int(input())

h=1
for i in range(x):
	h=h*(int(input()))

print(h%(10^9+7))