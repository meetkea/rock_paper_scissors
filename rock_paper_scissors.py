import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

computer_input = random.randint(0, 2)

if user_input == 0 and computer_input == 0:
  print("You chose: \n"+ rock + "\nComputer chose: " + rock + "\n It's a draw!")

elif user_input == 0 and computer_input == 1:
  print("You chose: \n" + rock + "\nComputer chose: " + paper + "\nComputer Wins!")

elif user_input == 0 and computer_input == 2:
    print("You chose: \n" + rock + "\nComputer chose: " + scissors + "\nYou Win!")

elif user_input == 1 and computer_input == 0:
    print("You chose: \n" + paper + "\nComputer chose: " + rock + "\nYou Win!")

elif user_input == 1 and computer_input == 1:
    print("You chose: \n" + paper + "\nComputer chose: " + paper + "\nIt's a Draw!")

elif user_input == 1 and computer_input == 2:
    print("You chose: \n" + paper + "\nComputer chose: " + scissors + "\nComputer Wins!")

elif user_input == 2 and computer_input == 0:
    print("You chose: \n" + scissors + "\nComputer chose: " + rock + "\nComputer Wins!")

elif user_input == 2 and computer_input == 1:
    print("You chose: \n" + scissors + "\nComputer chose: " + paper + "\nYou Win!")

elif user_input == 2 and computer_input == 2:
    print("You chose: \n" + scissors + "\nComputer chose: " + scissors + "\nIt's a Draw!")

else:
  print("Choose the right number!")
