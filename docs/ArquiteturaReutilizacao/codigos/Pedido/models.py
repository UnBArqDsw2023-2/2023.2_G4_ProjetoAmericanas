from interfaces import Observador
from services import ServicoDeEmail

class Usuario(Observador):
    def __init__(self, nome, email, senha, cpf, dataNascimento, endereco):
        self._nome = nome
        self._email = email
        self._senha = senha
        self._cpf = cpf
        self._dataNascimento = dataNascimento
        self._endereco = endereco
        self._pedido = None
        self._adaptadorEmail = ServicoDeEmail()

    def atualizarStatus(self):
         if self._pedido:
            print(f"Usuário {self._nome}: Status do pedido atualizado para {self._pedido._status}")
            self._adaptadorEmail.enviarEmailStatusPedido(self._nome, self._pedido._status)

    def fazerPedido(self, pedido):
        self._pedido = pedido
    
    def confirmaEmail(self):
        pass

    def confirmarSenha(self):
        pass
    
    def validarCPF(self):
        pass

    def cadastrar(self):
        pass

    def fazerLogin(self):
        pass

    def selecionarProduto(self):
        pass

    def verPerfil(self):
        pass

    def atualizarPerfil(self):
        pass

    def procurarProduto(self):
        pass


class Pedido:
    def __init__(self, transportadora, valorTotal, cupom, remetente, destinatario):
        self._transportadora = transportadora
        self._valorTotal = valorTotal
        self._cupom = cupom
        self._remetente = remetente
        self._destinatario = destinatario
        self._status = "Novo"
        self._observadores = []

    def adicionarObservador(self, observer):
        self._observadores.append(observer)

    def removerObservardor(self, observer):
        self._observadores.remove(observer)

    def notificarObservadores(self):
        for observer in self._observadores:
            observer.atualizarStatus()

    def definirStatus(self, status):
        self._status = status
        self.notificarObservadores()
    
    def confirmarPedido(self):
        pass
    def cancelarPedido(self):
        pass
    def detalharPedido(self):
        pass
    def calcularTotal(self):
        pass
    def adicionarCupom(self):
        pass
    def confirmarDadosUsuario(self):
        pass
