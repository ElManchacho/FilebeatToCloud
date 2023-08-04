from array import array
from tkinter import *
from tkinter import ttk
from parserScriptGenerator import generateParserScript
from fieldsConfigurationUi import FieldsConfiguration

class defFields:

  scriptPath : str

  def __init__(self) -> None:
    self.scriptPath = ''

  def setPath(self, newPath):
    self.scriptPath = newPath
  
  def getPath(self):
    return self.scriptPath

  def defFieldsUi(self, extractedFields : dict):

    fenetre = Tk()

    w = 470
    h = 480

    ws = fenetre.winfo_screenwidth()
    hs = fenetre.winfo_screenheight()

    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    fenetre.geometry('%dx%d+%d+%d' % (w, h, x, y))

    fenetre.title("FileBeatConfigurator")

    
    hr0 = ttk.Separator(fenetre, orient="vertical").grid(row=0, column=0, padx=10, rowspan=8, columnspan=1, sticky="ws")

    hr1 = ttk.Separator(fenetre, orient="horizontal").grid(pady=6, row=0, column=1, columnspan=6, sticky="ws")

    mainTitle = Label(fenetre, text="Configure your logs extract fields\n",font='bold').grid(row=1, column=1, columnspan=3)

    hr2 = ttk.Separator(fenetre, orient="horizontal").grid(pady=10, row=2, column=1, columnspan=6, sticky="ws")

    labelInfo = Label(fenetre, text="\nThe following fields names were generated from your sample.\nFeel free to add / modify / delete the ones you don't judge coherent.  \n", background="#E1BD0C").grid(row=2, column=1, columnspan=3, rowspan=2)

    fieldsTitle = Label(fenetre, text="Field(s)",pady=10, font=('black', 12)).grid(row=6, column=1, sticky="ws")
    addFieldsTitle = Label(fenetre, text="Add a log field :", pady=10).grid(row=7, column=1)
    fieldsEntry = Entry(fenetre, textvariable=str, width=30)
    listFields = Listbox(fenetre)
    for header in extractedFields["headers"]:
      listFields.insert('end', header)

    def addFields():

      newFields = fieldsEntry.get()

      if newFields != '':
        listFields.insert("end", newFields)
        fieldsEntry.delete(0, "end")

    def delFields():
      if listFields.curselection():
        listFields.delete(listFields.curselection())
        
    addFieldsButton = Button(fenetre, text='Add',command=lambda: addFields(), font=("black", 10)).grid(padx=20, row=7, column=2)
    fieldsEntry.grid(row=7, column=1)
    listFields.grid(row=8, column=1, columnspan=2, sticky="we")
    deleteFieldsButton = Button(fenetre, text='Delete fields',command=lambda: delFields(), font=("black", 10)).grid(padx=20, row=8, column=3)

    def validateFields(numberOfConfigs):
      try:
        int(numberOfConfigs)
      except:
        fenetre.destroy()
        return None
      if numberOfConfigs != '' and int(numberOfConfigs) > 0 :
        fields = listFields.get('@1,0','end')
        fenetre.destroy()
        configs = []
        for configIndex in range(int(numberOfConfigs)):
          fieldsArray =[]
          for field in fields: # convert tuple into array
            fieldsArray.append(field)
          fieldsConfigs = FieldsConfiguration(fieldsArray, configIndex)
          fieldsConfigs.defConfigs()
          configs.append(fieldsConfigs.getConfig())
        mappingScriptPath = generateParserScript(configs)
        self.scriptPath = mappingScriptPath
      

    hr3 = ttk.Separator(fenetre, orient="horizontal").grid(pady=10, row=11, column=1, columnspan=6, sticky="ws")
    labelConfigCount = Label(fenetre, text='Indicate the number of fields\nconfiguration your logs may encounter').grid(row=12, column=1, padx=10)
    entryConfigCount = Entry(fenetre, justify='center', width=10)
    entryConfigCount.insert(END, '1')
    sendButton = Button(fenetre, text='Configure fields order', command=lambda: validateFields(entryConfigCount.get()), width=20, font=('black', 13), padx=10).grid(row=13, column=2, columnspan=2)
    entryConfigCount.grid(row=13, column=1, padx=10)
    hr4 = ttk.Separator(fenetre, orient="horizontal").grid(pady=10, row=14, column=1, columnspan=6, sticky="ws")

    fenetre.mainloop()