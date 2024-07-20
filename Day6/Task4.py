''' Task 4: Lets say you are running a 5 km race. Write a program that,
        1. Upon completing each 1 km asks you "are you tired?"
        2. If you reply "yes" then it should break and print "you didn't finish the race"
        3. If you reply "no" then it should continue and ask "are you tired" on every km
        4. If you finish all 5 km then it should print congratulations message '''

# Solution
for i in range(1,6):
    print("km",i)
    reply = input("are you tired? ")
    if reply == "yes":
        print("you didn't finish the race")
        break
    elif reply == "no":
        continue
    else:
        print("invalid input")

# Output
'''
km 1
are you tired? no
km 2
are you tired? no
km 3
are you tired? yes
you didn't finish the race
'''