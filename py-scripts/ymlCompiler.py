import sys, yaml, os

def ymlComipler(input):
    basePath = os.getcwd().replace('py-scripts','')
    filebeatPath = basePath+'\\filebeat.yml'
    content = None

    with open(filebeatPath) as file:

        optionList = yaml.load(file, Loader=yaml.FullLoader)
        paths = []
        if (input["username"]) :
            optionList["output.elasticsearch"]["username"] = input["username"]
        else :
            optionList["output.elasticsearch"]["username"] = 'elastic'
        
        optionList["output.elasticsearch"]["password"] = input["password"]
        optionList["output.elasticsearch"]["hosts"] = input["hosts"]
        optionList["output.elasticsearch"]["index"] = input["index"]
        if (input["paths"] != []) :
            extension = input["extension"]
            for path in input["paths"]:
                paths.append(path+'\\*'+extension)
        else :
            paths = [os.getcwd().replace('py-scripts','Logs\\input\\*.txt')]
        optionList["filebeat.inputs"][0]["paths"]  = paths
        content = optionList

        file.close()

    with open(basePath+'/filebeat-8.3.1-windows-x86_64/filebeat.yml', 'w') as file:
        documents = yaml.dump(content, file, sort_keys=False)