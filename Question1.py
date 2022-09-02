
age=[19,22,19,24,20,25,26,24,25,24]

#sorting the list using sort method

age.sort()
print("The sorted age is: \n{} ".format(age))

#sorting without using sort method
#for a in range(len(age)):
    #for b in range(a + 1, len(age)):

       # if age[a] > age[b]:
           # age[a], age[b] = age[b], age[a]

#print(age)


#min & max using min and max functions

min=min(age)
max=max(age)
print("The minimum age is {} and maximum age is {} \n".format(min,max))


#adding min and max age to the list with method.
age.append(min)
age.append(max)
print("Age after appending the minimum and maximum age is :\n {}".format(age))


#median

count=len(age)
median=int(count/2)
print("Median is : {}".format(age[median]))

#average

total=sum(age)
average=total/count
print("Average is : {}".format(average))

#range

range=max-min
print("Range is : {}".format(range))