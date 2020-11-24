#counting bobs
def countingbobs(sentence):
    #enter a string
    cont=0
    i=0
    sentence=sentence.lower()

    for i in range(len(sentence)):
        word = sentence[i:i+3]
        if word == 'bob':
            cont+=1

    return f'There are {cont} bob'

d=countingbobs(sentence= 'bobo es bob por que bobea mucho bobobob')
print(d)