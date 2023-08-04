import os, subprocess, sys, time
from tkinter import *
from tkinter import ttk

class RequirementsPage:

    pythonVersion : str = ''

    pipVersion : str = ''

    pipPyyaml : str = ''

    pipPythonDotenv : str = ''

    pipPsutil : str = ''

    mustDeploy : bool =  False

    versionsObjectList = []

    filebeatVersions = []

    def __init__(self, versionsObjects, versionsList, pythonVersion, pipVersion, pipPyyaml, pipPythonDotenv, pipPsutil):

        self.versionsObjectList = versionsObjects

        self.filebeatVersions = versionsList

        self.pythonVersion = pythonVersion

        self.pipVersion = pipVersion

        self.pipPyyaml = pipPyyaml
        
        self.pipPythonDotenv = pipPythonDotenv
        
        self.pipPsutil = pipPsutil

        if (self.pythonVersion == ''):
            self.pythonVersion = "Warning : Dependency is not installed"
            self.mustDeploy = True

        if (self.pipVersion == ''):
            self.pipVersion = "Warning : Dependency is not installed"
            self.mustDeploy = True

        if (self.pipPyyaml == ''):
            self.pipPyyaml = "Warning : Dependency is not installed"
            self.mustDeploy = True

        if (self.pipPythonDotenv == ''):
            self.pipPythonDotenv = "Warning : Dependency is not installed"
            self.mustDeploy = True

        if (self.pipPsutil == ''):
            self.pipPsutil = "Warning : Dependency is not installed"
            self.mustDeploy = True


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

        mainTitle = Label(fenetre, text="Requirements : ",font='bold', pady=30).grid(row=1, column=1)

        pythonTtitle = Label(fenetre, text="Python version\n(must be 3.5 or higher) : ", font=('bold', 13)).grid(row=2, column=1)

        pythonVersion = Label(fenetre, text=self.pythonVersion,font=('black', 9)).grid(row=2, column=2)

        pipTitle = Label(fenetre, text="pip version : ", font=('bold', 13)).grid(row=3, column=1)

        pipVersion = Label(fenetre, text=self.pipVersion,font=('black', 9)).grid(row=3, column=2)

        pipPyyamlTitle = Label(fenetre, text="pip pyyaml : ", font=('bold', 13)).grid(row=4, column=1)

        pipPyyamlVersion = Label(fenetre, text=self.pipPyyaml,font=('black', 9)).grid(row=4, column=2)

        pipPythonDotenvTitle = Label(fenetre, text="pip python-dotenv : ", font=('bold', 13)).grid(row=5, column=1)

        pipPythonDotenvVersion = Label(fenetre, text=self.pipPythonDotenv,font=('black', 9)).grid(row=5, column=2)

        pipPsutilTitle = Label(fenetre, text="pip psutil : ", font=('bold', 13)).grid(row=6, column=1)

        pipPsutilVersion = Label(fenetre, text=self.pipPsutil,font=('black', 9)).grid(row=6, column=2)

        filebeatTitle = Label(fenetre, text="Filebeat versions : ", font=('bold', 13)).grid(row=7, column=1)

        baseOptionMenu = StringVar(fenetre)
        baseOptionMenu.set(self.filebeatVersions[0])
        filebeatVersions = OptionMenu(fenetre, baseOptionMenu, *self.filebeatVersions).grid(pady=20, row=7, column=2, columnspan=2)

        def deployment():
            fenetre.destroy()
            currentPath = str(os.getcwd())
            subprocess.run(["powershell.exe", currentPath+"\\deployment.ps1"])

        if (self.mustDeploy):

                deployTitle = Label(fenetre, text="If something is missing, redploy\nyour environnement here : ", font=('bold', 13)).grid(row=9, column=1)

                reployEnv = Button(fenetre, text='Deploy environnement', command=lambda: deployment(), width=20, font=('black', 13), padx=10).grid(row=9, column=2, columnspan=1)

                deploytWarning = Label(fenetre, text="Warning : This will overwrite\n every installed version of the elements\n above on your system !", font=('bold', 13)).grid(row=10, column=2)


        fenetre.mainloop()