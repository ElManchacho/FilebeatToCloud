from tkinter import *

def menuUi():

  fenetre = Tk()
  fenetre.title("ElasticDeployment")

  appHeader = LabelFrame(fenetre, text="Menu", padx=20, pady=20)
  appHeader.pack(fill="both", expand="yes")
  mainTitle = Label(appHeader, text="Easy elastic deployment for CLOUD instance", font='bold').pack(side=TOP, padx=0, pady=0)
  
  fenetre.mainloop()