import psutil

rawFilebeatServices = [x for x in psutil.win_service_iter() if x.name().lower() == 'filebeat']
filbeatServices = []
for rawService in rawFilebeatServices:
    svc = psutil.win_service_get(rawService.name())
    filbeatServices.append({"name":svc.name(),"state":svc.status()})
    print({"name":svc.name(),"state":svc.status()})