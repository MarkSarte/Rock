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
game_images = [rock, paper, scissors]
#Asking the user for their input on the game
player = input('What do you choose? Type "Rock", "Paper", or "Scissors"\n')
if player.lower() == "rock":
    player = 0
elif player.lower() == "paper":
    player = 1
elif player.lower() == "scissors":
    player = 2
else:
    player = 3
if  (0 <= player <= 2):
  print(game_images[player]) 
  #Assigning the computer a random input versus the player
  computer = random.randint(0, 2)
  #Printing the computers input
  print(f"Computer chose: {game_images[computer]}")
  #Scoring system player versus computer
  if game_images[player] == game_images[computer]:
    print("Draw.")
  elif (game_images[player] == rock and game_images[computer] == scissors) or (
       game_images[player] == scissors
        and game_images[computer] == paper) or (game_images[player] == paper
                                            and game_images[computer] == rock):
    print("You win!")
  else:
    print("You lose.")
else:
  print("You chose a wrong option. Try again.\n")