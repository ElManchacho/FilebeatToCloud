import os, sys, psutil, subprocess
from tkinter import *
from tkinter import ttk

def instanceListUi(filbeatVersion):

    selectedService = {}
    
    rawFilebeatServices = [x for x in psutil.win_service_iter() if x.name().lower().startswith('filebeat')]
    filbeatServices = []
    for rawService in rawFilebeatServices:
        svc = psutil.win_service_get(rawService.name())
        filbeatServices.append({"name":svc.name(),"state":svc.status()})

    fenetre = Tk()

    w = 1200
    h = 700

    ws = fenetre.winfo_screenwidth()
    hs = fenetre.winfo_screenheight()

    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 1.8)

    fenetre.geometry('%dx%d+%d+%d' % (w, h, x, y))

    fenetre.title("FileBeatConfigurator")

    hr1 = ttk.Separator(fenetre, orient="horizontal").grid(pady=6, row=0, column=0, columnspan=6, sticky="ws")

    mainTitle = Label(fenetre, text="List of registered Filebeat services :",font=('black', 15),).grid(row=1, column=0, columnspan=3)

    listServices = ttk.Treeview(fenetre, column=("service_name", "service_state"), show='headings')
    listServices.heading('service_name', text='Service name')
    listServices.heading('service_state', text='Service state')

    for service in filbeatServices :
        listServices.insert('', END, values=(service["name"], service["state"]))
    
    # TODO : Add Service description Card : Name, State (color ?), filebeat.yml config data, header mapping scripts,
    #        index name, check if endpoint is alive

    # TODO : Add possibility to Restart/Start/Stop/Delete services

    def selectService(event):
        listServices = event.widget
        selection = [listServices.item(item)["values"] for item in listServices.selection()][0]
        service = {"name":selection[0], "state":selection[1]}
        selectedService = service

    # TODO : Make "Delete Service" button match with selected Service's card,
    #        not a global delete that would take the lastly selected service without observing the card
    
    def deleteService(service):
        print(service)
        path = os.getcwd()+'\\custom-uninstall-service-filebeat.ps1' 
        subprocess.run(["powershell.exe",path+" -serviceName "+service["name"]],stdout=sys.stdout)
    addPathButton = Button(fenetre, text='Add',command=lambda: deleteService(selectedService), font=("black", 12)).grid(row=7, column=1)
    listServices.bind("<<TreeviewSelect>>", selectService)
    listServices.grid(row=8, column=0, columnspan=10, sticky="ws")


    # TODO : Add scrollbar to treeview

    # TODO : Add refresh button



    return None