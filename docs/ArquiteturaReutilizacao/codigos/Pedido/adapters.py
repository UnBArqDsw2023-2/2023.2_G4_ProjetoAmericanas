from interfaces import InterfaceDeEnvioDeEmail

class AdapterEmail(InterfaceDeEnvioDeEmail):
    def __init__(self, adaptee):
        self.adaptee = adaptee
    
    def enviarEmailStatusPedido(self, usuario, status):
        self.adaptee.enviarEmailStatusPedido(usuario, status)
