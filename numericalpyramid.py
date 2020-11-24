#numericalpyramid
def numericalpyramid(num):
    #enter a number
    row=[]
    number=0
    b=num-1
    k=0

    for j in range(num):
        row.append(j)

    for k in range(2*num-2):   
        if k<num:
            for l in range(num):
                if l<=k:
                    print(k+1,end='')
                    if l==k:
                        print('\n')
        else:
            for l in range(num):
                c=num-abs(num-k-1)
                if l<=b:
                    print(b,end='')
                    if l==b-1:
                        print('\n')
                        b-=1


print("Enter a number")
n=int(input()
                     
numericalpyramid(num= n)