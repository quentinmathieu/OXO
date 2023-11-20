import os

# fun to clear the screen (for continuous style play)
clear = lambda: os.system('cls')


#  the game still loop until the user press ctrl+c
while True:

  # display the game with actual state
  def displayGame(game):
    
    print("╔═══╦═══╦═══╗")
    for i in range(9):
          if i % 3 == 0 and i != 0:
              print("║\n╠═══╬═══╬═══╣")
          print(f"║ {game[i]} ", end="")
    print("║\n╚═══╩═══╩═══╝")
      

  # show each case reference
  def displayHelp():
    print("AIDE :")
    print("╔═══╦═══╦═══╗")
    for i in range(9):
          if i % 3 == 0 and i != 0:
              print("║\n╠═══╬═══╬═══╣")
          print(f"║ {i+1} ", end="")
    print("║\n╚═══╩═══╩═══╝")


  # display who's turn
  def displayTitle(symbol):
    print(f'\n\n\n╔═══════════╗\n║  MORPION  ║\n║  {symbol} TURN   ║\n╚═══════════╝\n')


  # check if the game is over
  def win(game, symbol):
    if (game[0] == symbol and game[1] == symbol and game[2] == symbol) or \
      (game[3] == symbol and game[4] == symbol and game[5] == symbol) or \
      (game[6] == symbol and game[7] == symbol and game[8] == symbol) or \
      (game[0] == symbol and game[3] == symbol and game[6] == symbol) or \
      (game[1] == symbol and game[4] == symbol and game[7] == symbol) or \
      (game[2] == symbol and game[5] == symbol and game[8] == symbol) or \
      (game[0] == symbol and game[4] == symbol and game[8] == symbol) or \
      (game[2] == symbol and game[4] == symbol and game[6] == symbol):
      print(f'\n\n\n╔═══════════╗\n║  MORPION  ║\n║  {symbol} GAGNE! ║\n╚═══════════╝\n')
      return True
    elif count == 9:
      print(f'\n\n\n╔═══════════╗\n║  MORPION  ║\n║  EGALITE! ║\n╚═══════════╝\n')
      return True
    return False
  


  # init a new game
  clear()
  game=[" "," "," "," "," "," "," "," "," "]
  message ="Choisissez une case:\n"
  displayTitle("X")
  displayGame(game)

  count=0

  #  loop until the game is over
  while count!= 9:
    user = input(message)
    clear()
    # check if the user input is valid, else retry and display help
    try :
      user = int(user)
      if (game[user-1] == " "):
        game[user-1] =  "X" if count%2== 0 else "O"
        count+=1
        if win(game, game[user-1]):
          break
        displayTitle("X" if count%2== 0 else "O")
        message ="Choisissez une case:\n"
      else:
        displayHelp()

        message ="Choisissez une case valide:\n"
    except:
        displayHelp()
        message ="Choisissez une case valide:\n"
    displayGame(game)

  input("Appuyez sur entrer pour recommencer!")