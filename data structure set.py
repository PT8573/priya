# #add krne k liye
# a={1,2,3,4,5}
# # y={7,8,9,10}
# a.add("priya")
# print(a)

#union
# y={"aipa","copa","cosmo","csa"}
# z={"fdt","dm","copa","tsdr"}
# print(y.union(z))
# print(y.intersection(z))
# print(y.difference(z))
# print(y.issubset(z))

#nested if in the dictornary(access )
# student={
#     "aipa":{"name":"sailesh","age":"20","trade":"aipa","address":"teliyarganj"},
#     "copa" :{"name":"raj","age":"20","trade":"copa","address":"civillins"},
#     "cosmo":{"name":"priya","age":"20","trade":"cosmo","address":"prayagraj"}
#     }
# # print(student)
# print(student["copa"]["address"])

# student={"name":"priya","age":"20","address":"teliyarganj"}
# # print(student["age"])
# # print(student["name"])

# #ADDING NEW KEY VALUE
# student["marks"]=89
# student["address"]="teliyarganj"
# print(student)

# #REMOVING FROM DICTIONARY 
# student.pop("age")
# print(student)

# #iterating over dictionary


patient=["priya","shivali","shipra","soni","sakshi","divyanshi"]
# disease=("blood canser")
blood_group={"A","B","AB","O_possitive"}
# # stage={"priya":"2ndstage","shivali":"1st satage","sakshi":"3rd stage","soni":"possitive"}



# # # print(patient)
# # # print(disease)
# # # print(blood_group)
# # # print(stage)

# # # print(patient[-2])
# # # print(patient[2:3])

patient.append("manvi")
# print(patient)

# print(blood_group)
# patient.insert(3,"komal")
# b=list(disease)
# print(b)

print(patient)
blood_group={
            "priya":{"blood_group":"A"},
             "shivali":{"blood_group":"B"},
             "shipra":{"blood_group":"AB"},

}
blood_group["manvi"]=["B negative"]
print(blood_group["manvi"]["blood_group"])











