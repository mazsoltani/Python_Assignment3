import random
words=["book","tree","python","bag","umrella","clock","engineer","toothpase","shirmoz"]
#i=random.randint(0,len(words)-1)
#print(i)
#word=words[i]
#print(word)
word=random.choice(words) #clock
#print(word)
list=[]
for i in range(len(word)):
    list.append('_')
print(list)
joon=int(input("Please choice Your number of Select for example 12  =="))
while joon>0:

    print(''.join(list))
        
    if ((''.join(list)) == word):
        print('************ You are Win **********',"your Joon is=",joon)
        break
    user_character=input("Please Enter your Character=") # s
    user_character=user_character.lower()
    
    if user_character in word:
        print("your Character is True... your Joon is",joon)
        for i in range(len(word)):
            if word[i]==user_character:
                list[i]=user_character
                print(list[i])

    else:

        joon=joon-1
        print("Your Character is Mistake.",joon)
 
