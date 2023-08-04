from tkinter import *
from tkinter import ttk
from menuNewConfig import menuNewConfig
from configListUi import configListUi
from instanceListUi import instanceListUi
from requirementsUi import RequirementsPage
import os

def menuUi(filbeatVersion, pythonVersion, pipVersion, pipPyyaml, pipPythonDotenv, pipPsutil):

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

    def newCgonfig(filbeatVersion):
        fenetre.destroy()
        menuNewConfig(filbeatVersion)
    
    def seeInstances():
        fenetre.destroy()
        serviceList = instanceListUi()
        serviceList.buildPage()

    def seeConfigs():
        fenetre.destroy()
        configListUi()

    
    versionsObjectList = [{"id":0, "name":"filebeat-8.3.1-windows-x86_64", "version":"8.3.1"}, {"id":1, "name": "filebeat-8.8.2-windows-x86_64", "version":"8.8.2"}]
    versionsList = []
    currentPath = os.getcwd()
    atLeastOneInstalled = False

    for versionObject in versionsObjectList:

        installationPath = currentPath + '\\' + versionObject["name"]

        if (os.path.exists(installationPath)):

            if (versionObject["name"] == filbeatVersion and not atLeastOneInstalled):

                versionsList.insert(0, versionObject["version"]+" (installed)")
                atLeastOneInstalled = True
                
            else:

                versionsList.append(versionObject["version"]+" (installed)")

            versionObject['installed'] = True

        else:

            versionsList.append(versionObject["version"]+" (not installed)")
            versionObject['installed'] = False
    
    baseOptionMenu = StringVar(fenetre)
    baseOptionMenu.set(versionsList[0])
    opt = OptionMenu(fenetre, baseOptionMenu, *versionsList).grid(pady=20, row=10, column=0, columnspan=2)

    def requirements(versionsObjectList, versionsList):
        serviceList = RequirementsPage(versionsObjectList, versionsList, pythonVersion, pipVersion, pipPyyaml, pipPythonDotenv, pipPsutil)
        serviceList.buildPage()

    def getSelectedVersion():
        listSelector = baseOptionMenu.get()
        for versionObject in versionsObjectList:
            if (versionObject["version"] in listSelector):
                return versionObject

    addConf = Button(fenetre, text='Add a new\nFilebeat configuration', command=lambda: newCgonfig(getSelectedVersion()), width=20, font=('black', 13), padx=10).grid(row=5, column=1, columnspan=1)

    hr3 = ttk.Separator(fenetre, orient="horizontal").grid(pady=20, row=6, column=1, columnspan=2, sticky="ws")

    browseInstances = Button(fenetre, text='Browse among existing\nFilebeat instances', command=lambda: seeInstances(), width=20, font=('black', 13), padx=10).grid(row=7, column=1, columnspan=1)

    hr4 = ttk.Separator(fenetre, orient="horizontal").grid(pady=20, row=8, column=1, columnspan=2, sticky="ws")

    browseConf = Button(fenetre, text='Browse among existing\nFilebeat configurations', command=lambda: seeConfigs(), width=20, font=('black', 13), padx=10).grid(row=9, column=1, columnspan=1)

    hr5 = ttk.Separator(fenetre, orient="horizontal").grid(pady=20, row=10, column=1, columnspan=2, sticky="ws")
    
    requirementsButton = Button(fenetre, text='Application requirements', command=lambda: requirements(versionsObjectList, versionsList), width=20, font=('black', 13), padx=10).grid(row=11, column=1, columnspan=2)

    fenetre.mainloop()
