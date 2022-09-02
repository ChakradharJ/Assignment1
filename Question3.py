#create a tuple names of your sisters and brothers
brothers=("Mahesh","Pavan","Tarak")
sisters=("Swetha","Sravani","Maggie")

#join brothers and sisters and assign to sibilings
siblings=brothers+sisters
print(siblings)

#how many sibilinga do you have
length=len(siblings)
print(length)

#modify tuple and add the names of your father and mother and assign to family members

#converting set to list
sibiling=list(siblings)

#appending mother and father names to the list
sibiling.append("Chandu")
sibiling.append("Sravs")

#converting sibiling to set and assiging the set to family_members
family_members=set(sibiling)
print(family_members)
