# Léxicos

Descrição_Projeto: Americanas, Perfil Comprador, e fluxos compreendidos do cadastro na plataforma até visualização/compra/pagamento de produtos.

## Introdução

<div align="justify">

&emsp;&emsp;O Léxico é uma técnica que procura descrever os símbolos de uma linguagem. O principal objetivo dos engenheiros de requisitos é buscar frases e símbolos do domínio da aplicação. Cada um desse símbolo é descrito com uma noção e um impacto, sendo a noção relacionada com o símbolo e o impacto com a descrição do efeito do símbolo na aplicação ou do efeito de algo na aplicação sobre o símbolo. No presente artefato, iremos utilizar a técnica descrita para analisar o fluxo de cadastro de usuário até o pagamento de produtos na plataforma <a href="https://www.americanas.com.br/?spa=true">Americanas</a>.

</div>

## Metodologia

<div align="justify">

&emsp;&emsp;Os léxicos foram identificados a partir do uso do aplicativo e do site da plataforma. Na tabela 1 abaixo temos o exemplo de como os léxicos serão apresentados e descritos:

</div>

|     Léxico     |      Autor      |   Noção  |       Impacto       |   Sinônimo  |   Classificação     |
| :------------: | :-------------: | :------: | :-----------------: | :---------: | :-----------------: |
| Nome do Léxico | Autor do Léxico | Símbolos | Descrição do efeito | Sinônimo(s) | Verbo/Objeto/Estado |

<div style="text-align: center">
<p> Tabela 1: Modelo dos léxicos (Fonte: RIBEIRO, Bruno. 2023).</p>
</div>

<div align="justify">

&emsp;&emsp;As descrições seguem o princípio circular e o princípio do vocabulário mínimo. O princípio da circularidade torna cada extensão da descrição ou a conotação, referindo-se a outros símbolos da linguagem, ou seja, durante as descrições dos léxicos os mesmos serão ligados a outros léxicos. A parte não simbólica da descrição deve vir de um subconjunto reduzido de palavras com significado claro (vocabulário mínimo), no caso desse documento, um sinônimo do léxico apresentado.

</div>

</br>

## Descrição dos Léxicos

<div align="justify">

&emsp;&emsp;Abaixo estão as tabelas de 2 a 29 que representam os léxicos do aplicativo em análise. Tais léxicos foram divididos em três categorias sendo elas: Estado, Objeto e Verbo. Cada léxico de cada categoria recebeu uma forma de simbolização específica, sendo elas:

- LE -> Léxico de Estado
- LO -> Léxico de Objeto
- LV -> Léxico de Verbo

</div>

<div align="justify">

&emsp;&emsp;Léxico de Estado: Os léxicos de estado referem-se aos termos que descrevem as condições, estados ou propriedades do sistema ou dos elementos nele contidos.

</div>

<div align="justify">

&emsp;&emsp;Léxico de Objeto: Os léxicos de objeto englobam os termos que representam os elementos tangíveis ou virtuais do sistema com os quais os usuários interagem

</div>

<div align="justify">

&emsp;&emsp;Léxico de Verbo: Os léxicos de verbo consistem em palavras ou frases que descrevem ações que podem ser executadas pelos usuários ou pelo sistema.

</div>
</br>

