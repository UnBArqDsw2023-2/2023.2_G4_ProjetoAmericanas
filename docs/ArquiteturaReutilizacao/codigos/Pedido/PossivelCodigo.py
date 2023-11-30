from abc import ABC, abstractmethod
from typing import List

# Classe Observer abstrata
class Observer(ABC):
    @abstractmethod
    def update(self):
        pass

# Classe Observable (Subject)
class Pedido:
    def __init__(self):
        self._observers = []
        self._status = "Novo"  # Status inicial

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update()

    def set_status(self, status):
        self._status = status
        self.notify_observers()

# Classe ConcreteObserver
class Usuario(Observer):
    def __init__(self, nome, carrinho_de_compras, email_adapter):
        self._nome = nome
        self._carrinho_de_compras = carrinho_de_compras
        self._pedido = None
        self._email_adapter = email_adapter

    def update(self):
        if self._pedido:
            print(f"Usuário {self._nome}: Status do pedido atualizado para {self._pedido._status}")
            self._email_adapter.send_email(self._nome, self._pedido._status)

    def realizar_pedido(self, pedido):
        self._pedido = pedido

# CarrinhoDeCompras é uma composição de Pedido
class CarrinhoDeCompras:
    def __init__(self):
        self._pedidos = []

    def adicionar_pedido(self, pedido):
        self._pedidos.append(pedido)

    def remover_pedido(self, pedido):
        self._pedidos.remove(pedido)

class EmailAdapter(ABC):
    @abstractmethod
    def send_email(self, user_name, status):
        pass

class FictitiousEmailAdapter(EmailAdapter):
    def send_email(self, user_name, status):
        print(f"Enviando e-mail para {user_name}: Status do pedido atualizado para {status}")

if __name__ == "__main__":
    pedido1 = Pedido()
    pedido2 = Pedido()

    carrinho = CarrinhoDeCompras()
    carrinho.adicionar_pedido(pedido1)
    carrinho.adicionar_pedido(pedido2)

    email_adapter = FictitiousEmailAdapter()

    usuario1 = Usuario("Bernardo", carrinho, email_adapter)
    usuario2 = Usuario("OutroUsuario", carrinho, email_adapter)

    # Adicionando observadores aos pedidos
    pedido1.add_observer(usuario1)
    pedido2.add_observer(usuario2)

    # Mudando o status do pedido
    pedido1.set_status("Em andamento")
    pedido2.set_status("Concluído")
