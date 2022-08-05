import os, sys, time
from tkinter import *
from tkinter import ttk
from ymlCompiler import ymlComipler
import subprocess
from dotenv import load_dotenv

class envChecked:
  _protected_elasticUrl : bool = False
  _protected_elasticUsername : bool = False
  _protected_elasticPassword : bool = False

  def getelasticUrl(self):
    return self._protected_elasticUrl

  def getelasticUsername(self):
    return self._protected_elasticUsername

  def getelasticPassword(self):
    return self._protected_elasticPassword

  def setelasticUrl(self, value:bool):
    self._protected_elasticUrl = value

  def setelasticUsername(self, value:bool):
    self._protected_elasticUsername = value

  def setelasticPassword(self, value:bool):
    self._protected_elasticPassword = value

class loadEnv:
  _protected_hosts : str
  _protected_username : str
  _protected_password : str
  def __init__(self):
    
    load_dotenv()

    self._protected_hosts = os.getenv("HOSTS")
    self._protected_username = os.getenv("USRNAME")
    self._protected_password = os.getenv("PASSWORD")

  def getHosts(self):
    return self._protected_hosts

  def getUsername(self):
    return self._protected_username

  def getPassword(self):
    return self._protected_password

def menuNewConfig():

  fenetre = Tk()

  envCheckable = envChecked()

  def checkState(check, entry : ttk.Entry, fieldId : int):
    env = loadEnv()
    if fieldId == 0:
      if envCheckable.getelasticUsername() == True:
         envCheckable.setelasticUsername(False)
         entry.delete(0,'end')
      else:
        envCheckable.setelasticUsername(True)
        entry.delete(0,'end')
        entry.insert('end',env.getUsername())
    elif fieldId == 1:
      if envCheckable.getelasticPassword() == True:
         envCheckable.setelasticPassword(False)
         entry.delete(0,'end')
      else:
        envCheckable.setelasticPassword(True)
        entry.delete(0,'end')
        entry.insert('end',env.getPassword())
    elif fieldId == 2:
      if envCheckable.getelasticUrl() == True:
         envCheckable.setelasticUrl(False)
         entry.delete(0,'end')
      else:
        envCheckable.setelasticUrl(True)
        entry.delete(0,'end')
        entry.insert('end',env.getHosts())

  w = 1200
  h = 700

  ws = fenetre.winfo_screenwidth()
  hs = fenetre.winfo_screenheight()

  x = (ws / 2) - (w / 2)
  y = (hs / 2) - (h / 1.8)

  fenetre.geometry('%dx%d+%d+%d' % (w, h, x, y))

  fenetre.title("FileBeatConfigurator")

  hr1 = ttk.Separator(fenetre, orient="horizontal").grid(pady=6, row=0, column=0, columnspan=6, sticky="ws")

  mainTitle = Label(fenetre, text="Configure your Filebeat environnement",font=('bold', 20)).grid(row=1, column=0, columnspan=3)

  hr2 = ttk.Separator(fenetre, orient="horizontal").grid(pady=10, row=2, column=0, columnspan=6, sticky="ws")

  elasticUsernameLabel = Label(fenetre, text="Elastic username", font=("black", 10), pady=10).grid(row=3, column=0, sticky="ws")
  elasticUsername = Entry(fenetre, textvariable=str, width=30, font=("black", 10))

  c1 = ttk.Checkbutton(fenetre, text='Use env variable',command=lambda:checkState(envCheckable, elasticUsername, 0), onvalue=True, offvalue=False)
  c1.grid(row=3, column=2, sticky="ws")

  elasticPasswordLabel = Label(fenetre, text="Elastic password", font=("black", 10),pady=10).grid(row=4, column=0, sticky="ws")
  elasticPassword = Entry(fenetre, show="*", textvariable=str, width=30, font=("black", 10))

  c2 = ttk.Checkbutton(fenetre, text='Use env variable',command=lambda:checkState(envCheckable, elasticPassword, 1), onvalue=True, offvalue=False)
  c2.grid(row=4, column=2, sticky="ws")

  elasticUrlLabel = Label(fenetre, text="Elasticsearch endpoint", font=("black", 10),pady=10).grid(row=5, column=0, sticky="ws")
  elasticUrl = Entry(fenetre, textvariable=str, width=30, font=("black", 10))

  c3 = ttk.Checkbutton(fenetre, text='Use env variable',command=lambda:checkState(envCheckable, elasticUrl, 2), onvalue=True, offvalue=False)
  c3.grid(row=5, column=2, sticky="ws")

  pathTitle = Label(fenetre, text="Paths", font=("black", 10), pady=10).grid(row=6, column=0, sticky="ws")
  addPathTitle = Label(fenetre, text="Add a log path :", pady=10).grid(row=7, column=0)
  pathEntry = Entry(fenetre, textvariable=str, width=30, font=("black", 10))
  listPath = Listbox(fenetre, font=("black", 9))

  def addPath():

    newPath = pathEntry.get()

    if newPath != '':
      listPath.insert("end", newPath)
      pathEntry.delete(0, "end")

  def delPath():
    if listPath.curselection():
      listPath.delete(listPath.curselection())
  addPathButton = Button(fenetre, text='Add',command=lambda: addPath(), font=("black", 12)).grid(row=7, column=1)
  pathEntry.grid(row=7, column=0)
  listPath.grid(row=8, column=0, columnspan=2, sticky="we")
  listPath.insert(0,os.getcwd().replace('py-scripts','Logs\\input'))
  deletePathButton = Button(fenetre, text='Delete path',command=lambda: delPath(), font=("black", 10)).grid(row=8, column=2)

  hr3 = ttk.Separator(fenetre, orient="vertical").grid(row=3, column=3, padx=10, rowspan=8, sticky="ns")

  indexLabel = Label(fenetre, text="Kibana index name", pady=10, font=("black", 10)).grid(row=3, column=4)
  index = Entry(fenetre, textvariable=str, width=30, font=("black", 10))
  fileExtensionLabel = Label(fenetre, text="File extension", font=("black", 10)).grid(row=4, column=4)
  fileExtension = Entry(fenetre, textvariable=str, width=30, font=("black", 10))
  separatorLabel = Label(fenetre, text="Attribute separator", font=("black", 10)).grid(row=5, column=4)
  separatorInput = Entry(fenetre, textvariable=str, width=30, font=("black", 10))
  logTypeLabel = Label(fenetre, text="Copy and paste a sample of your logs down there : ", font=("black", 10)).grid(row=6, column=4)
  logSample = Text(fenetre, bg="light grey", font=("black", 8), height=25, width=100, padx=20, pady=20)

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
      "sample": logSample.get('@1,0', 'end'),
      "separator": separatorInput.get() or ''
    }
    fenetre.destroy()
    ymlComipler(dicoInput)



    return None
    path = os.getcwd()+'\\filebeat-8.3.1-windows-x86_64\\install-service-filebeat.ps1'
    subprocess.Popen(["powershell.exe",path],stdout=sys.stdout)
    time.sleep(5)

    subprocess.Popen(["powershell.exe",'Start-Service filebeat'],stdout=sys.stdout)

    subprocess.Popen(["powershell.exe",'Get-Service filebeat'],stdout=sys.stdout)

    time.sleep(5)
    
    fenetre.destroy()
    
  elasticUsername.grid(row=3, column=1)
  elasticPassword.grid(row=4, column=1)
  elasticUrl.grid(row=5,column=1)
  index.grid(row=3, column=5)
  fileExtension.grid(row=4, column=5)
  fileExtension.insert(0,'txt')
  separatorInput.grid(row=5, column=5)
  separatorInput.insert(0, ';')
  logSample.grid(row=7, column=4, columnspan=2, rowspan=4)
  hr4 = ttk.Separator(fenetre, orient="horizontal").grid(pady=10, row=11, column=0, columnspan=6, sticky="ws")
  sendButton = Button(fenetre, text='Go to fields configuration', command=lambda: validateConfig(), width=50, font=("black", 15)).grid(row=12, column=1, columnspan=4)
  hr5 = ttk.Separator(fenetre, orient="horizontal").grid(pady=10, row=13, column=0, columnspan=6, sticky="ws")

  fenetre.mainloop()