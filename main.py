groupOne = [["nameone", "perferenceone", "perferencetwo", "perferencethree", "perferencefour", "suitorone", "suitortwo", "suitorthree", "suitorfour"], ["nametwo", "perferenceone", "perferencetwo", "perferencethree", "perferencefour", "suitorone", "suitortwo", "suitorthree", "suitorfour"], ["namethree", "perferenceone", "perferencetwo", "perferencethree", "perferencefour", "suitorone", "suitortwo", "suitorthree", "suitorfour"], ["namefour", "perferenceone", "perferencetwo", "perferencethree", "perferencefour", "suitorone", "suitortwo", "suitorthree", "suitorfour"]]
groupTwo = [["nameone", "perferenceone", "perferencetwo", "perferencethree", "perferencefour", "suitorone", "suitortwo", "suitorthree", "suitorfour"], ["nametwo", "perferenceone", "perferencetwo", "perferencethree", "perferencefour", "suitorone", "suitortwo", "suitorthree", "suitorfour"], ["namethree", "perferenceone", "perferencetwo", "perferencethree", "perferencefour", "suitorone", "suitortwo", "suitorthree", "suitorfour"], ["namefour", "perferenceone", "perferencetwo", "perferencethree", "perferencefour", "suitorone", "suitortwo", "suitorthree", "suitorfour"]]

print("Welcome to Online Matchmaker! Input the names of 4 people who you want to find a match! (these people will not match with each other)")

def checkMatch(group):
    count = False
    for i in range (4):
        if group[0][i + 5] is True and count is True:
            return count
        elif group[0][i + 5] is True:
            count = True
    count = False
    for i in range (4):
        if group[1][i + 5] is True and count is True:
            return count
        elif group[1][i + 5] is True:
            count = True
    count = False
    for i in range (4):
        if group[2][i + 5] is True and count is True:
            return count
        elif group[2][i + 5] is True:
            count = True
    count = False
    for i in range (4):
        if group[3][i + 5] is True and count is True:
            return count
        elif group[3][i + 5] is True:
            count = True
    return False

for i in range (4):
    groupOne[i][0] = input()
print("Now input the names of 4 different people for your initial 4 people to match with!")
for i in range (4):
    groupTwo[i][0] = input()
print("Now its time to input preferences!")
for i in range (4):
    print("Who does", groupOne[i][0], "prefer out of:", groupTwo[0][0], groupTwo[1][0], groupTwo[2][0], groupTwo[3][0] + "? ")
    groupOne[i][1] = input()
    tempPref = groupOne[i][1]
    tempName = i
    groupOne[i][2] = input("Who is their second choice? ")
    groupOne[i][3] = input("Who is their third choice? ")
    groupOne[i][4] = input("Who is their fourth choice? ")
    for i in range (4):
        if groupTwo[i][0] == tempPref.lower():
            groupTwo[i][tempName + 5] = True
for i in range (4):
    print("Who does", groupTwo[i][0], "prefer out of:", groupOne[0][0], groupOne[1][0], groupOne[2][0], groupOne[3][0] + "? ")
    groupTwo[i][1] = input()
    tempPref = groupTwo[i][1]
    tempName = i
    groupTwo[i][2] = input("Who is their second choice? ")
    groupTwo[i][3] = input("Who is their third choice? ")
    groupTwo[i][4] = input("Who is their fourth choice? ")
    for i in range (4):
        if groupOne[i][0] == tempPref.lower():
            groupOne[i][tempName + 5] = True
    for i in range (4):
        if groupTwo[i][0] == tempPref.lower():
            groupTwo[i][tempName + 5] = True

checkOne = checkMatch(groupOne)
checkTwo = checkMatch(groupTwo)

if checkOne is False:
    for i in range(4):
        if groupOne[0][i + 5] is True:
            groupOne[0][1] = groupTwo[i][0]
    for i in range(4):
        if groupOne[1][i + 5] is True:
            groupOne[1][1] = groupTwo[i][0]
    for i in range(4):
        if groupOne[2][i + 5] is True:
            groupOne[2][1] = groupTwo[i][0]
    for i in range(4):
        if groupOne[3][i + 5] is True:
            groupOne[3][1] = groupTwo[i][0]
    print(groupOne[0][0], "has been matched with", groupOne[0][1])
    print(groupOne[1][0], "has been matched with", groupOne[1][1])
    print(groupOne[2][0], "has been matched with", groupOne[2][1])
    print(groupOne[3][0], "has been matched with", groupOne[3][1])
if checkTwo is False:
    for i in range(4):
        if groupTwo[0][i + 5] is True:
            groupTwo[0][1] = groupOne[i][0]
    for i in range(4):
        if groupTwo[1][i + 5] is True:
            groupTwo[1][1] = groupOne[i][0]
    for i in range(4):
        if groupTwo[2][i + 5] is True:
            groupTwo[2][1] = groupOne[i][0]
    for i in range(4):
        if groupTwo[3][i + 5] is True:
            groupTwo[3][1] = groupOne[i][0]
    print(groupTwo[0][0], "has been matched with", groupTwo[0][1])
    print(groupTwo[1][0], "has been matched with", groupTwo[1][1])
    print(groupTwo[2][0], "has been matched with", groupTwo[2][1])
    print(groupTwo[3][0], "has been matched with", groupTwo[3][1])