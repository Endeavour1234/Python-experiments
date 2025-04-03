
# we are going to play a computer quiz game

play = input("Do you want to play a computer quiz game ? ").lower()

if play == "yes":
    print("That's gr8 ! Let's play : ) ")
    score = 0
else :
    print("You're no fun !! : ( ")
    quit()

ans1 = input("what's does CPU stand for ? ").lower()
if ans1 == "central processing unit":
    print("Bingo ! That's correct ! ")
    score += 1
else:
    print ("That's not right buddy.. sorry !")

ans2 = input("what's does ALU stand for ? ").lower()
if ans2 == "arithmetic logic unit":
    print("Bingo ! That's correct ! ")
    score += 1
else:
    print ("That's not right buddy.. sorry !")

ans3 = input("what's does GPU stand for ? ").lower()
if ans3 == "graphics processing unit":
    print("Bingo ! That's correct ! ")
    score += 1
else:
    print ("That's not right buddy.. sorry !")

ans4 = input("what's does RAM stand for ? ").lower()
if ans4 == "random access memory":
    print("Bingo ! That's correct ! ")
    score += 1
else:
    print ("That's not right buddy.. sorry !")


print("You answered " + str(score) + " questions correctly ! \n" + "You scored " + str((score/4) * 100) + "%") if score > 0 else print("Sorry mate ! You need to study more : )")
