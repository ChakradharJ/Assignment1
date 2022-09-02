# create Empty dog dictionary
dog={
}

# add name, color, legs,breed, age to dog dictionary
dog["name"]="Cho_Cho"
dog["color"]="White"
dog["legs"]=4
dog["breed"]="Labrador"
dog["age"]=5


#create student dictionary firstname, lastname, gender,age,maritalstatus,skills,country,city,address
student={
    "first_name":"Chakradar",
    "last_name":"Jonnalagadda",
    "gender":"Male",
    "age":23,
    "marital_status":"Single",
    "skills":["Python","Java Script","Salesforce"],
    "country":"USA",
    "city":"Overland_Park",
    "address":"Makcey_Street"
}


#get the length of the student dictionary

length=len(student)
print("The length of student dictionary is : \n{}".format(length))

#get the value of the skills and check the data type ,it should be list
x=[]
x=student["skills"]
print("The skills are : {} \n".format(x))
print("Type of skills is : {} \n ".format(type(x)))


#modify the skills by adding one or two skills

student["skills"].append("Java")
print("The updated skills :{} \n".format(student["skills"]))

#get the dictionary keys as a list

Student_keys=list(student.keys())
Dog_keys=list(dog.keys())

print("The keys are of student dictionary are : {} \n".format(Student_keys))
print("The keys are of dog dictionary are : {} \n".format(Dog_keys))


#get the dictionary values a list

student_values=list(student.values())
dog_values=list(dog.values())

print("The values of student dictionary are : {} \n".format(student_values))
print("The values of dog dictionary are : {} \n".format(dog_values))

