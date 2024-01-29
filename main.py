from tkinter import *
import random

#main function for generate color 

def generate_color():
    EntryColor.delete(0, END)
    color = '#{:02x}{:02x}{:02x}'.format(*map(lambda x: random.randint(0, 255), range(3)))
    LabeColor['bg'] = color
    EntryColor.insert(0,color)

root = Tk() #create a app window
root.title('Color Generate')
root.geometry('400x500') #app window size
root.resizable(0, 0) # app window size not changed 

LabeColor = Label(root, bg='white') #window for colors
LabeColor.place(relx=0.5, rely=0.3, anchor=CENTER, width=250, height=250) #window for color in center of app window

EntryColor = Entry(root, borderwidth=4) # create place for entry inf
EntryColor.place(relx=0.5, rely=0.6, anchor=CENTER, width=100, height=50) #place entry on the screen
generate_color
BtnGenerate = Button(root, text='Generate', font='Montserrat 14 bold', borderwidth=4, command=generate_color)
BtnGenerate.place(relx=0.5, rely=0.8, anchor=CENTER, width=250, height=50)
root.mainloop() #check if applicATION WORKS
