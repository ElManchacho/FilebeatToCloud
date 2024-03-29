import array
from math import ceil
from tkinter import *
from tkinter import ttk

class FieldsConfiguration:

    fields : array

    BASEFIELDS : array

    dragLocation : str

    dropLocation : str

    config: array = []

    configCounter : int

    def __init__(self, fieldsInput : array, configCounter : int):
        self.fields = fieldsInput
        fieldsInputCopy = []
        for field in fieldsInput:
            fieldsInputCopy.append(field)
        self.BASEFIELDS = fieldsInputCopy
        self.configCounter = configCounter

    def getConfig(self):
        return self.config

    def defConfigs(self):

        def deleteHeader(event):
            tv = event.widget
            if str(tv.identify_column(event.x)).replace('#','') != '':
                toDelete = tv['columns'][int(str(tv.identify_column(event.x)).replace('#',''))-1]
                self.fields.pop(self.fields.index(toDelete))
                tv['columns'] = self.fields
                for field in self.fields:
                    tv.column(field, anchor=CENTER)
                    tv.heading(field, text=field, anchor=CENTER)

    
        def dragValue(event):
            tv = event.widget
            if str(tv.identify_column(event.x)).replace('#','') != '':
                self.dragLocation = tv['columns'][int(str(tv.identify_column(event.x)).replace('#',''))-1]

        def dropValue(event):
            tv = event.widget
            if str(tv.identify_column(event.x)).replace('#','') != '':
                self.dropLocation = tv['columns'][int(str(tv.identify_column(event.x)).replace('#',''))-1]
                if (self.dragLocation in self.fields):
                    dragLocationIndex = self.fields.index(self.dragLocation)
                    dropLocationIndex = self.fields.index(self.dropLocation)
                    self.fields[dragLocationIndex] = self.dropLocation
                    self.fields[dropLocationIndex] = self.dragLocation
                    tv['columns'] = self.fields
                    for field in self.fields:
                        tv.column(field, anchor=CENTER)
                        tv.heading(field, text=field, anchor=CENTER)

        def Movement(event):
            tv = event.widget
            if str(tv.identify_column(event.x)).replace('#','') != '':
                self.dropLocation = tv['columns'][int(str(tv.identify_column(event.x)).replace('#',''))-1]

        fenetre = Tk()
        
        w = 650 + (len(self.fields)*50)

        h = 300

        ws = fenetre.winfo_screenwidth()
        hs = fenetre.winfo_screenheight()

        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        fenetre.geometry('%dx%d+%d+%d' % (w, h, x, y))

        fenetre.title("FileBeatConfigurator - Configuration "+str(self.configCounter))

        mainTitle = Label(fenetre, text="Configure your fields position for the header logs interpreter\n",font='bold', padx=5).pack()

        labelInfo = Label(fenetre, text="\nYou can now see your fields configuration respecting the order of your logs columns format\nDrag and drop the columns if it doesn't fit your logs format order\nDouble click a column name to delete it\n", background="#E1BD0C", padx=5).pack()

        labelLineBreak1 = Label(fenetre, text="\n").pack()

        def validateConfigs():
            newConfig = []
            for i in range(len(self.fields)): # Loads fields in input with the input order as the position on the logs files
                newConfig.append({"title":str(self.fields[i]),"position":i})
            self.config = newConfig
            fenetre.destroy()

        
        tv = ttk.Treeview(fenetre, show="headings", height=0)
        style = ttk.Style()
        style.configure("Treeview.Heading", font=('black', 15))
        tv['columns']=(self.fields)
        tv.column('#0', width=0, stretch=NO)
        tv.heading('#0', text='', anchor=CENTER)
        for field in self.fields:
            tv.column(field,anchor=CENTER)
            tv.heading(field, text=field, anchor=CENTER)

        tv.pack(padx=5)

        tv.bind("<ButtonPress-1>", dragValue)
        tv.bind("<ButtonRelease-1>", dropValue, add='+')
        tv.bind("<B1-Motion>",Movement, add='+')
        tv.bind("<Double-1>", deleteHeader, add='+')

        if len(self.fields) > 4:
            
            labelLineBreak2 = Label(fenetre, text="\n", height=1).pack()
            scrollbar = Scrollbar(fenetre, orient='horizontal')
            scrollbar.pack(fill="x", padx=5)
            tv.configure(xscrollcommand=scrollbar.set)
            tv.configure(selectmode="extended")
            scrollbar.configure(command=tv.xview)

            sh2 = ttk.Separator(fenetre, orient="horizontal").pack()
        
        labelLineBreak3 = Label(fenetre, text="\n").pack()

        sendButton = Button(fenetre, text='Validate configuration', command=lambda: validateConfigs(), font=('black', 13), padx=5).pack()

        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")

        fenetre.mainloop()