# Moscow

## Introdução

<div style="text-align:justify">Após a elicitação de diversos requisitos pelo método de brainstorm se faz necessário o uso de meios para priorizar tais requisitos, de maneira a intender o grau de importância de cada um deles.</div> 

<div style="text-align:justify">Dessa forma, nessa seção a técnica utilizada para a priorização dos requisitos é o Moscow.</div>

## Metodologia

<div style="text-align:justify">O método MoSCoW é uma técnica de priorização de requisitos que tem como objetivo ajudar o time de desenvolvimento a tomar decisões de forma mais eficiente. A estrutura MoSCoW é baseada em quatro categorias:</div>

 - **M** -> Must-Have (Deve ter)
 - **S** -> Should (Deveria ter)
 - **C** -> Could-Have (Poderia ter)
 - **W** -> Would/Want/Won't-Have (Não precisa ter)


### Must-Have

<div style="text-align:justify">A categoria Must-Have representa as tarefas indispensáveis para a realização do projeto, e que precisam ser priorizadas. Essas demandas são de alto impacto e agregam valor ao produto, e caso não sejam atendidas, podem prejudicar a experiência do cliente. As atividades Must-Have são as mais urgentes e devem ser resolvidas prioritariamente pelo time.</div>


### Should-Have

<div style="text-align:justify">A categoria Should-Have representa as tarefas importantes para a realização do projeto, mas que não são fundamentais como as atividades Must-Have.</div>


### Could-Have

<div style="text-align:justify">A categoria Could-Have representa as tarefas menos importantes que as atividades Should-Have. Esses requisitos agregam valor ao projeto, mas sua ausência não impacta significativamente a realização do projeto.</div>


### Would/Want/Won't

<div style="text-align:justify">Por fim, a categoria Would/Want/Won't-Have representa as tarefas que não possuem importância significativa para o projeto. A presença ou ausência desses requisitos não tem impacto na conclusão satisfatória do projeto.</div>


<div style="text-align:justify">O objetivo da técnica MoSCoW é ajudar o time de desenvolvimento a alinhar os stakeholders sobre o que deve ser feito, de acordo com a ordem de importância dos elementos considerados. Ao utilizar essa técnica, o time de desenvolvimento consegue identificar o grau de prioridade das tarefas em um projeto e concentrar esforços nas demandas mais importantes.</div>

## Requisitos 

<div style="text-align:justify">As Tabelas de 1 a 4 a seguir contém a priorização dos Requisitos elicitados.</div>

### Em relação ao fluxo de cadastro

| id | Descrição | Prioridade |
| :--: | :------:| :--------: |
| BS01 | A plataforma deve armazenar dados do usuário | Must |
| BS02 | A plataforma deve exigir o nome completo do usuário | Must |
| BS03 | A plataforma deve exigir o email do usuário | Must |
| BS04 | A plataforma deve exigir que o usuário confirme o email | Must |
| BS05 | A plataforma deve exigir uma senha e que o usuário a confirme | Must |
| BS06 | A plataforma deve exigir que a senha possua mais de 8 caracteres | Must |
| BS07 | A plataforma deve exigir o CPF do usuário | Must |
| BS08 | A plataforma deve exigir a data de nascimento do usuário | Should |
| BS09 | A plataforma deve diminuir o número de dados exigidos do usuário | Should |
| BS10 | A plataforma deve exigir que o usuário defina se deseja receber promoções por email | Could |
| BS11 | A plataforma deve exigir o número de telefone do usuário | Won't |
| BS12 | A plataformaa deve exigir o CEP do usuário | Won't |

<div style="text-align: center">
<p> Tabela 1: Priorização do fluxo de cadastro (Fonte: RIBEIRO, Bruno. 2023).</p>
</div>

### Em relação ao fluxo de visualização do produto

