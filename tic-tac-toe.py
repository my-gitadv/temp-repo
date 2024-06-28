def printboard(board):  # Print current board (Returns nothing)
  # ???
  #  - - -
  #  - - -
  #  - - -
  print (board[0],board[1],board[2])
  print (board[3],board[4],board[5])
  print (board[6],board[7],board[8])
  
  return 


def posIsValid(pos, board):  # Returns True if the position is valid
  # ???
  if board[pos-1] == '-' :
    return (True)
  else:
    return (False)


def updateboard(board, pos, player):  # Update current board (Returns nothing)
  board[pos-1] = player

  return


def checkWin(board):  # Returns True if the game ends
  if board[0] == board[1] == board[2] and board[0] != '-':
    return True  # First case example
  if board[3] == board[4] == board[5] and board[3] != '-':
    return True
  if board[6] == board[7] == board[8] and board[6] != '-':
    return True
  if board[0] == board[6] == board[3] and board[0] != '-':
    return True  
  if board[1] == board[4] == board[7] and board[1] != '-':
    return True
  if board[2] == board[5] == board[8] and board[5] != '-':
    return True
  if board[0] == board[4] == board[8] and board[0] != '-':
    return True
  if board[2] == board[6] == board[4] and board[2] != '-':
    return True
  return False 


def start():

  print(' 1 2 3\n 4 5 6\n 7 8 9\n')
  board = ['-', '-', '-', '-', '-', '-', '-', '-','-']  # Nine empty postitions on the board
  player = 'X'
  printboard(board)
  turn = 1

  while True:  # This loop is for proceeding the game
    if turn%2 == 0 :
       player = 'O'
    else :
       player = 'X'
    while True:  # This loop is for input
      print('Turn %d' % turn)
      pos = int(input('Player %s Enter Position 1-9: ' % player))

      if posIsValid(pos, board):
      
        updateboard(board, pos, player)
        printboard(board)
        # print(turn)
        
        break

      print('Sorry this position is already marked.\n')

    if checkWin(board):
      # What happened
      print(player,'Win')
      break
      

    # Then proceeds to next turn but what we need to do first?
    turn += 1


start()
