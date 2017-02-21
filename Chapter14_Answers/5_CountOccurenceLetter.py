'''Program to count the occurrence of each letter'''
from tkinter import * 
import tkinter.messagebox 
from tkinter.filedialog import askopenfilename

def countLetters(line, counts): 
    for ch in line:
        if ch.isalpha():
            counts[ord(ch) - ord('a')] += 1

def analyzeFile(filename):
    try:
        readfile = open(filename, "r") 
    
        counts = 26 * [0]
        for line in readfile:
            countLetters(line.lower(), counts)

        for i in range(len(counts)):
            if counts[i] != 0:
                text.insert(END, chr(ord('a') + i) + " appears  " + str(counts[i])
                  + (" time" if counts[i] == 1 else " times") + "\n")
    
        readfile.close()
    except IOError:
        tkinter.messagebox.showwarning("Analyze File error", "File " + filename + " does not exist")  

def showResult():
    analyzeFile(filename.get())
    
            
def openFile(): 
    filenameforReading = askopenfilename()
    filename.set(filenameforReading)
 
        
window = Tk() 
window.title("Count occurrence of Letters") 

frame1 = Frame(window) 
frame1.pack()

scrollbar = Scrollbar(frame1)
scrollbar.pack(side = RIGHT, fill = Y)
text = Text(frame1, width = 40, height = 10, wrap = WORD, 
            yscrollcommand = scrollbar.set)
text.pack()
scrollbar.config(command = text.yview)

frame2 = Frame(window)
frame2.pack()

Label(frame2, text = "Enter a filename: ").pack(side = LEFT)
filename = StringVar()
Entry(frame2, width = 20, textvariable = filename).pack(side = LEFT)
Button(frame2, text = "Browse", command = openFile).pack(side = LEFT)
Button(frame2, text = "Show Result", command = showResult).pack(side = LEFT)

window.mainloop() 