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

score = Label(root, fg="#77A5BB", text="0", bg="#CDFFF9", font=("Comic Sans MS", "20", "bold"))
score.place(relx=0.9, rely=0.05, anchor=CENTER)

inputBox = Entry(root)
inputBox.place(relx=0.5, rely=0.6, anchor=CENTER)

class Game():
    def __init__(self):
        self.__score = 0
    
    def UpdateGame(self):
        self.text = ["Red", "Orange", "Green", "Blue", "Purple"]
        self.randomTxt = random.randint(0, 4)
        self.color = ["Red", "Orange", "Green", "Blue", "Purple"]
        self.randomNumColor = random.randint(0, 4)
        randomColor['text'] = self.text[self.randomTxt]
        randomColor['fg'] = self.color[self.randomNumColor]

    def __UpdateScore(self, inputValue):
        guess = inputBox.get()
        if self.color[self.randomNumColor] == guess:
            print(self.color[self.randomNumColor])
            increment = random.randint(0,10)
            self.__score = self.__score + increment
            score['text'] = "Score: "+ str(self.__score)
            
    def getUserValue(self, inputValue):
        self.__UpdateScore(inputValue)

Game = Game()        

def getInput():
    guess = inputBox.get()
    Game.getUserValue(guess)
    Game.UpdateGame()
    inputBox.delete(0, END)

Play = Button(root, bg="#CDFFF9", text="Play", width=10, height=1, font=("Comic Sans MS", "24", "bold"), command=Game.UpdateGame)
Play.place(relx=0.3, rely=0.35, anchor=CENTER)

Check = Button(root, bg="#CDFFF9", text="Check", width=10, height=1, font=("Comic Sans MS", "24", "bold"), command=getInput)
Check.place(relx=0.7, rely=0.35, anchor=CENTER)
         
root.mainloop()