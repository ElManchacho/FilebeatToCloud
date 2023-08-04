from tkinter import *
from tkinter import ttk
from requirementsUi import RequirementsPage
import os

def poorMenuUi():

    fenetre = Tk()

    w = 380
    h = 480

    ws = fenetre.winfo_screenwidth()
    hs = fenetre.winfo_screenheight()

    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    fenetre.geometry('%dx%d+%d+%d' % (w, h, x, y))

    fenetre.title("FileBeatConfigurator")
    
    hr0 = ttk.Separator(fenetre, orient="vertical").grid(row=0, column=0, padx=10, rowspan=12, columnspan=1, sticky="ws")

    hr1 = ttk.Separator(fenetre, orient="horizontal").grid(pady=6, row=0, column=1, columnspan=2, sticky="ws")

    mainTitle = Label(fenetre, text="Welcome on the FilbeatToCloud app !",font='bold', pady=10, anchor="center").grid(row=1, column=1, columnspan=1)

    hr2 = ttk.Separator(fenetre, orient="horizontal").grid(pady=10, row=2, column=1, columnspan=2, sticky="ws")

    scndTitle = Label(fenetre, text="Menu",font=('black', 15)).grid(row=3, column=1, columnspan=1)

    hr2bis = ttk.Separator(fenetre, orient="horizontal").grid(pady=10, row=4, column=1, columnspan=1, sticky="ws")
 
    versionsObjectList = [{"id":0, "name":"filebeat-8.2.1-windows-x86_64", "version":"8.2.1"},{"id":1, "name": "filebeat-8.8.2-windows-x86_64", "version":"8.8.2"}]
    versionsList = []
    currentPath = os.getcwd()
    for versionObject in versionsObjectList:
        installationPath = currentPath + '\\' + versionObject["version"]
        if (os.path.exists(installationPath)):
            versionsList.append(versionObject["version"]+" (installed)")
            versionObject['installed'] = True
        else:
            versionsList.append(versionObject["version"]+" (not installed)")
            versionObject['installed'] = False
   
    def requirements(versionsObjectList, versionsList, pythonVersion, pipVersion, pipPyyaml, pipPythonDotenv, pipPsutil):
        serviceList = RequirementsPage(versionsObjectList, versionsList)
        fenetre.destroy()
        serviceList.buildPage()

    requirementsButton = Button(fenetre, text='Application requirements', command=lambda: requirements(versionsObjectList, versionsList), width=20, font=('black', 13), padx=10).grid(row=11, column=1, columnspan=2)

    fenetre.mainloop()
