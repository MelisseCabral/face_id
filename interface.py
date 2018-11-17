from tkinter import *
import addNewFace as newFace

class Application:

   def __init__(self, application):

       def recognizer():
           execfile("recognizer.py")

       def trainning():
           execfile("trainning.py")

       def addFace():
           newFace.getImages('mel')

       application.title("Face ID")
       application['bg'] = 'white'

       self.fontePadrao = ("Arial", "10")
       self.container = Frame(application)
       self.container["pady"] = 10
       self.container["padx"] = 15
       self.container["bg"] = 'white'
       self.container.pack()

       self.recognizer = Button(self.container)
       self.recognizer["text"] = "Recognizer"
       self.recognizer["font"] = ("Calibri", "10")
       self.recognizer["width"] = 30
       self.recognizer["pady"] = 5
       self.recognizer["bg"] = '#0984e3'
       self.recognizer["command"] = recognizer
       self.recognizer.pack()

       self.trainning = Button(self.container)
       self.trainning["text"] = "Trainning"
       self.trainning["font"] = ("Calibri", "10")
       self.trainning["width"] = 30
       self.trainning["pady"] = 5
       self.trainning["bg"] = '#0984e3'
       self.trainning["command"] = trainning
       self.trainning.pack()

       self.container6 = Frame(application)
       self.container6["padx"] = 20
       self.container6["pady"] = 5
       self.container6["bg"] = 'white'
       self.container6.pack()

       self.txtusuario = Entry(self.container6)
       self.txtusuario["width"] = 17
       self.txtusuario["font"] = ("Calibri", "10")
       self.txtusuario.pack(side=LEFT)

       self.addNew = Button(self.container6)
       self.addNew["text"] = "Add New"
       self.addNew["font"] = ("Calibri", "10")
       self.addNew["width"] = 13
       self.addNew["pady"] = 5
       self.addNew["padx"] = 5
       self.addNew["bg"] = '#0984e3'
       self.addNew["command"] = addFace
       self.addNew.pack(side=LEFT,  padx=5)

       self.sair = Button(self.container)
       self.sair["text"] = "Close"
       self.sair["font"] = ("Calibri", "10")
       self.sair["width"] = 30
       self.sair["pady"] = 5
       self.sair["bg"] = '#0984e3'
       self.sair["command"] = self.container.quit
       self.sair.pack()

root = Tk()
Application(root)
root.mainloop()