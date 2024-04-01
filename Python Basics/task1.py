'''Use loops to accept 5 values from user and store them in a list. Display all the values
(objects) of the list.'''

value_list=[]

for i in range(5):
    value=input("Enter Value: ")
    value_list.append(value)

print("Values Stored in the list: ")

for j in value_list:
    print (j)