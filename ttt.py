import os
from termcolor import colored

board = [0,1,2,
        3,4,5,
        6,7,8]

def print_board():
  print ("---------")
  print (board[0], "|", board[1], "|", board[2])
  print ("---------")
  print (board[3], "|", board[4], "|", board[5])
  print ("---------")
  print (board[6], "|", board[7], "|", board[8])
  print ("---------")


def checker():
  if (board[0] == board[1] == board[2] or \
      board[3] == board[4] == board[5] or \
      board[6] == board[7] == board[8] or \
      board[0] == board[3] == board[6] or \
      board[1] == board[4] == board[7] or \
      board[2] == board[5] == board[8] or \
      board[0] == board[4] == board[8] or \
      board[2] == board[4] == board[6]):

    return True
  else:
    return False

os.system("clear")
print_board()
print ("Welcome to Tic Tac Toe!")

t = True
counter = 0
player = 1

while (t == True):

  if (counter == 9):
    print ("Its a Tie!")
    break

  print ("Player",player)
  spot = int(input("Select a spot: "))



  if (board[spot] != "X" and board[spot] != "O"):
    if (player == 1):
      board[spot] = colored('X','red')
    else:
      board[spot] = colored('O','green')
    counter = counter + 1
    os.system("clear")
    print_board()

  else:
    print("This spot is taken!")

  result = checker()

  if (result == True):
    print("Congratulations Player", player,", you have won!")
    break;

  else:
    if (player == 1):
      player = 2
    else:
      player = 1