| id | Descrição | Prioridade |
| :--: | :-----: | :--------: |
| BS13 | A plataforma deve apresentar uma search bar | Must |
| BS14 | A plataforma deve exibir um catálogo de produtos | Must |
| BS15 | A plataforma deve apresentar filtros | Must |
| BS16 | A plataforma deve apresentar uma página para cada produto | Must |
| BS17 | A plataforma deve exibir uma ficha técnica para cada produto | Must |
| BS18 | A plataforma deve apresentar fotos de cada produto | Must |
| BS19 | A plataforma deve permitir que o produto possa ser avaliado | Must |
| BS20 | A plataforma deve apresentar uma área destinada a dúvidas sobre cada produto | Must |
| BS21 | A plataforma deve exibir um botão de compra | Must |
| BS22 | A plataforma deve apresentar uma lista de sugestões vinculada a search bar | Should |
| BS23 | A plataforma deve exibir a opção de visualizar o catálogo em lista ou em cards | Should |
| BS24 | A plataforma deve conseguir ordenar os produtos | Should |
| BS25 | A plataforma deve apresentar uma área destinada a comentários em relação a cada produto | Should |
| BS26 | A plataforma deve exibir itens semelhantes a cada produto | Should |
| BS27 | A plataforma deve apresentar a opção de filtrar por marca | Would |

<div style="text-align: center">
<p> Tabela 2: Priorização do fluxo de visualização do produto (Fonte: RIBEIRO, Bruno. 2023).</p>
</div>

### Em relação ao fluxo de compra do produto

| id | Descrição | Prioridade |
| :--: | :-----: | :--------: |
| BS28 | A plataforma deve exibir um carrinho de compras | Must |
| BS29 | A plataforma deve permitir que o usuário defina a transportadora | Must |
| BS30 | A plataforma deve permitir que o usuário remova itens do carrinho | Must |
| BS31 | A plataforma deve incluir o frete no valor do produto | Must |
| BS32 | A plataforma deve confirmar os dados do usuário | Must |
| BS33 | A plataforma deve exigir o endereço do usuário | Must |
| BS34 | A plataforma deve detalhar o preço do produto | Must |
| BS35 | A plataforma deve fornecer a possibilidade de adicionar mais de um item ao carrinho | Must |
| BS36 | A plataforma deve permitir o cancelamento da compra | Must |
| BS37 | A plataforma deve permitir que o usuário adicione um cupom | Should |

<div style="text-align: center">
<p> Tabela 3: Priorização do fluxo de compra do produto (Fonte: RIBEIRO, Bruno. 2023).</p>
</div>

### Em relação ao fluxo de pagamento do produto

| id | Descrição | Prioridade |
| :--: | :-----: | :--------: |
| BS38 | A plataforma deve exigir os dados do cartão do usuário (CVV, CPF, Validade e Número) | Must |
| BS39 | A plataforma deve ter a possibilidade de emitir boleto | Must |
| BS40 | A plataforma deve conseguir gerar chave ou QRcode de pagamento por Pix | Must |
| BS41 | A plataforma deve apresentar a possibilidade de TED e DOC | Must |
| BS42 | A plataforma deve emitir nota fiscal por email | Must |
| BS43 | A plataforma deve oferecer a opção de parcelar | Must |
| BS44 | A plataforma deve exigir que o usuário selecione uma opção de pagamento | Must |
| BS45 | A plataforma deve fornecer a opção de imprimir o boleto | Must |
| BS46 | A plataforma deve oferecer a opção de vincular o CPF ou o CNPJ à nota fiscal | Must |
| BS47 | A plataforma deve confirmar o pagamento por email | Must |

<div style="text-align: center">
<p> Tabela 4: Priorização do fluxo de pagamento do produto (Fonte: RIBEIRO, Bruno. 2023).</p>
</div>

## Referências

1. Wiegers, K. and Beatty, J., 2013. Software requirements. Pearson Education.

## Histórico de versão

| Versão | Data de alteração  | Alteração |  Responsável    | Revisor     |  Data de revisão  |
| :----: | :---------------: | :-------------: | :-----------: | :-----------: | :-----------: |
| `1.0` | 15/09/2023 | Criação do documento | [Bruno Ribeiro](https://github.com/BrunoRiibeiro) e [Igor Penha](https://github.com/igorpenhaa) | [Rafael Bosi](https://github.com/StrangeUnit28) | 15/09/2023 |
