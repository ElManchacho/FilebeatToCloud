import array
from math import ceil
from tkinter import *
from tkinter import ttk

class FieldsConfiguration:

    fields : array

    dragLocation : str

    dropLocation : str

    configsList : array = []

    widthValue : int

    def __init__(self, fields : array):
        self.fields = fields

    def getConfigs(self):
        return self.configsList

    def defConfigs(self):
    
        def dragValue(event):
            if str(tv.identify_column(event.x)).replace('#','') != '':
                self.dragLocation = tv['columns'][int(str(tv.identify_column(event.x)).replace('#',''))-1]

        def dropValue(event):
            tv = event.widget
            if str(tv.identify_column(event.x)).replace('#','') != '':
                self.dropLocation = tv['columns'][int(str(tv.identify_column(event.x)).replace('#',''))-1]
                dragLocationIndex = self.fields.index(self.dragLocation)
                dropLocationIndex = self.fields.index(self.dropLocation)
                self.fields[dragLocationIndex] = self.dropLocation
                self.fields[dropLocationIndex] = self.dragLocation
                tv['columns'] = self.fields
                for field in self.fields:
                    tv.column(field, anchor=CENTER, width=int(ceil(self.widthValue)))
                    tv.heading(field, text=field, anchor=CENTER)

        def Movement(event):
            tv = event.widget
            if str(tv.identify_column(event.x)).replace('#','') != '':
                self.dropLocation = tv['columns'][int(str(tv.identify_column(event.x)).replace('#',''))-1]

        fenetre = Tk()
        
        w = 920

        self.widthValue = w

        h = 450

        ws = fenetre.winfo_screenwidth()
        hs = fenetre.winfo_screenheight()

        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        fenetre.geometry('%dx%d+%d+%d' % (w, h, x, y))

        fenetre.title("FileBeatConfigurator")

        hr0 = ttk.Separator(fenetre, orient="vertical").grid(row=0, column=0, padx=10, rowspan=8, columnspan=1, sticky="ws")

        hr1 = ttk.Separator(fenetre, orient="horizontal").grid(pady=6, row=0, column=1, columnspan=6, sticky="ws")

        mainTitle = Label(fenetre, text="Configure your fields position for the header logs interpreter\n",font='bold').grid(row=1, column=1, columnspan=3)

        hr2 = ttk.Separator(fenetre, orient="horizontal").grid(pady=10, row=2, column=1, columnspan=6, sticky="ws")

        labelInfo = Label(fenetre, text="\nYou can now see your fields configuration respecting the order of your logs columns format\nDrag and drop the columns if it doesn't fit your logs format\n", background="#E1BD0C").grid(row=2, column=1, columnspan=3, rowspan=2)

        hr3 = ttk.Separator(fenetre, orient="horizontal").grid(pady=10, row=4, column=1, columnspan=6, sticky="ws")

        def validateConfigs():
            self.configsList = []
            newConfig = []
            for i in range(len(self.fields)): # Loads fields in input with the input order as the position on the logs files
                newConfig.append({"title":str(self.fields[i]),"position":i})
            self.configsList.append(newConfig)

        
        tv = ttk.Treeview(fenetre, show="headings", height=0)
        style = ttk.Style()
        style.configure("Treeview.Heading", font=('black', 15))
        tv['columns']=(self.fields)
        tv.column('#0', width=0, stretch=NO)
        tv.heading('#0', text='', anchor=CENTER)
        for field in self.fields:
            tv.column(field,anchor=CENTER, width=int(ceil(self.widthValue/4.61))) # Arbitrary column width adjustement because of a weird resize bug when column values changes
            tv.heading(field, text=field, anchor=CENTER)

        tv.grid(row=5, column=3, columnspan=3, rowspan=2)

        tv.bind("<ButtonPress-1>", dragValue)
        tv.bind("<ButtonRelease-1>", dropValue, add='+')
        tv.bind("<B1-Motion>",Movement, add='+')

        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")


        sendButton = Button(fenetre, text='Validate fields', command=lambda: validateConfigs(), width=15, font=('black', 13)).grid(row=12, column=1, columnspan=2)


        fenetre.mainloop()

test = FieldsConfiguration(['f1','f2','f3'])
test.defConfigs()