import psutil, os, subprocess, sys, time
from tkinter import *
from tkinter import ttk

class ServiceCard:

    name : str

    state : str

    def initServiceData(self, serviceName):
        rawFilebeatService = [x for x in psutil.win_service_iter() if x.name().lower() == serviceName]
        svc = psutil.win_service_get(rawFilebeatService[0].name())
        self.name = svc.name()
        self.state = svc.status()

    def __init__(self, serviceName):
        self.initServiceData(serviceName)

    def getState(self):
        return self.state

    def setState(self, newState):
        self.state = newState
    
    # TODO : Add Service description Card : Name, State (color ?), filebeat.yml config data, header mapping scripts,
    #        index name, check if endpoint is alive

    # TODO : Add possibility to Restart/Start/Stop/Delete services
    
    # TODO : Make "Delete Service" button match with selected Service's card,
    #        not a global delete that would take the lastly selected service without observing the card
    
    def delete(self):
        try:
            path = os.getcwd()+'\\custom-uninstall-service-filebeat.ps1' 
            subprocess.run(["powershell.exe", path+" -serviceName "+str(self.name)+" -ErrorVariable badoutput -ErrorAction SilentlyContinue"])
            self.setState('deleted')
        except Exception as error:
            print(error)
        

    def start(self):
        try:
            subprocess.run(["powershell.exe","Start-Service "+str(self.name)+" -ErrorVariable badoutput -ErrorAction SilentlyContinue"])
        except Exception as error:
            print("error")
    

    def stop(self):
        try:
            subprocess.run(["powershell.exe","Stop-Service "+str(self.name)+" -ErrorVariable badoutput -ErrorAction SilentlyContinue"])
        except Exception as error:
            print(error)

    def restart(self):
        try:
            subprocess.run(["powershell.exe","Restart-Service "+str(self.name)+" -ErrorVariable badoutput -ErrorAction SilentlyContinue"])
        except Exception as error:
            print(error)

    # TODO : Create the Service card window

    def showServiceCard(self):

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

        serviceName = Label(fenetre, text="Name : "+self.name,font='bold', pady=10).grid(row=1, column=1, columnspan=14)

        hr2 = ttk.Separator(fenetre, orient="horizontal").grid(pady=30, row=2, column=1, columnspan=2, sticky="ws")
        
        serviceState = Label(fenetre, text="State : "+self.state,font='bold', pady=10)

        hr3 = ttk.Separator(fenetre, orient="horizontal").grid(pady=30, row=4, column=1, columnspan=2, sticky="ws")

        def startService():
            try :
                self.start()
                refreshService()
            except Exception as error:
                print("error")
        
        sartServiceButton = Button(fenetre, text='Start',command=lambda: startService(), font=("black", 12)).grid(row=4, column=4)

        def stopService():
            try :
                self.stop()
                refreshService()
            except Exception as error:
                print(error)
        
        stopServiceButton = Button(fenetre, text='Stop',command=lambda: stopService(), font=("black", 12)).grid(row=4, column=6)

        def restartService():
            try :
                self.restart()
                refreshService()
            except Exception as error:
                print(error)
        
        restartServiceButton = Button(fenetre, text='Restart',command=lambda: restartService(), font=("black", 12)).grid(row=4, column=8)

        def deleteService():
            try :
                self.delete()
                fenetre.destroy()
            except Exception as error:
                print(error)
        
        deleteServiceButton = Button(fenetre, text='Delete',command=lambda: deleteService(), font=("black", 12)).grid(row=4, column=10)

        def refreshService():
            self.initServiceData(self.name)
            serviceState.config(text="State : "+self.state)

        refreshServiceButton = Button(fenetre, text='Refresh',command=lambda: refreshService(), font=("black", 12)).grid(row=2, column=15)

        serviceState.grid(row=3, column=1, columnspan=1)

        fenetre.mainloop()