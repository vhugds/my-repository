





from tkinter import *

import random


def restart():

  global player

  #updates the player order and text bar

  player = random.choice(characters)

  label.config(text=player+ " 's turn")


  #updates button text to blank spaces

  for row in range(3):

    for column in range(3):

      buttons[row][column].config(text="")



def next_turn(row, column):

  global player

  if buttons[row][column]['text'] == "" and check_winner() is False:

    if player == characters[0]:

      buttons[row][column]['text'] = player


  if check_winner() is False:

    player = characters[1]

    label.config(text=(characters[1] +" turn"))


  elif check_winner() is True:

    label.config(text=(characters[0] +" won"))


  elif check_winner() == "Tie":

    label.config(text=("Tie"))


  else:

    buttons[row][column]['text'] = player

    if check_winner() is False:

      player = characters[0]

      label.config(text=(characters[0] +" turn"))


    elif check_winner() is True:

      label.config(text=(characters[1] +" won"))

    elif check_winner() == "Tie":

      label.config(text=("Tie"))



def check_winner():

  for row in range(3):

    if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != '':

      return True

  for column in range(3):

    #if all the buttons in a row have matching text that is not equal to a blank space

    if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != '':

      return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":

      return True

    if buttons[2][0]['text'] == buttons[1][1]['text'] == buttons[0][2]['text'] != "":

      return True

    #then we check for ties

    if empty_spaces() is False:

      return "Tie"

    else:

      return False
  


def empty_spaces():

  spaces = 9

  for row in range(3):

    for column in range(3):

      if buttons[row][column]['text']!='':

        spaces-=1

        if spaces == 0:

         return False

        else:

          return True


board = Tk()

board.title("Tic-Tac-Toe")

characters = ["x","o"]


player = random.choice(characters)

buttons = [['','',''],
           ['','',''],
           ['','','']]

label = Label(text=player+ "'s turn", font=("futura",40))

label.pack(side="top")


new_game_button = Button(text="New Game", font=("futura",20), command=restart)

new_game_button.pack(side="top")


frame = Frame(board)

frame.pack()


for row in range(3):

  for column in range(3):

    buttons[row][column] = Button(frame, text ="",font=('consolas',40), width=5, height=2, command=lambda row=row, column=column:next_turn(row,column)  )

    buttons[row][column].grid(row=row,column=column)


board.mainloop()