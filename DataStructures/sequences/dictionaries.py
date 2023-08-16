#  collection of key and value pairs 
#  access of values is made available by the key 
#  unordered , mutable , 

student = {
  "name" : "Joseph",
  "age" : "20",
  "major" : "Computer Science"
}

# CRUDING 
studentName = student["name"]
student["age"] = 26
student["emergencyContact"] = "079434..."
del student["age"]

# inbuilt methods 
# .get("key") : access 
# student.keys() : reveal the key names 
# student.values() : reveal all values 
# checking for a key : in keyword 
#  .copy : duplicate a dictionary 
# dict(student) : duplicate 


# NESTED DICTIONARY 
myFamily = {
    "child1" : {
        "name" : "",
        "age" : ""
    }, 
      "child2" : {
        "name" : "",
        "age" : ""
    },
      "child3" : {
        "name" : {
            "firstname" : "ann",
            "secondname" : "doe"
        },
        "age" : ""
    }
}

print(myFamily["child3"]["name"]["firstname"])