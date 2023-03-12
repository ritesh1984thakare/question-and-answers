print("Q1:do you like Dawn or Dusk?")
print("   1) = Dawn")
print("   2) = Dusk")
answer1 = int(input("Enter your preference:"))
if answer1 == 1:
    print("gryffindor and Ravenclaw")
elif answer1 == 2:
    print("Hufflepuff and slytherin ")
else:
    print("Wrong input")
if answer1 == 1 or 2:
    print("Points:",+1)

print("Q2:When I'm dead, I want people to remember me as?")
print("   1) = The Good")
print("   2) = The Great")
print("   3) = The Wise")
print("   4) = The Bold")
answer2 = int(input("Enter your preference:"))
if answer2 == 1:
    print("Hufflepuff")
elif answer2 == 2:
    print("slytherin")
elif answer2 == 3:
    print("Ravenclaw")
elif answer2 == 4:
    print("Gryffindor")
else:
    print("Wrong input")
if answer2 == 1 or 2 or 3 or 4:
    print("points:",+2)

print("Q3:Which kind of instrument most pleases your ear?")
print("   1) = The Violin")
print("   2) = The trumpet")
print("   3) = The piano")
print("   4) = The drum")
answer3 = int(input("Enter your preference:"))
if answer3 == 1:
    print("slytherin")
elif answer3 == 2:
    print("Hufflepuff")
elif answer3 == 3:
    print("Ravenclaw")
elif answer3 == 4:
    print("Gryffindor")
else:
    print("Wrong input")
if answer3 == 1 or 2 or 3 or 4:
    print("points:",+4)
all= answer1,answer2,answer3
print("All answers:",all)

all_answers= answer1+answer2+answer3
print("All points total:",all_answers)
