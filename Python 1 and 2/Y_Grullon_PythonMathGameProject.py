#To pick random numbers

import random
#To round the numbers
import math
#To clear the screen
import os


#Describing the program to the user
print("    ********************************************")
print("    *                                          *")
print("    *        Welcome to the Math Game!         *")
print("    *                                          *")
print("    ********************************************")

#Telling the reader what the program with do
print("""
This program will provide a small math game to have fun and
to strengthen your mathematical knowledge
""")
start = input("[Click Enter to start]")

#Question Function

def make_multiple_questions(difficulty, Amount_Of_Question):

  right = 0
  wrong = 0
#Making it repeat x amount of times
  for i in range(Amount_Of_Question):
      num1 = 0
      num2 = 0
      num3 = 0
#The type of questions it will generate if the difficulty is 1
      if difficulty == 1:
          #Generating random numbers between 1 and 10
          num1 = random.randint(1, 10)
          num2 = random.randint(1, 10)

          operator = random.choice(['+', '-', '*'])
          print("Round the number to the nearest whole number")
          print("")

          question = int(input(f"What is {num1} {operator} {num2}="))


          #Answering the question
          answer = eval(f"{num1} {operator} {num2}")
          answer = math.ceil(answer)
#Checking if the user answer is correct
          if question == answer:
            print("You got it right!")
            right += 1 
          else:
            print("You got it wrong!")
            print("The answer was", answer)
            wrong +=1
          os.system('sleep 1')
          os.system('clear')



    #The type of questions it will generate if the difficulty is 2
      elif difficulty == 2:
        #Generating random numbers between 10 and 50
          num1 = random.randint(10, 50)
          num2 = random.randint(10, 50)
          num3 = random.randint(10, 50)
          operator = random.choice(['+', '-', '*', '/'])
          operator2 = random.choice(['+', '-', '*', '/'])

          print("Round the number to the nearest whole number")
          print("")
          question = int(input(f"What is {num1} {operator} {num2} {operator2} {num3} ="))
          answer = eval(f"{num1} {operator} {num2} {operator2} {num3}")
          answer = math.ceil(answer)

          if question == answer:
            print("You got it right!")
            right += 1 
          else:
            print("You got it wrong!")
            print("The answer was", answer)
            wrong +=1
          os.system('sleep 1')
          os.system('clear')

    #The type of questions it will generate if the difficulty is 3
      elif difficulty == 3:
        #Generating random numbers between 50 and 100
          num1 = random.randint(50, 100)
          num2 = random.randint(50, 100)
          num3 = random.randint(50, 100)
          num4 = random.randint(50, 100)
          operator = random.choice(['+', '-', '*', '/'])
          operator2 = random.choice(['+', '-', '*', '/'])
          operator3 = random.choice(['+', '-', '*'])
          print("Round the number to the nearest whole number")
          print("")

          question = int(input(f"What is {num1} {operator} {num2} {operator2} {num3} {operator3} {num4} ="))
          answer = eval(f"{num1} {operator} {num2} {operator2} {num3} {operator3} {num4}")
          answer = math.ceil(answer)
          if question == answer:
            print("You got it right!")
            right += 1
          else:
            print("You got it wrong!")
            print("The answer was", answer)
            wrong +=1
          os.system('sleep 1')
          os.system('clear')
#Generating an average amount for the amount of questions they got right
  average = right / Amount_Of_Question * 100
#Rounding the number
  average = math.ceil(average)  
#Displays the amount of questions they got right, wrong, and the average
  print("You have answered", Amount_Of_Question, "questions")
  print("")
  print("You got", right, "right and" ,wrong, "wrong")
  print("")
  print("Your score is", average)
  print("")
  print("")
  print("____________________________")
  print("|                          |")
  print("  Your score is",average)
  print("|__________________________|") 
  return average

def setting():
  #Asking for the amount of questions the user wants to answer
    Amount_Of_Question = int(input("How many questions would you like to answer?:"))
  #Explaining what Dyanamic progression is
    print("Dyanamic Progression is when you get the question right you get harder questions and if you get it wrong you get easier questions.")
  #Asking if the user wants Dyanamic progression or not
    Dyanamic_ProgressionQ = input("Would you like to have Dyanamic progression in your questions? (Y/N):")




#Checing if the user wants Dyanamic progression
    if Dyanamic_ProgressionQ == "Y":
        print("Answer:")
        Dyanamic_Progression(Amount_Of_Question)

    #If the user doesnt pick yes
    elif Dyanamic_ProgressionQ == "N":
        difficulty = input("What difficulty would you like to play at? (Easy, Medium, Hard):")
        #checking if the
        if difficulty == "Easy":
            print("You have chosen Easy difficulty")
            difficulty = 1
        elif difficulty == "Medium":
            print("You have chosen Medium difficulty")
            difficulty = 2
        elif difficulty == "Hard":
            print("You have chosen Hard difficulty")
            difficulty = 3
        make_multiple_questions(difficulty, Amount_Of_Question)

