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
import random as r
list=[rock,paper,scissors]
n=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

print(list[n])


print("Computer chose :")
c=r.randint(0,2)
print(c)
print(list[c])


if n==c:
  print("Draw. . .")
elif n==0 and c==2:
  print("Player won!")
elif n==2 and c==0:
  print("Computer won!")
elif n>c:
  print("Player won!")
elif n<c:
  print("Computer won!")
elif n>=3 or n<0:
  print("Invalid input!!!")

