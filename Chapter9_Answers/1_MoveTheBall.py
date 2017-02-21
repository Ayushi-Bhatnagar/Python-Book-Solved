'''Class to make an interface to move the ball left right up and down'''
from tkinter import * 

class MoveBall:
    def __init__(self): 
        frame = Tk() 
        frame.title("Move A Ball") 
        self.canvas = Canvas(frame, bg = "white", width = 200, height = 200) 
        self.canvas.pack() 
        self.canvas.create_oval(80, 60,60, 80, tags = ("oval"), fill="red")

        self.move = 10

            
        btLeft = Button(frame, text = "Left", command = self.moveLeft) 
        btLeft.pack(side = LEFT)
        btRight = Button(frame, text = "Right",command = self.moveRight) 
        btRight.pack(side = LEFT)
        btUp = Button(frame, text = "Up", command = self.moveUp) 
        btUp.pack(side = LEFT)
        btDown= Button(frame, text = "Down",command = self.moveDown)
        btDown.pack(side = LEFT)
        frame.mainloop() 
    
    def moveLeft(self):
        self.canvas.move("oval", -self.move, 0)
        self.canvas.update()
            
        
    def moveRight(self):
        self.canvas.move("oval", self.move, 0)
        self.canvas.update()

    
    def moveUp(self):
        self.canvas.move("oval", 0, -self.move)
        self.canvas.update()

        
    def moveDown(self):
        self.canvas.move("oval", 0, self.move)

        

MoveBall() 