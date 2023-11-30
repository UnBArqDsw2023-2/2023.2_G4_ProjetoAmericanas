## Visão de Dados

## MER

#### Entidades

* Usuario
* Pedido
* Produto
* Pagamento
* Endereco
* Cartao

#### Atributos

* Usuario: <span style="text-decoration: underline;">idUsuario</span>, nome, email, senha, telefone, dataNascimento, genero
* Pedido: <span style="text-decoration: underline;">idPedido</span>, transportadora, valor, status
* Produto: <span style="text-decoration: underline;">idProduto</span>, nome, avaliacao, marca, qtdEstoque
* Pagamento: <span style="text-decoration: underline;">idPagamento</span>, parcelas, formaPagamento
* Endereco: <span style="text-decoration: underline;">idEndereco</span>, numero, complemento, bairro, cidade, estado, cep
Cartao: <span style="text-decoration: underline;">idCartao</span>, nome, cvv, dataValidade, numero


#### Relacionamentos

**Usuário contém Cartão**
- Um Usuário pode possuir nenhum ou vários cartões (1,n). Um cartão pode ser contido por no mínimo um usuário e no máximo um (1,1);

**Usuário contém Endereço**
- Um usuário pode conter nenhum ou vários endereços  (0,n). Um endereço pode ser contido por no mínimo um usuário, e no máximo um.

**Usuário possui Pedido**
- Um Usuário pode possuir nenhum ou vários pedido(0,n). Um Pedido pode ser possuido por no minimo um Usuário, e no máximo um (1,1);

**Pedido possui Pagamento**
- Um Pedido pode possuir no mínimo um pagamento, e no máximo um (1,1). Um pagamento pode ser possuido por  no mínimo um pedido, e no máximo um (1,1);

**Pedido possui Produto**

- Um pedido possui no minimo um Produto ou vários Produtos (1,n). Um Produto pode ser possuido por nenhum ou vários pedidos (0,n).

## DER

![](../images/derAmericanas.png)

<div style="text-align: center">
<p> Diagrama Entidade-Relacionamento (Elaborado por: Vitor Manoel & Gustavo Barbosa. 2023).</p>
</div>