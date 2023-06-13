
Names: umwizerwa Gedeon
  department:Information Technology
    REGno:221017217
      
      #stage 1
      # stage1
friends_no = int(input("Enter the number of friends and joining  (including you):\n"))

if friends_no <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    friends = {}
    for _ in range(friends_no):
        name = input()
        friends[name] = 0
    print(friends)

    #stage 2
# write your code here

friends_no = int(input("Enter the number of friends joining (including you):\n"))
if friends_no <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    friends = {}
    for _ in range(friends_no):
        name = input()
        friends[name] = 0
    amount = int(input("Enter the total bill value:"))
    ones_amount = amount/friends_no
    print()
    bill_splitting = round(ones_amount, 2)
    for person in friends:
        friends[person] = bill_splitting
    print(friends)

    
#stage 3

# write your code here

import random
friends_no = int(input("Enter the number of friends joining (including you):\n"))

if friends_no <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    friends = {}
    for _ in range(friends_no):
        name = input()
        friends[name] = 0
    amount = int(input("Enter the total bill value:"))
    ones_amount = amount/friends_no
    print()
    bill_splitting = round(ones_amount, 2)
    for person in friends:
        friends[person] = bill_splitting
    print("Do you want to use the 'Who is lucky?' feature? Write Yes/No:")
    response = input()
    if (response.upper() == "YES"):
        random_lucky = random.choice(list(friends))
        print("{} is the lucky one!".format(random_lucky))
    else:
        print("No one is going to be lucky")


#stage 4
# write your code here

#write your code     

import random
friends_no = int(input("Enter the number of people joining (including yourself): \n"))
if friends_no <= 0:
    print("No one is joining for the party")
else:
    friends = {}
    print("")
    print('Enter the name of person ')
    for i in range(friends_no):
        name = input("")
        friends[name] = 0
    print("")
    print("Enter the total bill amount: ")
    final_bill = float(input())
    split_value = round(final_bill /friends_no+friends_no, 2)
    for guest in friends:
        friends[guest] =  split_value
    print("")
    print("Do you want to use the 'Who is lucky?' feature? (Yes/No): ")
    use_lucky_feature = input()
    if use_lucky_feature.lower() == "yes":
        lucky_person = random.choice(list(friends.keys()))
        print("")
        print(f"{lucky_person} is the lucky one!")
        # split_value = round(final_bill / friends_no, 2)
        for guest in friends:
          if guest == lucky_person:
            split_value = 0
            friends[guest]=split_value
        print(friends)    
    else:
        print("")
        print("No one is going to be lucky")
        for guest in friends:
          # if guest == lucky_person:
            split_value = round(final_bill / friends_no, 2)
            friends[guest]=split_value
        print(friends)

    
