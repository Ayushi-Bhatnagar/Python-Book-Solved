'''Program to display a pie chart in TKInterface'''
from tkinter import *
import math 
        
class PieChart:
    def drawSlice(self, start, extent, color, title):
        self.canvas.create_arc(self.width / 2 - self.radius, self.height / 2 - self.radius, 
            self.width / 2 + self.radius, self.height / 2 + self.radius, 
            start = start, extent = extent, fill = color)
        x = self.width / 2 + self.radius * math.cos(math.radians(extent / 2 + start))
        y = self.height / 2 - self.radius * math.sin(math.radians(extent / 2 + start))
        self.canvas.create_text(x, y, text = title)
 
    def __init__(self):
        window = Tk()
        window.title("Pie Chart") 
        self.radius = 100
        self.width = 300
        self.height = 300
        
        self.canvas = Canvas(window, bg = "white", width = self.width, height = self.height)
        self.canvas.pack()
        self.drawSlice(0, 360 * 0.2, "red", "Project -- 20%")
        self.drawSlice(360 * 0.2, 360 * 0.1, "blue", "Quizzes -- 10%")
        self.drawSlice(360 * 0.2 + 360 * 0.1, 360 * 0.3, "green", "Midterm -- 30%")
        self.drawSlice(360 * 0.2 + 360 * 0.1 + 360 * 0.3, 360 * 0.4, "orange", "Final -- 40%")
        
        window.mainloop() 

PieChart()