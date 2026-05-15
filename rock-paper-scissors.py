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
computer = [f"{rock}", f"{paper}", f"{scissors}"]
user = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

if user == "0":
    useresult = rock
    print(rock)
    compresult = computer[random.randint(0, 2)]
    print(f"{compresult}")
    if useresult == compresult:
        print("Draw")
    if useresult >= compresult:
        print("you won")
    if useresult <= compresult:
        print("you lost")
elif user == "1":
    useresult = paper
    print(paper)
    compresult = computer[random.randint(0, 2)]
    print(f"{compresult}")
    if useresult == compresult:
        print("Draw")
    if useresult >= compresult:
        print("you won")
    if useresult <= compresult:
        print("you lost")
elif user == "2":
    useresult = scissors
    print(scissors)
    compresult = computer[random.randint(0, 2)]
    print(f"{compresult}")
    if useresult == compresult:
        print("Draw")
    if useresult >= compresult:
        print("you won")
    if useresult <= compresult:
        print("you lost")
else:
    print("you typed in a wrong input!")