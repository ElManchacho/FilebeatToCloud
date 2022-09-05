import yaml, os
from formatAnalyser import formatAnalyser
from fieldsSetUpUi import defFields

def ymlComipler(input):
    basePath = os.getcwd().replace('py-scripts','')
    filebeatPath = basePath+'\\filebeat.yml'
    content = None
    scriptPath = ""
    with open(filebeatPath) as file:

        optionList = yaml.load(file, Loader=yaml.FullLoader)
        paths = []
        if (input["username"]) :
            optionList["output.elasticsearch"]["username"] = input["username"]
        else :
            optionList["output.elasticsearch"]["username"] = 'elastic'
        
        optionList["output.elasticsearch"]["password"] = input["password"]
        hostUrl = input["hosts"]
        if ':443' not in hostUrl :
            hostUrl = input["hosts"]+':443'
        optionList["output.elasticsearch"]["hosts"] = hostUrl
        optionList["output.elasticsearch"]["index"] = input["index"]
        if (input["paths"] != []) :
            extension = input["extension"]
            for path in input["paths"]:
                if '.' in extension :
                    paths.append(path+'\\*'+extension)
                else:
                    paths.append(path+'\\*.'+extension)
        optionList["filebeat.inputs"][0]["paths"]  = paths
        if (len(input["sample"]) != 1 and input["sample"] != ''):
            fieldsFormat = formatAnalyser(input["extension"], input["sample"], input["separator"])
            if fieldsFormat["headersNumber"] != 0 and fieldsFormat["headers"] != [] :
                fieldsSetUp = defFields()
                fieldsSetUp.defFieldsUi(fieldsFormat)
                mappingScript = fieldsSetUp.getPath()
                scriptPath = mappingScript;
                optionList["filebeat.inputs"][0]["processors"][0]["script"]['file'] = mappingScript
        else:
            fieldsFormat = formatAnalyser(input["extension"], "", input["separator"])
            if fieldsFormat["headersNumber"] == 0 and fieldsFormat["headers"] == [] :
                fieldsSetUp = defFields()
                fieldsSetUp.defFieldsUi(fieldsFormat)
                mappingScript = fieldsSetUp.getPath()
                scriptPath = mappingScript;
                optionList["filebeat.inputs"][0]["processors"][0]["script"]['file'] = mappingScript
        content = optionList
    
        file.close()

    with open(basePath+'/filebeat-8.3.1-windows-x86_64/filebeat.yml', 'w') as file:
        documents = yaml.dump(content, file, sort_keys=False)

    return scriptPath