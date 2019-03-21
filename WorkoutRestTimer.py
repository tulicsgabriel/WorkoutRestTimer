# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 19:59:53 2018

@author: Dzsezusz
"""

from tkinter import Tk, Label, Button, Entry, StringVar
import os, random
import winsound
import time

class MyGUI:
    
    def __init__(self, master):
        self.master = master
        master.title("Gym Timer")
        self.master.geometry("300x200+30+30") 
        #self.master.configure(background = "light blue")

        self.label = Label(master, text="Rest Time App", font=("Helvetica 20 bold"), justify = 'center', pady = 5)
        self.label.pack()
        
        self.textbox_input = StringVar()
        
        self.greet_button = Button(master, text="Set Rest Time (sec)", font=("Helvetica", 12), justify = 'center', pady = 5, command=self.Timer)
        self.greet_button.pack() 
        
        self.textbox = Entry(master, textvariable = self.textbox_input, font=("Helvetica", 12), justify = 'center')
        self.textbox.pack()
        
        self.label2 = Label(master, text="00:00", font=("Helvetica", 16), justify = 'center', fg="red", bg='black', pady = 5)
        self.label2.pack()
        
        self.number_of_sets_left = 5
        
        self.label3 = Label(master, text="Number of sets left: " + str(self.number_of_sets_left), font=("Helvetica", 12), justify = 'center', fg="red", bg='yellow', pady = 5)
        self.label3.pack()
             
    def Timer(self):
        uin = self.textbox_input.get()   # this will be the input from the user
        when_to_stop = abs(int(uin))  
        while when_to_stop > 0:
                m, s = divmod(when_to_stop, 60)
                time_left = str(m).zfill(2) + ":" + str(s).zfill(2)
                self.label2.configure(text = time_left + "\r")
                self.label2.update_idletasks()
                time.sleep(1)            
                when_to_stop -=1 
        self.label2.configure(text = "00:00")
        
        self.UpdateSetNumber()
        self.PlaySound()
                
    def PlaySound(self):
        path = os.path.dirname(__file__)
        pathOfSounds =os.path.join(path, 'sounds')
        filename = random.choice(os.listdir(pathOfSounds)) #chooses random file from path
        PathOfFile = pathOfSounds + "\\" + filename  # gets path of file
        winsound.PlaySound(PathOfFile, winsound.SND_FILENAME) # plays file
        
    def UpdateSetNumber(self):
        self.number_of_sets_left = self.number_of_sets_left  - 1
        if self.number_of_sets_left < 1:
            self.number_of_sets_left = 5
        
        self.label3.configure(text = "Number of sets left: " + str(self.number_of_sets_left))
        self.label3.update_idletasks() 
        

root = Tk()
my_gui = MyGUI(root)
root.mainloop()