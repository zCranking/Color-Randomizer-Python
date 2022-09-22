from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import random

root = Tk()
root.title("Color Randomizer")
root.geometry("800x600")
root.config(bg="#CDFFF9")

randomColor = Label(root, fg="#77A5BB", bg="#CDFFF9",font=("Comic Sans MS", "34", "bold"))
randomColor.place(relx=0.5, rely=0.5, anchor=CENTER)

class Game():
    def __init__(self):
        self.__score = 0
    
    def UpdateGame(self):
        self.text = ["Red", "Orange", "Green", "Blue", "Purple"]
        self.randomTxt = random.randint(1, 5)
        self.color = ["Red", "Orange", "Green", "Blue", "Purple"]
        self.randomNumColor = random.randint(1, 5)
        randomColor['text'] = self.text[self.randomTxt]
        randomColor['fg'] = self.color[self.randomNumColor]
        
Game = Game()        

Button = Button(root, bg="#CDFFF9", text="Button", width=10, height=1, font=("Comic Sans MS", "24", "bold"), command=Game.UpdateGame)
Button.place(relx=0.5, rely=0.2, anchor=CENTER)
         
root.mainloop()