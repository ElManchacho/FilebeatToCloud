import os, fnmatch
from array import array
from dataclasses import field

def findFiles(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(name)
    return result

def generateParserScript(fields : array, emptyField : str = ''):
    
    basePath = os.getcwd().replace('py-scripts','')
    scriptFolderPath = basePath+'filebeatScripts\\'

    if len(fields) == 0 : # no fields --> laxist script
        scriptCounter = 0
        existingScripts = findFiles('laxistCsvParser*.js', scriptFolderPath+'generated\\')

        if len(existingScripts) != 0 :

            lastGeneratedScriptName = (existingScripts[-1].replace('laxistCsvParser','')).replace('.js','')
            scriptCounter =int(lastGeneratedScriptName) + 1

        f = open(scriptFolderPath+"Templates\\laxistCsvParserTemplate.js", "r")
        laxistCsvParserCript = f.read()
        fullPathLaxistScript = scriptFolderPath+"generated\\laxistCsvParser"+ str(scriptCounter) +".js"
        with open(fullPathLaxistScript, 'a') as file:

            file.write(laxistCsvParserCript.strip())

        return fullPathLaxistScript

    else : # generate custome mapping script

        scriptCounter = 0
        existingScripts = findFiles('csvParser*.js', scriptFolderPath+'generated\\')

        if len(existingScripts) != 0 :

            lastGeneratedScriptName = (existingScripts[-1].replace('csvParser','')).replace('.js','')
            scriptCounter =int(lastGeneratedScriptName) + 1

        f = open(scriptFolderPath+"Templates\\strictCsvParserTemplate.js", "r")
        strictCsvParserCript = f.read()
        headersConfig = []
        headersConfig.append({"":""})
        print(headersConfig)
        strictCsvParserCript = strictCsvParserCript.replace('var headers = [];','var headers ='+str(headersConfig)+';',1)
        fullPathScript = scriptFolderPath+"generated\\csvParser"+ str(scriptCounter) +".js"
        #with open(fullPathScript, 'a') as file:

        #    file.write(strictCsvParserCript.strip())
        
        return fullPathScript

generateParserScript(['f1','f2','f3'],'')