class serviceCard:

    def __init__(self, serviceName):
        self.name = serviceName
        rawFilebeatServices = [x for x in psutil.win_service_iter() if x.name().lower() == service_name]
        filbeatServices = []
        for rawService in rawFilebeatServices:
            svc = psutil.win_service_get(rawService.name())
            filbeatServices.append({"name":svc.name(),"state":svc.status()})

    def getelasticUrl(self):
        return self._protected_elasticUrl

    def getelasticUsername(self):
        return self._protected_elasticUsername