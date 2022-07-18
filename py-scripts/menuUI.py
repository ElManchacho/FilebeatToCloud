import os, sys, time
from tkinter import *
from tkinter import ttk
from ymlCompiler import ymlComipler
import subprocess

def menuUi():

  fenetre = Tk()
  fenetre.title("FileBeatConfigurator")

  hr1 = ttk.Separator(fenetre, orient="horizontal").grid(pady=6, row=0, column=0, columnspan=6, sticky="ws")

  mainTitle = Label(fenetre, text="Configure your Filebeat environnement",font='bold').grid(row=1, column=0, columnspan=3)

  hr2 = ttk.Separator(fenetre, orient="horizontal").grid(pady=10, row=2, column=0, columnspan=6, sticky="ws")

  elasticUsernameLabel = Label(fenetre, text="Elastic username (default : elastic)",pady=10).grid(row=3, column=0, sticky="ws")
  elasticUsername = Entry(fenetre, textvariable=str, width=30)

  elasticPasswordLabel = Label(fenetre, text="Elastic password",pady=10).grid(row=4, column=0, sticky="ws")
  elasticPassword = Entry(fenetre, textvariable=str, width=30)

  elasticUrlLabel = Label(fenetre, text="Elasticsearch endpoint",pady=10).grid(row=5, column=0, sticky="ws")
  elasticUrl = Entry(fenetre, textvariable=str, width=30)

  pathTitle = Label(fenetre, text="Path(s)",pady=10).grid(row=6, column=0, sticky="ws")
  addPathTitle = Label(fenetre, text="Add a log path :", pady=10).grid(row=7, column=0)
  pathEntry = Entry(fenetre, textvariable=str, width=30)
  listPath = Listbox(fenetre)

  def addPath():

    newPath = pathEntry.get()

    if newPath != '':
      listPath.insert("end", newPath)
      pathEntry.delete(0, "end")

  def delPath():
    if listPath.curselection():
      listPath.delete(listPath.curselection())
  addPathButton = Button(fenetre, text='Add',command=lambda: addPath()).grid(row=7, column=1)
  pathEntry.grid(row=7, column=0)
  listPath.grid(row=8, column=0, columnspan=2, sticky="we")
  deletePathButton = Button(fenetre, text='Delete path',command=lambda: delPath()).grid(row=8, column=2)

  hr2 = ttk.Separator(fenetre, orient="vertical").grid(row=3, column=3, padx=10, rowspan=8, sticky="ns")

  indexLabel = Label(fenetre, text="Kibana index name",pady=10).grid(row=3, column=4)
  index = Entry(fenetre, textvariable=str, width=30)
  fileExtensionLabel = Label(fenetre, text="File extension").grid(row=4, column=4)
  fileExtension = Entry(fenetre, textvariable=str, width=30)
  logTypeLabel = Label(fenetre, text="Copy and paste a sample of your logs down there : ").grid(row=5, column=4)
  logSample = Text(fenetre, bg="light grey", font=("black", 10), height=30, width=100, padx=20, pady=20)

  def validateConfig():
    pathsArray = []
    ListOfPaths = listPath.get('@1,0', 'end')
    for path in ListOfPaths:
      pathsArray.append(path)
    dicoInput = {
      "username": elasticUsername.get(), 
      "password": elasticPassword.get(), 
      "hosts": elasticUrl.get(), 
      "paths": pathsArray, 
      "index": index.get(), 
      "extension": fileExtension.get(), 
      "sample": logSample.get('@1,0', 'end')
    }
    ymlComipler(dicoInput)
    return None
    path = os.getcwd()+'\\filebeat-8.3.1-windows-x86_64\\install-service-filebeat.ps1'
    subprocess.Popen(["powershell.exe",path],stdout=sys.stdout)
    time.sleep(5)

    subprocess.Popen(["powershell.exe",'Start-Service filebeat'],stdout=sys.stdout)
    time.sleep(5)
    
    fenetre.destroy()
    
  elasticUsername.grid(row=3, column=1)
  elasticPassword.grid(row=4, column=1)
  elasticUrl.grid(row=5,column=1)
  index.grid(row=3, column=5)
  fileExtension.grid(row=4, column=5)
  logSample.grid(row=6, column=4, columnspan=2, rowspan=5)
  hr3 = ttk.Separator(fenetre, orient="horizontal").grid(pady=10, row=11, column=0, columnspan=6, sticky="ws")
  sendButton = Button(fenetre, text='Validate configuration', command=lambda: validateConfig(), width=50).grid(row=12, column=3, columnspan=2)
  hr4 = ttk.Separator(fenetre, orient="horizontal").grid(pady=10, row=13, column=0, columnspan=6, sticky="ws")

  fenetre.mainloop()