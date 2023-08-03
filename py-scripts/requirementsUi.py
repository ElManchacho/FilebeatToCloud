import psutil, os, subprocess, sys, time
from tkinter import *
from tkinter import ttk

class RequirementsPage:

    pythonVersion : str = ''

    pipVersion : str = ''


    def __init__(self):

        self.pythonVersion = (subprocess.Popen(["powershell.exe", "python --version SilentlyContinue"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)).stdout.read().decode().strip()

        self.pipVersion = (subprocess.Popen(["powershell.exe", "pip --version SilentlyContinue"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)).stdout.read().decode().strip()

    def buildPage(self):

        fenetre = Tk()

        w = 600
        h = 700

        ws = fenetre.winfo_screenwidth()
        hs = fenetre.winfo_screenheight()

        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 1.8)

        fenetre.geometry('%dx%d+%d+%d' % (w, h, x, y))

        fenetre.title("FileBeatConfigurator")

        hr0 = ttk.Separator(fenetre, orient="vertical").grid(row=0, column=0, padx=10, rowspan=11, columnspan=15, sticky="ws")

        hr1 = ttk.Separator(fenetre, orient="horizontal").grid(pady=6, row=0, column=1, columnspan=2, sticky="ws")

        mainTitle = Label(fenetre, text="Requirements : ",font='bold').grid(row=1, column=1)

        pythonTtitle = Label(fenetre, text="Python version : ",font='bold').grid(row=2, column=2)

        pythonVersion = Label(fenetre, text=self.pythonVersion,font='bold').grid(row=2, column=3)

        pipTitle = Label(fenetre, text="Python version : ",font='bold').grid(row=3, column=2)

        pipVersion = Label(fenetre, text=self.pipVersion,font='bold').grid(row=3, column=3)

        fenetre.mainloop()