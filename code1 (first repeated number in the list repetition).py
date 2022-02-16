#first repeated number in the list repetition numbers

y=[]       
x=[1,2,3,2,3,5,6]
for i in range(len(x)):
    for j in range(len(x)):
        try:
            if x[i]==x[i+j+1]:
                y.append(x[i])
                
        except IndexError:
            pass
print(y.pop(0))
