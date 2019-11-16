# from tk import Stringvar
from tkinter import *

from PIL import Image, ImageTk, ImageDraw, ImageFilter
class Window(Frame) :

    def __init__(self, master = None) :
        Frame.__init__(self, master)

        self.master = master

        self.init_window()
    def init_window(self):

        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)

        # quitButton = Button(self, text="Quit", command=self.client_exit);
        # quitButton.place(x=0, y=0)

        menu = Menu(self.master)
        self.master.config(menu = menu)

        file = Menu(menu)
        file.add_command(label = 'Exit', command=self.client_exit)
        menu.add_cascade(label='File', menu=file)

        edit = Menu(menu)
        edit.add_command(label = 'Show Image', command=self.showBoard())
        edit.add_command(label='Show Text', command=self.showTxt)
        menu.add_cascade(label='Edit', menu=edit)
        # self.variable = tkinter.Stringvar()


    def client_exit(self) :
        exit()

    def showImg(self) :
        load = Image.open("IMG_1240.JPG")
        load.putalpha(128)
        newsize = (100, 40)
        load = load.resize(newsize)
        render = ImageTk.PhotoImage(load)
        # img.putalpha(100)

        img = Label(self, image=render)
        img.image = render
        img.place(x=0,y=0)

    def showBoard(self) :
        load = Image.open("Board.jpg")
        newsize = (1000, 600)
        load = load.resize(newsize)
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=100, y = 200)

    def showTxt(self) :
        text = Label(self, text='Hey there')
        text.pack()

OptionsPlayer1 = [
    "Select one",
    "Place",
    "Observe"

]
OptionsSpace1 = [
    "Select a place",
    "(1,1)",
    "(1,2)",
    "(1,3)",
    "(2,1)",
    "(2,2)",
    "(2,3)",
    "(3,1)",
    "(3,2)",
    "(3,3)"
]
root = Tk()
# master = Tk()
variable = StringVar(root)
variable.set(OptionsPlayer1[0])
player1Option = OptionMenu(root, variable, *OptionsPlayer1)
player1Option.pack(side=LEFT)
variable2 = StringVar(root)
variable2.set(OptionsSpace1[0])
player1Place = OptionMenu(root, variable2, *OptionsSpace1)
player1Place.pack(side=LEFT)

variable3 = StringVar(root)
variable3.set(OptionsPlayer1[0])
player2Option = OptionMenu(root, variable3, *OptionsPlayer1)
player2Option.pack(side=RIGHT)

variable4 = StringVar(root)
variable4.set(OptionsSpace1[0])
player2Place = OptionMenu(root, variable4, *OptionsSpace1)
player2Place.pack(side=RIGHT)

# player1Option.pack(pady = 0)
root.geometry("3000x900")

app = Window(root)


root.mainloop()
