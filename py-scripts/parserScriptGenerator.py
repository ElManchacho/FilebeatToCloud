import os, fnmatch, json
import array

def findFiles(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(name)
    return result

def generateParserScript(configs : array, emptyField : str = ''): # input logs headers configuration(s) / empty columns value
    
    basePath = os.getcwd().replace('py-scripts','')
    scriptFolderPath = basePath+'filebeatScripts\\'
    if len(configs) == 0 or len(configs[0])==0: # no fields --> laxist script
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

    else : # Generate custom mapping script


        scriptCounter = 0
        existingScripts = findFiles('csvParser*.js', scriptFolderPath+'generated\\')

        if len(existingScripts) != 0 :

            lastGeneratedScriptName = (existingScripts[-1].replace('csvParser','')).replace('.js','')
            scriptCounter =int(lastGeneratedScriptName) + 1

        f = open(scriptFolderPath+"Templates\\strictCsvParserTemplate.js", "r")
        strictCsvParserCript = f.read()
        headersConfigs = configs

        instanceCounter = 0
        configCounter = 0

        existingInstances = findFiles('config_*.json', scriptFolderPath+'generated\\headersConfigs\\')
        for config in headersConfigs:
            if len(existingInstances) != 0 :
                lastGeneratedInstance = (existingInstances[-1].replace('config_','')).replace('.json','').split(".")[0]
                instanceCounter = int(lastGeneratedInstance) + 1
                existingConfigs = findFiles('config_'+str(instanceCounter)+'.*.json', str(scriptFolderPath)+'generated\\headersConfigs\\')
                if len(existingConfigs) != 0 :
                    lastGeneratedConfigs = (existingConfigs[-1].replace('config_'+str(instanceCounter)+'.','')).replace('.json','')[0]
                    configCounter = int(lastGeneratedConfigs) + 1
            else:
                instanceCounter = 0
                configCounter = 0
                existingConfigs = findFiles('config_'+str(instanceCounter)+'.*.json', str(scriptFolderPath)+'generated\\headersConfigs\\')
                if len(existingConfigs) != 0 :
                    lastGeneratedConfigs = (existingConfigs[-1].replace('config_'+str(instanceCounter)+'.','')).replace('.json','')[0]
                    configCounter = int(lastGeneratedConfigs) + 1
            
            with open(scriptFolderPath+"generated\\headersConfigs\\config_"+str(instanceCounter)+"."+str(configCounter)+".json", 'a') as file:

                file.write(json.dumps(config))
        
        strictCsvParserCript = strictCsvParserCript.replace('var headersConfig = [];','var headersConfig ='+str(headersConfigs)+';',1)
        fullPathScript = scriptFolderPath+"generated\\csvParser"+ str(scriptCounter) +".js"
        with open(fullPathScript, 'a') as file:

            file.write(strictCsvParserCript.strip())
        
        return fullPathScript