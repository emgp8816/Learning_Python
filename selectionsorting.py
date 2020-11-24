import random
from datetime import datetime

#Selection Sorting
def selectionsort(list):
	print(f'The original list is {list}')
	b=len(list)
	list2=list[:]
	for j in range(b):
		a=list[0]
		for i in range(b-j):
			if list[i]<a:
				a=list[i]
		list2[j]=a
		list.pop(list.index(a))
	return f'The ordered list is {list2}'

#random list generator
def randomlist(n,m):
      lists = [0]  * n
      for i in range(n):
          lists[i] = round(m*random.random())
      return lists

#user's input
print("Choose the length of the list")
n=int(input())
print("Choose the maximum limit of the list")
m=int(input())

#stars cronometer
firstinstant = datetime.now()

print(selectionsort(list =randomlist(n,m)))

#finishes cronometer
finalinstant = datetime.now()
time = finalinstant - firstinstant

#running time
print(f'Running time: {time}')