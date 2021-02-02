
import tkinter as tk 
from random import randint
import array

class Die:

  def __init__(self):
    self.number = randint(1,6)

dice = array.array('i',[0,0,0,0,0])

root = tk.Tk()
root.title("Roll the dice")

dice_frame = tk.Frame(
                      root,
                      width = 700, 
                      height = 200,
                      bg = "orange"
)
dice_frame.pack()

def createDice():
  for i in range(1):
    for j in range(5):
      global dice
      die = Die()

      dice[j] = die.number

      button = tk.Button(
                        master=dice_frame,
                        text=str(die.number),
                        bg = "#ffc353",
                        fg = "#ff6d53",
                        font = ("ms serif",35,"bold"),
                        padx=60,
                        pady=60
      )
      button.grid(row=i,column=j)
    combination_calculation()

  def combination_calculation():
      global dice
      combinations_dictionary = {}

      # set up dictionary
      for i in range(len(dice)+1):
          combinations_dictionary.update({str(i+1):0})

      for i in range(len(dice)):
          current = dice[i]
          #   update occurrance for that one key
          combinations_dictionary[str(current)] = combinations_dictionary[str(current)] + 1

      for key,value in combinations_dictionary.items():
          print(key,value)
      maxKey = max(combinations_dictionary, key=combinations_dictionary.get)
      maxValue = combinations_dictionary[maxKey]
      combination_label.config(text="There was {0} occurrences of {1}".format(maxValue,maxKey))


roll_button = tk.Button(
                      root,
                      text = "Roll the Dice",
                      font = ("ms serif",35,"bold"),
                      fg = "green",
                      width=20,
                      height=3,
                      command=createDice
)
roll_button.pack()

root.mainloop()
