import random
lenght_of_number = int(input("Please Enter Lenght of List= "))
list1= []
 
for i in range(0,lenght_of_number):
    number = random.randint(1,lenght_of_number)
    list1.append(number)
    #list1.append(number
   # Mylist_none_repeat = list(dict.fromkeys(my_list))
print(list1)
finalData = list(set(list1))
print(finalData)