- ## Estado

    - ### LE01 - <a id="Aceitação dos termos">Aceitação dos termos</a>

    |     Léxico     |      Autor      |   Noção  |       Impacto       |   Sinônimo  |   Classificação     |
    | :-------: | :-------: | :-----------: | :----------------: | :-------: | :--------: |
    | Aceitação dos termos | [Bruno Ribeiro](https://github.com/BrunoRiibeiro) | Estado de no qual é assinado um documento que estabelece as regras e condições de uso de determinado serviço executado por uma empresa ou organização. | Os termos de uso e políticas de privacidade consistem em contratos de adesão, firmados desde o acesso a um site até a compra de produtos. | Adesão | Estado |

    <div style="text-align: center">
    <p> Tabela 2: Léxico de aceitação dos termos (Fonte: RIBEIRO, Bruno. 2023).</p>
    </div>
    </br>

- ### LE02 - <a id="Características de produto">Características de produto</a>

    |     Léxico     |      Autor      |   Noção  |       Impacto       |   Sinônimo  |   Classificação     |
    | :-------: | :-------: | :-----------: | :----------------: | :-------: | :--------: |
    | Características de produto | [Bruno Ribeiro](https://github.com/BrunoRiibeiro) | Um produto é avaliado por suas características. | Compradores adquirem produtos baseados em suas características. | Aspecto, atributo | Estado |

    <div style="text-align: center">
    <p> Tabela 2: Léxico de características de produto (Fonte: RIBEIRO, Bruno. 2023).</p>
    </div>
    </br>    

- ## Objeto

    - ### LO01 - <a id="Avaliação">Avaliação</a>

    |     Léxico     |      Autor      |   Noção  |       Impacto       |   Sinônimo  |   Classificação     |
    | :------------: | :-------------: | :------: | :-----------------: | :---------: | :-----------------: |
    | Avaliação | [Bruno Ribeiro](https://github.com/BrunoRiibeiro) | Conjectura sobre condições, extensão, intensidade ou qualidade de um produto. | Um comprador visualiza a média das avaliações de um produto antes de adquiri-lo. | Consideração, julgamento, parecer, opinião, conjectura. | Objeto |

    <div style="text-align: center">
    <p> Tabela 3: Léxico de avaliação (Fonte: RIBEIRO, Bruno. 2023).</p>
    </div>
    </br>

   - ### LO02 - <a id="Carrinho">Carrinho</a>

    |     Léxico     |      Autor      |   Noção  |       Impacto       |   Sinônimo  |   Classificação     |
    | :------------: | :-------------: | :------: | :-----------------: | :---------: | :-----------------: |
    | Carrinho | [Bruno Martins](https://github.com/gitbmvb) | Interface que armazena os itens selecionados pelo usuário, além do valor total, descontos, etc. Simula a experiência familiar e comum de um carrinho de compras da vida real. | Oferecer ao usuário a sensação de controle sobre a adminstração dos produtos selecionados. | Cesta, sacola | Objeto |

    <div style="text-align: center">
    <p> Tabela 4: Léxico de carrinho (Fonte: MARTINS, Bruno. 2023).</p>
    </div>
    </br>

   - ### LO03 - <a id="Comentário">Comentário</a>

    |     Léxico     |      Autor      |   Noção  |       Impacto       |   Sinônimo  |   Classificação     |
    | :------------: | :-------------: | :------: | :-----------------: | :---------: | :-----------------: |
    | Comentário | [Bruno Martins](https://github.com/gitbmvb) | Elemento no qual o usuário registra as suas impressões e expectativas depois de haver comprado um produto. | Feedback dos usuários sobre a qualidade dos produtos oferecidos pela loja. | Avaliação, observação, consideração | Objeto |

    <div style="text-align: center">
    <p> Tabela 5: Léxico de comentário (Fonte: MARTINS, Bruno. 2023).</p>
    </div>
    </br>

   - ### LO04 - <a id="Menu">Menu</a>

    |     Léxico     |      Autor      |   Noção  |       Impacto       |   Sinônimo  |   Classificação     |
    | :------------: | :-------------: | :------: | :-----------------: | :---------: | :-----------------: |
    | Menu | [Bruno Martins](https://github.com/gitbmvb) | É um elemento gráfico que exibe de forma dinâmica os produtos segregados nos diversos departamentos da loja. | Facilitar a visualização agrupando os itens em departamentos semelhantes. | Navbar, sidebar | Objeto |

    <div style="text-align: center">
    <p> Tabela 6: Léxico de menu (Fonte: MARTINS, Bruno. 2023).</p>
    </div>
    </br>

    - ### LO05 - <a id="Nome Completo">Nome Completo</a>

    |     Léxico     |      Autor      |   Noção  |       Impacto       |   Sinônimo  |   Classificação     |
    | :------------: | :-------------: | :------: | :-----------------: | :---------: | :-----------------: |
    | Nome Completo | [Bruno Ribeiro](https://github.com/BrunoRiibeiro) | Uma forma de indentificação do usuário, um conjunto de nomes pelos quais um indivíduo é conhecido e que pode ser recitado. | O nome aparecerá como destinatário em todas as encomendas remetidas. | Nome Pessoal | Objeto |

    <div style="text-align: center">
    <p> Tabela 7: Léxico de nome completo (Fonte: RIBEIRO, Bruno. 2023).</p>
    </div>
    </br>

     - ### LO06 - <a id="Produto">Produto</a>

    |     Léxico     |      Autor      |   Noção  |       Impacto       |   Sinônimo  |   Classificação     |
    | :------------: | :-------------: | :------: | :-----------------: | :---------: | :-----------------: |
    | Produto | [Bruno Ribeiro](https://github.com/BrunoRiibeiro) | Aquilo que é produzido para venda no mercado. | Usuários buscam por produtos na aplicação, os quais dejesam comprar. | Mercadoria, mercancia, item, objeto, compra. | Objeto |

    <div style="text-align: center">
    <p> Tabela 8: Léxico de produto (Fonte: RIBEIRO, Bruno. 2023).</p>
    </div>
    </br>

   - ### LO07 - <a id="Search bar">Search bar</a>

    |     Léxico     |      Autor      |   Noção  |       Impacto       |   Sinônimo  |   Classificação     |
    | :------------: | :-------------: | :------: | :-----------------: | :---------: | :-----------------: |
    | Search bar | [Bruno Ribeiro](https://github.com/BrunoRiibeiro) | É um elemento gráfico de controle, usualmente uma caixa de texto em linha única, com a finalidade de busca na base de dados. | Buscar produtos desejados. | Search box, Search field | Objeto |

    <div style="text-align: center">
    <p> Tabela 9: Léxico de search bar (Fonte: RIBEIRO, Bruno. 2023).</p>
    </div>
    </br>

- ## Verbo

    - ### LV01 - <a id="Aumentar">Adicionar</a>

        |     Léxico     |      Autor      |   Noção  |       Impacto       |   Sinônimo  |   Classificação     |
        | :------------: | :-------------: | :------: | :-----------------: | :---------: | :-----------------: |
        | Adicionar | [Bruno Martins](https://github.com/gitbmvb) | O usuário quer aumentar a quantidade de elementos de um mesmo item presente no carrinho. | O usuário adquire mais itens, de acordo com a sua necessidade. | Aumentar, crescer, incrementar | Verbo |

        <div style="text-align: center">
        <p> Tabela 10: Léxico de adicionar (Fonte: MARTINS, Bruno. 2023).</p>
        </div>
        </br>

    - ### LV02 - <a id="Alterar">Alterar</a>

        |     Léxico     |      Autor      |   Noção  |       Impacto       |   Sinônimo  |   Classificação     |
        | :------------: | :-------------: | :------: | :-----------------: | :---------: | :-----------------: |
        | Alterar | [Bruno Martins](https://github.com/gitbmvb) | O usuário almeja alterar uma informação introduzida incorretamente. | Evitar o armazenamento no sistema de dados incorretos do usuário. | Mudar, trocar, substituir, atualizar | Verbo |

        <div style="text-align: center">
        <p> Tabela 11: Léxico de alterar (Fonte: MARTINS, Bruno. 2023).</p>
        </div>
        </br>

    - ### LV03 - <a id="Avaliar">Avaliar</a>

        |     Léxico     |      Autor      |   Noção  |       Impacto       |   Sinônimo  |   Classificação     |
        | :------------: | :-------------: | :------: | :-----------------: | :---------: | :-----------------: |
        | Avaliar | [Bruno Ribeiro](https://github.com/BrunoRiibeiro) | Quando um comprador redige um texto com a ideia de, conjecturar sobre ou determinar a qualidade, de um produto comprado anteriormente. | Produtos avaliados são mais quistos pelo público. | Qualificar | Verbo |

        <div style="text-align: center">
        <p> Tabela 12: Léxico de avaliar (Fonte: RIBEIRO, Bruno. 2023).</p>
        </div>
        </br>

    - ### LV04 - <a id="Cancelar">Cancelar</a>

        |     Léxico     |      Autor      |   Noção  |       Impacto       |   Sinônimo  |   Classificação     |
        | :------------: | :-------------: | :------: | :-----------------: | :---------: | :-----------------: |
        | Cancelar | [Bruno Martins](https://github.com/gitbmvb) | O usuário almeja interromper a compra e descartar as alterações feitas. | O usuário possui a liberdade de cancelar o ato de compra durante qualquer etapa da mesma. | Cessar, interromper, anular, desconsiderar, desfazer | Verbo |

        <div style="text-align: center">
        <p> Tabela 13: Léxico de cancelar (Fonte: MARTINS, Bruno. 2023).</p>
        </div>
        </br>

    - ### LV05 - <a id="Comprar">Comprar</a>

        |     Léxico     |      Autor      |   Noção  |       Impacto       |   Sinônimo  |   Classificação     |
        | :------------: | :-------------: | :------: | :-----------------: | :---------: | :-----------------: |
        | Comprar | [Bruno Ribeiro](https://github.com/BrunoRiibeiro) | Quando um usuário quer obter, mediante pagamento, a propriedade ou o uso de. | Produtos comprados saem do estoque para a casa do usuário o qual comprou. | Adquirir, mercar | Verbo |

        <div style="text-align: center">
        <p> Tabela 14: Léxico de comprar (Fonte: RIBEIRO, Bruno. 2023).</p>
        </div>
        </br>

    - ### LV06 - <a id="Confirmar">Confirmar</a>

    |     Léxico     |      Autor      |   Noção  |       Impacto       |   Sinônimo  |   Classificação     |
    | :------------: | :-------------: | :------: | :-----------------: | :---------: | :-----------------: |
    | Confirmar | [Bruno Ribeiro](https://github.com/BrunoRiibeiro) | Serie de checagens feitas durante o processo de cadastro para averiguar a correctude dos dados apresentados. | Dados quando confirmados condizem com dados apresentados anteriormente | Reconhecer, anuir | Verbo |

    <div style="text-align: center">
    <p> Tabela 15: Léxico de confirmar (Fonte: RIBEIRO, Bruno. 2023).</p>
    </div>
    </br>

    - ### LV07 - <a id="Deslogar">Deslogar</a>

        |     Léxico     |      Autor      |   Noção  |       Impacto       |   Sinônimo  |   Classificação     |
        | :------------: | :-------------: | :------: | :-----------------: | :---------: | :-----------------: |
        | Deslogar | [Bruno Martins](https://github.com/gitbmvb) | O usuário encerra sua sessão na conta pessoal do site. | O usuário mantém a segurança de seus dados pessoais.  | Sair, encerrar, terminar, finalizar | Verbo |

        <div style="text-align: center">
        <p> Tabela 16: Léxico de deslogar (Fonte: MARTINS, Bruno. 2023).</p>
        </div>
        </br>

    - ### LV08 - <a id="Diminuir">Diminuir</a>

        |     Léxico     |      Autor      |   Noção  |       Impacto       |   Sinônimo  |   Classificação     |
        | :------------: | :-------------: | :------: | :-----------------: | :---------: | :-----------------: |
        | Diminuir | [Bruno Martins](https://github.com/gitbmvb) | O usuário quer diminuir a quantidade de elementos de um mesmo item presente no carrinho. | O usuário adquire menos itens, de acordo com a sua necessidade. | Decrementar, diminuir, reduzir, economizar | Verbo |

        <div style="text-align: center">
        <p> Tabela 17: Léxico de diminuir (Fonte: MARTINS, Bruno. 2023).</p>
        </div>
        </br>

    - ### LV09 - <a id="Filtrar">Filtrar</a>

        |     Léxico     |      Autor      |   Noção  |       Impacto       |   Sinônimo  |   Classificação     |
        | :------------: | :-------------: | :------: | :-----------------: | :---------: | :-----------------: |
        | Filtrar | [Bruno Martins](https://github.com/gitbmvb) | O usuário filtra o resultado da busca de um produto pelo **menu** ou pela **search bar**. | O usuário pode encontrar produtos que se encaixam melhor às suas preferências. | Selecionar, especificar, restringir | Verbo |

        <div style="text-align: center">
        <p> Tabela 18: Léxico de filtrar (Fonte: MARTINS, Bruno. 2023).</p>
        </div>
        </br>

    - ### LV10 - <a id="Logar">Logar</a>

        |     Léxico     |      Autor      |   Noção  |       Impacto       |   Sinônimo  |   Classificação     |
        | :------------: | :-------------: | :------: | :-----------------: | :---------: | :-----------------: |
        | Logar | [Bruno Martins](https://github.com/gitbmvb) | O usuário entra na sua conta pessoal do site. | O usuário entra na sua conta e consegue ter acesso a maior recursos, como favoritar produtos e armazená-los no carrinho.  | Entrar, acessar, identificar-se | Verbo |

        <div style="text-align: center">
        <p> Tabela 19: Léxico de logar (Fonte: MARTINS, Bruno. 2023).</p>
        </div>
        </br>

    - ### LV11 - <a id="Perguntar">Perguntar</a>

        |     Léxico     |      Autor      |   Noção  |       Impacto       |   Sinônimo  |   Classificação     |
        | :------------: | :-------------: | :------: | :-----------------: | :---------: | :-----------------: |
        | Perguntar | [Bruno Martins](https://github.com/gitbmvb) | O usuário necessita esclarecer dúvidas técnicas sobre o produto que deseja adquirir. | O usuário fica ciente das qualidades do produto. | Indagar, requestar, duvidar | Verbo |

        <div style="text-align: center">
        <p> Tabela 20: Léxico de perguntar (Fonte: MARTINS, Bruno. 2023).</p>
        </div>
        </br>

    - ### LV12 - <a id="Rastrear">Rastrear</a>

        |     Léxico     |      Autor      |   Noção  |       Impacto       |   Sinônimo  |   Classificação     |
        | :------------: | :-------------: | :------: | :-----------------: | :---------: | :-----------------: |
        | Rastrear | [Bruno Martins](https://github.com/gitbmvb) | Depois de comprado o produto, o usuário pode rastrear sua movimentação. | O usuário está ciente da atual situação da demanda de entrega. | Monitorar, checar, analisar, informar-se | Verbo |

        <div style="text-align: center">
        <p> Tabela 21: Léxico de rastrear (Fonte: MARTINS, Bruno. 2023).</p>
        </div>
        </br>

## Conclusão

<div align="justify">

&emsp;&emsp;Assim, os léxicos identificados foram procurados e reconhecidos utilizando o aplicativo e site da plataforma, revelando elementos que podem ser interpretados como figuras de linguagem, que descrevem algo, ou como simples ícones. Com base nisso, podemos concluir que alguns desses léxicos possuem uma conexão rastreável com a atividade de brainstorm, estabelecendo uma ligação entre os artefatos e permitindo uma rastreabilidade ainda mais ampla entre eles.

</div>
</br>

## Referência

[1] SERRANO, Milene. Requisitos - Aula 10. Local: UnB-FGA, Gama, DF. Apresentação de Power Point. 35, color.

## Histórico de Versões

| Data | Versão | Descrição | Autor(es) | Data de revisão | Revisor(es) |
| :-: | :-: | :-: | :-: | :-: | :-: |
| 12/09/2023 | `1.0` | Criando o artefato | [Bruno Ribeiro](https://github.com/BrunoRiibeiro) e [Bruno Martins](https://github.com/gitbmvb) | 14/09/2023 | [Rafael Bosi](https://github.com/StrangeUnit28) |
