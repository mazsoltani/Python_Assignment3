lenght_of_number = int(input("Please Enter Lenght of List= "))
list1= []
list_sort=[]
 
for i in range(0,lenght_of_number):
    print("i is=",i)
    number = int(input("Please Enter your number= "))
    list1.append(number)
    list_sort.append(number)
list_sort.sort()

if list1==list_sort:
    print("Your List is Sorted.")
else:
    print("Your List is not Sorted.") 