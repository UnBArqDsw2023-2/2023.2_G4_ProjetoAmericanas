from abc import ABC, abstractmethod

class Observador:
    @abstractmethod
    def update(self):
        pass

class InterfaceDeEnvioDeEmail(ABC):
    @abstractmethod
    def enviarEmailStatusPedido(self, usuario, status):
        pass