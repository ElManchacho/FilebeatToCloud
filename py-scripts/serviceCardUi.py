import psutil, os, subprocess, sys, time
from tkinter import *
from tkinter import ttk

class ServiceCard:

    name : str

    state : str

    def __init__(self, serviceName):
        self.name = serviceName
        rawFilebeatService = [x for x in psutil.win_service_iter() if x.name().lower() == serviceName]
        svc = psutil.win_service_get(rawFilebeatService[0].name())
        self.name = svc.name()
        self.state = svc.status()


    # TODO : Add Service description Card : Name, State (color ?), filebeat.yml config data, header mapping scripts,
    #        index name, check if endpoint is alive

    # TODO : Add possibility to Restart/Start/Stop/Delete services
    
    # TODO : Make "Delete Service" button match with selected Service's card,
    #        not a global delete that would take the lastly selected service without observing the card
    
    def delete(self):
        print(self.name)
        path = os.getcwd()+'\\custom-uninstall-service-filebeat.ps1' 
        subprocess.run(["powershell.exe",path+" -serviceName "+str(self.name)],stdout=sys.stdout)


# TODO : Create the Service card window

def showServiceCard(serviceName):
    
    selectedService = ServiceCard(serviceName)

    fenetre = Tk()

    w = 600
    h = 700

    ws = fenetre.winfo_screenwidth()
    hs = fenetre.winfo_screenheight()

    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 1.8)

    fenetre.geometry('%dx%d+%d+%d' % (w, h, x, y))

    fenetre.title("FileBeatConfigurator")

    hr0 = ttk.Separator(fenetre, orient="vertical").grid(row=0, column=0, padx=10, rowspan=11, columnspan=1, sticky="ws")

    hr1 = ttk.Separator(fenetre, orient="horizontal").grid(pady=6, row=0, column=1, columnspan=2, sticky="ws")

    serviceName = Label(fenetre, text="Name : "+selectedService.name,font='bold', pady=10).grid(row=1, column=1, columnspan=1)

    hr2 = ttk.Separator(fenetre, orient="horizontal").grid(pady=30, row=2, column=1, columnspan=2, sticky="ws")
    
    serviceState = Label(fenetre, text="State : "+selectedService.state,font='bold', pady=10).grid(row=3, column=1, columnspan=1)

    hr3 = ttk.Separator(fenetre, orient="horizontal").grid(pady=30, row=4, column=1, columnspan=2, sticky="ws")

    def deleteService():
        selectedService.delete()
        fenetre.destroy()
    
    showCardButton = Button(fenetre, text='Delete',command=lambda: deleteService(), font=("black", 12)).grid(row=4, column=12, columnspan=2)

    # TODO : Add refresh button

    fenetre.mainloop()