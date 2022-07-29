from tkinter import *
from tkinter import ttk


def formatAnalyser(extension: str, sample: str, separator: str):

    sampled = {
        'headersNumber': 0,
        'headers': ['']
    }

    lines = sample.split('\n')

    emptyLine = True
    while emptyLine == True:
        lines.remove('')
        if ('' not in lines):
            emptyLine = False

    interpreted = None
    
    if 'csv' in extension:
        if separator == "":
            interpreted = interpret(lines, ";")
        else:
            interpreted = interpret(lines, separator)
        sampled["headersNumber"] = interpreted["headersNumber"]
        sampled["headers"] = interpreted["headers"]
    else:
        if separator !="":
            interpreted = interpret(lines, separator)
            sampled["headersNumber"] = interpreted["headersNumber"]
            sampled["headers"] = interpreted["headers"]
    return sampled

def interpret(text, sep):
    headers = text[0].split(sep)
    if headers[-1] == '' :
        headers.pop()
    for i in range(len(headers)):
        if headers[i]=='' or headers[i]==' ':
            headers[i] = '<empty field>'
    return {"headersNumber": len(headers), "headers": headers}