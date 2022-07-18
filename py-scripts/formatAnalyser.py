from tkinter import *
from tkinter import ttk

def formatAnalyser(extension : str, sample : str):
    sampled = {
        'headersNumber1':0,
        'headers1':[],
        'headersNumber2':0,
        'headers2':[]
    }

    lines = sample.split('\n')

    emptyLine = True
    while emptyLine == True:
        lines.remove('')
        if ('' not in lines):
            emptyLine = False
    

    if 'csv' in extension:
        headers = lines[0].split(';')
        sampled["headersNumber1"] = len(headers)
        sampled["headers1"] = headers
        headers = lines[0].split(',')
        sampled["headersNumber2"] = len(headers)
        sampled["headers2"] = headers

    else:
        def separatorWindowUi():
            separatorWindow = Tk()
            separatorWindow.title("FileBeatConfigurator")
            mainTitle = Label(separatorWindow, text="Set up your log field separator",font='bold').grid(row=1, column=0, columnspan=3)
            hr1 = ttk.Separator(separatorWindow, orient="horizontal").grid(pady=6, row=2, column=0, columnspan=3, sticky="ws")
            separatorInput = Entry(separatorWindow, textvariable=str, width=30)
            def validateSeparator():
                separator = separatorInput.get()
                headers = lines[0].split(separator)     
                sampled["headersNumber1"] = len(headers)
                sampled["headers1"] = headers
                return separatorWindow.destroy()
            sendButton = Button(separatorWindow, text='Validate fields separator', command=lambda: validateSeparator(), width=50).grid(row=12, column=3, columnspan=2)
            separatorInput.grid(row=7, column=0)
        separatorWindowUi()
    print(sampled["headersNumber1"])
    return sampled