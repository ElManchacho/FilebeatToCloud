from tkinter import *
from tkinter import ttk

def defFieldsUi(extractedFields):

  fenetre = Tk()
  fenetre.title("FileBeatConfigurator")

  hr1 = ttk.Separator(fenetre, orient="horizontal").grid(pady=6, row=0, column=0, columnspan=6, sticky="ws")

  mainTitle = Label(fenetre, text="Configure your logs extract fields",font='bold').grid(row=1, column=0, columnspan=3)

  hr2 = ttk.Separator(fenetre, orient="horizontal").grid(pady=10, row=2, column=0, columnspan=6, sticky="ws")

  labelInfo = Label(fenetre, text="\n  The following fields names were generated from your sample, feel free to add / modify / delete the ones you don't judge coherent.  \n", background="#E1BD0C").grid(row=2, column=0, columnspan=3, rowspan=2)

  fieldsTitle = Label(fenetre, text="Fields(s)",pady=10).grid(row=6, column=0, sticky="ws")
  addFieldsTitle = Label(fenetre, text="Add a log field :", pady=10).grid(row=7, column=0)
  fieldsEntry = Entry(fenetre, textvariable=str, width=30)
  listFields = Listbox(fenetre)
  for header in extractedFields["headers1"]:
    listFields.insert('end', header)

  def addFields():

    newFields = fieldsEntry.get()

    if newFields != '':
      listFields.insert("end", newFields)
      fieldsEntry.delete(0, "end")

  def delFields():
    if listFields.curselection():
      listFields.delete(listFields.curselection())
  addFieldsButton = Button(fenetre, text='Add',command=lambda: addFields()).grid(row=7, column=1)
  fieldsEntry.grid(row=7, column=0)
  listFields.grid(row=8, column=0, columnspan=2, sticky="we")
  deleteFieldsButton = Button(fenetre, text='Delete fields',command=lambda: delFields()).grid(row=8, column=2)

  def validateFields():
    
    fenetre.destroy()

  hr3 = ttk.Separator(fenetre, orient="horizontal").grid(pady=10, row=11, column=0, columnspan=6, sticky="ws")
  sendButton = Button(fenetre, text='Validate fields', command=lambda: validateFields(), width=50).grid(row=12, column=3, columnspan=2)
  hr4 = ttk.Separator(fenetre, orient="horizontal").grid(pady=10, row=13, column=0, columnspan=6, sticky="ws")

  fenetre.mainloop()

  # get :
  #     - elastic username (default : elastic) --> Ok
  #     - elastic password --> Ok
  #     - cloud kibana URI --> Ok
  #     - nom index (default : index) --> En cours ....
  #     - liste des fields de logs --> Ok
  #     - intel recup champs + envoi dans script (Pas fait) de modifcation de filebeat.yml
  #     - BONUS : type de fichier de logs --> UI : OK, Intel : on verra
          #   processors: 
          #   - decode_csv_fields:
          #       fields: 
          #         message: decoded.csv 
          #       separator: ";"
          #   - extract_array:
          #       field: decoded.csv
          #       mappings:
          #         parsed.attribute1: 0
          #         parsed.attribute2: 1
          #         parsed.attribute3: 2
          #         parsed.attribute4: 3
          #         parsed.attribute5: 4
          #         parsed.attribute6: 5
          #         parsed.attribute7: 6
          #         parsed.attribute8: 7
          #         parsed.attribute9: 8
          #         parsed.attribute10: 9
          #   - drop_fields:
          #       fields: ["decoded"]

