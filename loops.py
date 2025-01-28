list_of_cloud = ["aws", "gcp", "azure"]

print(list_of_cloud)

#adding new cloud
list_of_cloud.append("hostinger")


#we need to add print statement to shown recent updates
print(list_of_cloud)

list_of_cloud.append("oracle") #add to end of the list

print(list_of_cloud)

list_of_cloud.insert(2,"salesforce") #add where ever we want

print(list_of_cloud)

list_of_cloud.insert(0,"my cloud")

print(list_of_cloud)

#Itreation of a list
for cloud in list_of_cloud:
    print(cloud)