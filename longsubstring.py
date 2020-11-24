
def longsubstring(string):
	#enter a string
	substring=''
	lsubstring=''
	for i in range(len(string)):
		#print(substring)
		if substring.find(string[i])!= -1 or i==len(string):
			if len(substring)>len(lsubstring):
				lsubstring=substring
				substring=string[i]
				
		else:
			substring+=string[i]


	return f'The long substring is {lsubstring}'

print("Enter a word or phrase")
phrase=input()

print(longsubstring(string = phrase))
	