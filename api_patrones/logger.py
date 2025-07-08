class LoggerSingleton:
    _instance = None
    logs = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def registrar(self, mensaje):
        self.logs.append(mensaje)