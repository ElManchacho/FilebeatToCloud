import os, psutil, subprocess, array
from tkinter import *
from tkinter import ttk
from serviceCardUi import showServiceCard, ServiceCard

class instanceListUi:

    selectedServiceName : str = ''
    
    serviceList : array = []

    def setList(self):
        rawFilebeatServices = [x for x in psutil.win_service_iter() if x.name().lower().startswith('filebeat')]
        filbeatServices = []
        for rawService in rawFilebeatServices:
            svc = psutil.win_service_get(rawService.name())
            filbeatServices.append({"name":svc.name(),"state":svc.status()})
        self.serviceList = filbeatServices

    def __init__(self):
        self.setList()

    def setSelectedServiceName(self, serviceName):
        self.selectedServiceName = serviceName
    
    def getSelectedService(self):
        return self.selectedServiceName

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

        hr0 = ttk.Separator(fenetre, orient="vertical").grid(row=0, column=0, padx=10, rowspan=11, columnspan=1, sticky="ws")

        hr1 = ttk.Separator(fenetre, orient="horizontal").grid(pady=6, row=0, column=1, columnspan=2, sticky="ws")

        mainTitle = Label(fenetre, text="List of registered Filebeat services :",font='bold', pady=10).grid(row=1, column=1, columnspan=1)

        hr2 = ttk.Separator(fenetre, orient="horizontal").grid(pady=30, row=2, column=1, columnspan=2, sticky="ws")

        listServices = ttk.Treeview(fenetre, column=("service_name", "service_state"), show='headings')
        listServices.heading('service_name', text='Service name')
        listServices.heading('service_state', text='Service state')

        for service in self.serviceList :
            listServices.insert('', END, values=(service["name"], service["state"]))


        def selectService(event):
            listServices = event.widget
            selection = [listServices.item(item)["values"] for item in listServices.selection()][0]
            self.setSelectedServiceName(selection[0])

        def showCard():
            selectedName = self.getSelectedService()
            if (selectedName != ''):
                showServiceCard(self.getSelectedService())
                self.setList()
            # else message "Please select a Serivice first."


        hr0 = ttk.Separator(fenetre, orient="vertical").grid(row=0, column=11, padx=10, rowspan=11, columnspan=1, sticky="ws")
        showCardButton = Button(fenetre, text='Show service card',command=lambda: showCard(), font=("black", 12)).grid(row=4, column=12, columnspan=2)
        listServices.bind("<<TreeviewSelect>>", selectService)
        listServices.grid(row=4, column=1, columnspan=10, sticky="ws")


        # TODO : Add scrollbar to treeview

        # TODO : Add refresh button



        fenetre.mainloop()