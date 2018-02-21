print ("Player 1 is X")
board = ["   |   |  ", "-----------","   |   |  ", "-----------","   |   |  " ]
i = 0
def board_reset():
    global board
    board = ["   |   |  ", "-----------","   |   |  ", "-----------","   |   |  " ]
def winning_conditions_x():
    if list(board[0])[1] == "X" and list(board[2])[1] == "X" and list(board[4])[1] == "X":
        return True
    elif list(board[0])[5] == "X" and list(board[2])[5] == "X" and list(board[4])[5] == "X":
        return True
    elif list(board[0])[9] == "X" and list(board[2])[9] == "X" and list(board[4])[9] == "X":
        return True
    elif list(board[0])[1] == "X" and list(board[0])[5] == "X" and list(board[0])[9] == "X":
        return True
    elif list(board[2])[1] == "X" and list(board[2])[5] == "X" and list(board[2])[9] == "X":
        return True
    elif list(board[4])[1] == "X" and list(board[4])[5] == "X" and list(board[4])[9] == "X":
        return True
    elif list(board[0])[1] == "X" and list(board[2])[5] == "X" and list(board[4])[9] == "X":
        return True
    elif list(board[4])[1] == "X" and list(board[2])[5] == "X" and list(board[0])[9] == "X":
        return True
    else:
        return False
def winning_conditions_o():
    if list(board[0])[1] == "O" and list(board[2])[1] == "O" and list(board[4])[1] == "O":
        return True
    elif list(board[0])[5] == "O" and list(board[2])[5] == "O" and list(board[4])[5] == "O":
        return True
    elif list(board[0])[9] == "O" and list(board[2])[9] == "O" and list(board[4])[9] == "O":
        return True
    elif list(board[0])[1] == "O" and list(board[0])[5] == "O" and list(board[0])[9] == "O":
        return True
    elif list(board[2])[1] == "O" and list(board[2])[5] == "O" and list(board[2])[9] == "O":
        return True
    elif list(board[4])[1] == "O" and list(board[4])[5] == "O" and list(board[4])[9] == "O":
        return True
    elif list(board[0])[1] == "O" and list(board[2])[5] == "O" and list(board[4])[9] == "O":
        return True
    elif list(board[4])[1] == "O" and list(board[2])[5] == "O" and list(board[0])[9] == "O":
        return True
    else:
        return False
def print_board():
    res = ""
    for row in board:
        print (" ".join(row))
def p1turn(turn):
    if turn%2 == 0:
        return True
    elif turn%2 == 1:
        return False
def change_x(row,col):
  if col == 1:
    if row == 1:
        lst = list(board[0])
        lst[1] = "X"
        lst
        new = ""
        for i in lst:
            new += i
        board[0] = new
    elif row == 2:
        lst = list(board[2])
        lst[1] = "X"
        lst
        new = ""
        for i in lst:
            new += i
        board[2] = new
    elif row == 3:
        lst = list(board[4])
        lst[1] = "X"
        lst
        new = ""
        for i in lst:
            new += i
        board[4] = new
  elif col == 2:
    if row == 1:
        lst = list(board[0])
        lst[5] = "X"
        lst
        new = ""
        for i in lst:
            new += i
        board[0] = new
    elif row == 2:
        lst = list(board[2])
        lst[5] = "X"
        lst
        new = ""
        for i in lst:
            new += i
        board[2] = new
    elif row == 3:
        lst = list(board[4])
        lst[5] = "X"
        lst
        new = ""
        for i in lst:
            new += i
        board[4] = new
  elif col == 3:
    if row == 1:
        lst = list(board[0])
        lst[9] = "X"
        lst
        new = ""
        for i in lst:
            new += i
        board[0] = new
    elif row == 2:
        lst = list(board[2])
        lst[9] = "X"
        lst
        new = ""
        for i in lst:
            new += i
        board[2] = new
    elif row == 3:
        lst = list(board[4])
        lst[9] = "X"
        lst
        new = ""
        for i in lst:
            new += i
        board[4] = new
def change_o(row,col):
  if col == 1:
    if row == 1:
        lst = list(board[0])
        lst[1] = "O"
        lst
        new = ""
        for i in lst:
            new += i
        board[0] = new
    elif row == 2:
        lst = list(board[2])
        lst[1] = "O"
        lst
        new = ""
        for i in lst:
            new += i
        board[2] = new
    elif row == 3:
        lst = list(board[4])
        lst[1] = "O"
        lst
        new = ""
        for i in lst:
            new += i
        board[4] = new
  elif col == 2:
    if row == 1:
        lst = list(board[0])
        lst[5] = "O"
        lst
        new = ""
        for i in lst:
            new += i
        board[0] = new
    elif row == 2:
        lst = list(board[2])
        lst[5] = "O"
        lst
        new = ""
        for i in lst:
            new += i
        board[2] = new
    elif row == 3:
          lst = list(board[4])
          lst[5] = "O"
          lst
          new = ""
          for i in lst:
            new += i
          board[4] = new
  elif col == 3:
    if row == 1:
        lst = list(board[0])
        lst[9] = "O"
        lst
        new = ""
        for i in lst:
            new += i
        board[0] = new
    elif row == 2:
        lst = list(board[2])
        lst[9] = "O"
        lst
        new = ""
        for i in lst:
            new += i
        board[2] = new
    elif row == 3:
        lst = list(board[4])
        lst[9] = "O"
        lst
        new = ""
        for i in lst:
            new += i
        board[4] = new
def round(turn, row, col):
    if p1turn(turn) == True:
        change_x(row,col)
        print_board()
    else:
        change_o(row,col)
        print_board()
def already_chosen(row, col):
  selected = list(board[2*(row-1)])[(4*col)-3]
  if selected == "X" or selected == "O":
      return True
  else:
      return False
while i in range(10):
  print ("Player {}'s turn!".format((i%2)+1))
  if winning_conditions_x() == True:
          print ("X wins!!!")
          y_n = (input("Play Again? Y/N: ")).lower()
          if y_n == "y":
              board_reset()
              i = 0
          else:
            break
  elif winning_conditions_o() == True:
          print ("O wins!!!")
          y_n = (input("Play Again? Y/N: ")).lower()
          if y_n == "y":
              board_reset()
              i = 0
          else:
              break
  elif i == 9:
    print ("Draw :(")
    y_n = (input("Play Again? Y/N: ")).lower()
    if y_n == "y":
        board_reset()
        i = 0
    else:
        break
  else:
      row = int(input("Row: "))
      col = int(input("Col: "))
      if row < 0 or col < 0 or row > 3 or col > 3:
          print ("That is not a valid selection")
      elif already_chosen(row,col) == False:
        round(i,row,col)
        i += 1
      else:
        print ("Already Chosen")
