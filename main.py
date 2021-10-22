print("Welcome to quizlet we will be playing a quiz game you have to ans some questions!")
name = input("Pls let us know your name: ")
print("Hello,",name,"pls read the following rules")
print("1) Pls enter all your answers in small letters only")
print("2) If the answer is not in small letters the answer will be wrong ")
print("3) Pls check the spellings of your answers")
print("4) if the spellings are wrong the answer will also be wrong ")
play = input("have you understood the rules and wish to play? if so then type 'yes' ")

if play != "yes":
    exit("ok, bye until next time :)")
if play == "yes":
    print("great!, now get exited!")

ans1 = input("what is the 4 planet from the sun? ")
if ans1 == "mars":
    print("correct! the 4th planet from the sun is mars after Earth!")
else: print("sorry, your answer is wrong, try again later!"); exit()

print("now the secound question:-")
ans2 = input("what is the fullform of R.A.M in computers? ")
if ans2 == "random access memory":
    print("correct again! the fullform of R.A.M is random access memory")
else: print("sorry, your answer is wrong, try again later!") ; exit()

print("coming up, the third question!")
ans3 = input("which is the biggest country in the world? ")
if ans3 == "russia":
    print("correct again! the biggest country in the world is russia!!")
else: print("sorry, your answer is wrong, try again later!") ; exit()

print("the forth question is:-")
ans4 = input("which continent has the most population? ")
if ans4 == "asia":
    print("correct again! the continent with the most population is asia! ")
else: print("sorry, your answer is wrong, try again later!") ; exit()

print("now! the final question!")
ans5 = input("in which year did world war 2 end? ")
if ans5 == "1945":
    print("correct again! the world war 2 ended in 1945,", name, "you did a great job 5/5!!, pat yourself on the back!! :)" )
else: print("sorry, your answer is wrong, try again later!") ; exit()
