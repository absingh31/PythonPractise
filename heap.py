import heapq

#heap functions ============>>>>
'''
1). heapq.heapify(yourlist)
2). heapq.heappush(yourlist, new_item)
3). heapq.heappop(yourlist)     ==>  This pops the smallest element
4). heapq.nlargest(number, yourlist) ==> Returns top 3 largest element
5). heapq.nsmallest(number, yourlist) ==> Return smallest 3 elements of the heap
6). heapq.heappushpop(yourlist, item) ==> increased efficiency, push first then pop smallest element of the heap
7). heapq.heapreplace(yourlist, item) ==> when you want to save memory, first pops and then push
'''

def main():
	heap = [1,3,2,66,4]

	heapq.heapify(heap)

	heapq.heappush(heap, 15)

	print(heapq.nsmallest(3, heap))

	print(heapq.nlargest(3, heap))