import csv

a=[]

with open("enjoysports.csv","r") as csvfile:
    next(csvfile)
    for row in csv.reader(csvfile):
        a.append(row)

print("The no. of rows in training instance are : ",len(a))

print(a)

num_attributes = len(a[0])-1

hypothesis = ['0']*num_attributes
print("The initial hypothesis is : ",hypothesis,"\n")

for i in range(len(a)):
    if a[i][num_attributes]=="yes":
        print("The instance ",i+1," is ",a[i]," and is positive instance.\n")
        for j in range(num_attributes):
            if a[i][j] == hypothesis[j] or hypothesis[j] == '0':
                hypothesis[j] = a[i][j]
            else:
                hypothesis[j] = '?'
        print("The Hypothesis of the instance ",i+1," is ",hypothesis,"\n")
    else:
        print("The instance ", i + 1, " is ", a[i], " and is negative instance and hence ignored.\n")
        print("The Hypothesis of the instance ", i + 1, " is ", hypothesis, "\n")

print("The maximum specific hypothesis is ",hypothesis)


