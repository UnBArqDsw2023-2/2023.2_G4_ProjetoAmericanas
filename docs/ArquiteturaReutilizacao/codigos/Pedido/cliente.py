from interfaces import InterfaceDeEnvioDeEmail
from models import Usuario, Pedido

def main():
    status = "Em andamento"

    usuario = Usuario(
        nome="Bernardo",
        email="bernardo@email.com",
        senha="senha123",
        cpf="123.456.789-01",
        dataNascimento="01/01/2000",
        endereco="Rua Exemplo, 123",
    )

    pedido = Pedido(
        transportadora="Transportadora Exemplo",
        valorTotal=100.0,
        cupom="DESCONTO123",
        remetente="Remetente Exemplo",
        destinatario="Destinatario Exemplo"
    )

    pedido.adicionarObservador(usuario)
    usuario.fazerPedido(pedido)
    pedido.definirStatus(status)


if __name__ == "__main__":
    main()
