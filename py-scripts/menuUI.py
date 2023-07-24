from tkinter import *
from tkinter import ttk
from menuNewConfig import menuNewConfig
from configListUi import configListUi
from instanceListUi import instanceListUi

def menuUi(filbeatVersion):

    fenetre = Tk()

    w = 470
    h = 480

    ws = fenetre.winfo_screenwidth()
    hs = fenetre.winfo_screenheight()

    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    fenetre.geometry('%dx%d+%d+%d' % (w, h, x, y))

    fenetre.title("FileBeatConfigurator")
    
    hr0 = ttk.Separator(fenetre, orient="vertical").grid(row=0, column=0, padx=10, rowspan=11, columnspan=1, sticky="ws")

    hr1 = ttk.Separator(fenetre, orient="horizontal").grid(pady=6, row=0, column=1, columnspan=2, sticky="ws")

    mainTitle = Label(fenetre, text="Welcome on the FilbeatToCloud project app !",font='bold', pady=10).grid(row=1, column=1, columnspan=1)

    hr2 = ttk.Separator(fenetre, orient="horizontal").grid(pady=30, row=2, column=1, columnspan=2, sticky="ws")

    scndTitle = Label(fenetre, text="Menu",font=('black', 15)).grid(row=3, column=1, columnspan=1)

    hr2bis = ttk.Separator(fenetre, orient="horizontal").grid(pady=20, row=4, column=1, columnspan=2, sticky="ws")

    def newCgonfig():
        fenetre.destroy()
        menuNewConfig(filbeatVersion)
    
    def seeInstances():
        fenetre.destroy()
        instanceListUi()

    def seeConfigs():
        fenetre.destroy()
        configListUi()

    addConf = Button(fenetre, text='Add a new\nFilebeat configuration', command=lambda: newCgonfig(), width=20, font=('black', 13), padx=10).grid(row=5, column=1, columnspan=1)
    hr3 = ttk.Separator(fenetre, orient="horizontal").grid(pady=20, row=6, column=1, columnspan=2, sticky="ws")
    browseInstances = Button(fenetre, text='Browse among existing\nFilebeat instances', command=lambda: seeInstances(), width=20, font=('black', 13), padx=10).grid(row=7, column=1, columnspan=1)
    hr4 = ttk.Separator(fenetre, orient="horizontal").grid(pady=20, row=8, column=1, columnspan=2, sticky="ws")
    browseConf = Button(fenetre, text='Browse among existing\nFilebeat configurations', command=lambda: seeConfigs(), width=20, font=('black', 13), padx=10).grid(row=9, column=1, columnspan=1)
    hr5 = ttk.Separator(fenetre, orient="horizontal").grid(pady=20, row=10, column=1, columnspan=2, sticky="ws")

    fenetre.mainloop()