def leader_board(names, average, difficulty):
  player = "|Player Name| "
  scores = "|Average Score| "
  the_dif = "|The Difficulty| "
  print("Leaader Board: ")
  with open('leaderboard.txt', 'a') as text_file:
      text_file.write(f"{player}    {scores}    {the_dif}\n")
      text_file.write("")
      text_file.write(f"|{names}|              |{average}|                |{difficulty}|\n")
      text_file.write("________________________________________________________\n")
      text_file.close()
  with open('leaderboard.txt', 'r') as text_file:
      print("")
      print(text_file.read())

average = 0
difficulty = 0
def Dyanamic_Progression(Amount_Of_Question):
  global average
  global difficulty
  right = 0
  wrong = 0
  difficulty = 1  
  for i in range(Amount_Of_Question):
      num1 = 0
      num2 = 0
      num3 = 0

      if difficulty == 1:
          num1 = random.randint(1, 10)
          num2 = random.randint(1, 10)

          operator = random.choice(['+', '-', '*'])
          print("Round the number to the nearest whole number")
          print("")
          question = int(input(f"What is {num1} {operator} {num2}="))


          answer = eval(f"{num1} {operator} {num2}")
          answer = math.ceil(answer)

          if question == answer:
            print("You got it right!")
            right += 1
            difficulty += 1
          else:
            print("You got it wrong!")
            print("The answer was", answer)
            wrong +=1
            difficulty = 1
          os.system('sleep 1')
          os.system('clear')




      elif difficulty == 2:
          num1 = random.randint(1, 50)
          num2 = random.randint(1, 50)
          num3 = random.randint(1, 50)
          operator = random.choice(['+', '-', '*', '/'])
          operator2 = random.choice(['+', '-', '*', '/'])
          print("Round the number to the nearest whole number")
          print("")
          question = int(input(f"What is {num1} {operator} {num2} {operator2} {num3} ="))


          answer = eval(f"{num1} {operator} {num2} {operator2} {num3}")
          answer = math.ceil(answer)

          if question == answer:
            print("You got it right!")
            right += 1
            difficulty += 1
          else:
            print("You got it wrong!")
            print("The answer was", answer)
            wrong +=1
            difficulty -= 1
          os.system('sleep 1')
          os.system('clear')


      elif difficulty == 3:
          num1 = random.randint(1, 100)
          num2 = random.randint(1, 100)
          num3 = random.randint(1, 100)
          num4 = random.randint(1, 100)
          operator = random.choice(['+', '-', '*', '/'])
          operator2 = random.choice(['+', '-', '*', '/'])
          operator3 = random.choice(['+', '-', '*'])
          print("Round the number to the nearest whole number")
          print("")
          question = int(input(f"What is {num1} {operator} {num2} {operator2} {num3} {operator3} {num4} ="))

          answer = eval(f"{num1} {operator} {num2} {operator2} {num3} {operator3} {num4}")
          answer = math.ceil(answer)
          if question == answer:
            print("You got it right!")
            right += 1
            difficulty += 1
          else:
            print("You got it wrong!")
            print("The answer was", answer)
            wrong +=1
            difficulty -= 1
          os.system('sleep 1')
          os.system('clear')
  average = right / Amount_Of_Question * 100
  average = math.ceil(average)  
  print("You have answered", Amount_Of_Question, "questions")
  print("")
  print("You got", right, "right and" ,wrong, "wrong")
  print("")
  print("Your score is", average)
  print("")
  print("")
  print(" _________________________")
  print(" |                       |")
  print("  Your score is",average)
  print(" |_______________________|") 

  return average


#Ask the user if they would like to enter the setting

Enter_Setting = input("Would you like to enter the setting? (yes/no)\n[Typing no will cause the program to randomize the setting for you]")

if Enter_Setting == "yes":
  setting()
elif Enter_Setting == "no":
  random_diff = random.randint(0,2)+1
  random_amount = random.randint(1,20)-1
  print("_____________________________________________________________")
  print("")
  print("These are the settings that was chosen for you")
  print("")
  print("Difficulty:",random_diff)
  print("")
  print("Amount of questions:",random_amount)
  print("")
  print("_____________________________________________________________")
  make_multiple_questions(random_diff, random_amount)


#Ask the user if they would like to enter the leaderboard

led = input("Would you like to enter the leaderboard?\n(yes/no)")

if led == "yes":
  names = input("What is your name?:")
  leader_board(names, average, difficulty)

elif led == "no":
  print("Thank you for playing!")
  os.system("clear")


