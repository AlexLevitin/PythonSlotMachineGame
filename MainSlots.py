import random
import time
import GUI

budget = 100
GUI.budgetLabel.configure(text = f"Budget is: {budget}")
options = [1,2,3,4,5,6]




#print win/lose message
def printResIncreaseBudget(_bet):
   s1 = GUI.slot1._text
   s2 = GUI.slot2._text
   s3 = GUI.slot3._text
   global budget 
   if(s1 == s2 and s2 == s3):
      GUI.msgLabel.configure(text = f"Great! You Won {_bet*2}$", text_color = "green")
      budget = budget - _bet + _bet*2
      GUI.root.update()
   elif(s1 == s2 or s1 == s3 or s2 == s3):
      GUI.msgLabel.configure(text = f"Nice! You Won {_bet*2.5}$", text_color = "yellow")
      budget = budget - _bet +_bet * 1.5 
      GUI.root.update()
   else:
      GUI.msgLabel.configure(text = f"Too Bad! You lost {_bet}$", text_color = "red")
      budget = budget -_bet
      GUI.root.update()
   GUI.budgetLabel.configure(text = f"Budget is: {budget}")
   GUI.root.update()
   if(budget <= 0 ):
       GUI.msgLabel.configure(text = "Game Over", text_color = "red")
       GUI.root.update()
       time.sleep(2)
       GUI.root.destroy()

      

#set play game function
def playGame():
   betAmount = int(GUI.entry1.get())
   if betAmount == "":
      GUI.msgLabel.configure(text = "You Must Place A Bet To Play!", text_color = "red")
      GUI.root.update()
      return
   elif(betAmount > budget or betAmount <= 0):
      GUI.msgLabel.configure(text = "Invalid Bet", text_color = "red")
      GUI.root.update()
      return
   GUI.slot1.configure(text = "")
   GUI.slot2.configure(text = "")
   GUI.slot3.configure(text = "")

   for i in range(20):                                 #loop for spin
     GUI.slot1.configure(text = f"{spinSingleWheel()}")
     GUI.root.update()
     time.sleep(0.05)
   for i in range(20):    
     GUI.slot2.configure(text = f"{spinSingleWheel()}")
     GUI.root.update()
     time.sleep(0.05)
   for i in range(20):    
     GUI.slot3.configure(text = f"{spinSingleWheel()}")
     GUI.root.update()
     time.sleep(0.05)
   printResIncreaseBudget(betAmount)



 #spin wheel funtion
def spinSingleWheel():
    randomNum = random.randint(0,5)
    return options[randomNum]
GUI.playButton.configure(command = playGame)
GUI.root.mainloop()


