import random
print("Tic, Tac, Toe")
Player = input(" What will you pick: Rock, Paper, Scissors(1,2,3) ")
Computer = random.randint(0,4)
if Computer == 1 and Player == 1:
  print("Computer picked Rock, and you picked rock. It's a tie!")
  Player = input("What will you pick: Rock, Paper, Scissors(1,2,3)")
if Computer == 1 and Player == 2:
  print("Computer picked Rock, and you picked Paper. It's a win for you!")
  Player = input("What will you pick: Rock, Paper, Scissors(1,2,3)")
if Computer == 1 and Player == 3:
  print("Computer picked Rock, and you picked Scissors. It's a win for computer!")
  Player = input("What will you pick: Rock, Paper, Scissors(1,2,3)")
if Computer == 2 and Player == 1:
  print("Computer picked Paper, and you picked Rock. It's a win for computer!")
  Player = input("What will you pick: Rock, Paper, Scissors(1,2,3)")
if Computer == 2 and Player == 2:
  print("Computer picked Paper, and you picked Paper. It's a Tie")
  Player = input("What will you pick: Rock, Paper, Scissors(1,2,3)")
if Computer == 2 and Player == 3:
  print("Computer picked Paper, and you picked Scissors. It's a win for you")
  Player = input("What will you pick: Rock, Paper, Scissors(1,2,3)")
if Computer == 3 and Player == 1:
  print("Computer picked Scissors, and you picked rock. It's a win for you")
  Player = input("What will you pick: Rock, Paper, Scissors(1,2,3)")
if Computer == 3 and Player == 2:
  print("Computer picked Scissors, and you picked Paper. It's a loss for you!")
  Player = input("What will you pick: Rock, Paper, Scissors(1,2,3)")
if Computer == 3 and Player == 3:
  print("Computer picked Scissors, and you picked Scissors. It's a tie")
  Player = input("What will you pick: Rock, Paper, Scissors(1,2,3)")
  
    
    
  
