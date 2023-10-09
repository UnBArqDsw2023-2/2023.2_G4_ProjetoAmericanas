<div class="body">
  
# Diagrama de pacotes

## 1. Introdução

<div align="justify">

&emsp;&emsp; Conforme a notação UML de diagramas estáticos [1], um diagrama de pacotes constitui uma representação estrutural prescrita pela UML, 
cuja finalidade é a descrição dos agrupamentos lógicos que compõem o sistema, destacando, assim, as interdependências existentes entre eles. 
Este tipo de diagrama é frequentemente empregado como meio para representar a estrutura arquitetônica de um sistema, evidenciando a organização de suas classes. 
Cabe mencionar que um pacote, neste contexto, corresponde a uma unidade de agregação que engloba elementos relacionados no âmbito da UML, incluindo, 
mas não se limitando a, diagramas, documentos, classes e, eventualmente, outros pacotes.

## 2. Participantes

Os participantes que participaram do desenvolvimento desse artefato foram:

- Bernado Pissutti
- Bruno Ribeiro
- Bruno Bomfim
- Igor Penha
- Marcos Souza

## 3. Metodologia

O artefato foi desenvolvido em conjunto utilizando a ferramenta Microsoft Teams para reunião e para modelagem a ferramenta LucidChart. 
Para o desenvolvimento em conjunto, um membro do grupo compartilhou a tela da ferramenta de modelagem, e com o auxílio do restante do grupo, 
que também modificava o diagrama online, as ideias e possíveis modelagens foram discutidas. E, assim, foi evoluindo o artefatp ao longo da sprint


## 4. Artefato

&emsp;&emsp;A equipe se reuniu e, juntamente, começou a construir o artefato que seria o diagrama de pacote, inicialmente, a gente tentou modelar quais seriam os tipos de organização de pastas que estaríamos buscando, com uma dica que foi dada pela professora, dividimos em dois grandes modelos principais, Client e Application, o Client é a camada que mostra como o usuário se conecta com a aplicação, no caso, ou por web ou por mobile. Já o módulo Application, foi dividido nos modelos frontend, que continha os pacotes necessários para a criação de telas e manuseio básico de dados, backend, que continha as suas camadas e a conexão externa com o banco de dados, ainda sem modelagem.

### 4.1 Legenda

<div style="display: center; align-items: center;">.
  <img src="../../images/t2-Modelagem/legendaDiagramaDePacote.png" alt="legenda com a descrição dos elementos  presentes no artefato diagrama de pacote" style="margin-right: 20px;"/>
  <div style="flex-grow: 1;">
    <h6 style="text-align: flex;">
    Figura 1 : Legenda do Diagrama de Pacotes
    </h6>
  </div>
</div>

### 4.2 Primeira versão do diagrama

<div style="display: center; align-items: center;">
  <img src="../../images/t2-Modelagem/DiagramaPacotes.jpg" alt="Diagrama de pacotes" style="margin-right: 20px;"/>
  <div style="flex-grow: 1;">
    <h6 style="text-align: flex;">
    Figura 2 : Diagrama de Pacotes V1 (Fonte: Bernado Pissutti, Bruno Ribeiro, Bruno Bomfim, Igor Penha e Marcos Souza, 2023).
    </h6>
  </div>
</div>


## 5. Estrutura do diagrama

&emsp;&emsp; A estrtura do diagrama foi dividida em camadas que irão ser explicadas a seguir:

### Front-End

- Pages: Esta camada representa as páginas ou telas da interface do usuário. Aqui, são definidas as diferentes telas que os usuários podem interagir no sistema.

- Assets: Nesta camada, são armazenados recursos gráficos, como imagens, ícones e arquivos de estilo, que são utilizados na interface do usuário.

- Services: Os serviços são responsáveis por realizar solicitações e interações com o back-end. Eles lidam com a comunicação entre o front-end e o back-end do sistema.

- Components: Os componentes são unidades reutilizáveis de código que compõem as páginas. Eles podem incluir elementos de interface, como botões, formulários e caixas de diálogo.

- Tests: Nesta camada, são realizados testes de unidade e integração para garantir a qualidade e o funcionamento adequado do front-end.



### Back-End

- View: A camada de visualização é responsável por apresentar os dados aos usuários e receber suas interações. Ela lida com a renderização das páginas e a comunicação com o front-end.

- Controller: Os controladores são responsáveis por receber as solicitações dos clientes, processá-las e coordenar ações no sistema. Eles atuam como intermediários entre a visualização e a camada de negócios.

- Business: A camada de negócios contém a lógica de negócios do sistema. Ela processa as informações, realiza cálculos e toma decisões com base nas solicitações dos clientes e nas regras de negócios.
  
### Database

A camada de banco de dados armazena e gerencia os dados do sistema. Ela inclui tabelas, esquemas e procedimentos de acesso aos dados. Essa camada é fundamental para a persistência e recuperação das informações utilizadas pelo sistema.

## 6. Gravação da reunião

<iframe width="1000vw" height="650vh" src="https://www.youtube.com/embed/_w_TTuf8hv8" title="reunião de execução do diagrama de pacotes" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe>
<div align="center">
<p> <b>Vídeo 1</b>: gravação da execução do diagrama de pacotes (Fonte: Grupo. 2023).</p>
</div>

## 7. Conclusão

Em conclusão, o diagrama de pacotes apresentado neste artefato representa uma visão estrutural importante do sistema em desenvolvimento. Ele oferece uma representação clara das diferentes camadas e módulos que compõem o sistema, destacando as interdependências entre eles. A colaboração da equipe, utilizando ferramentas como o Microsoft Teams e o LucidChart, foi essencial para a construção e evolução do diagrama ao longo da sprint.

O diagrama de pacotes, dividido em categorias como Front-End, Back-End e Database, fornece uma visão geral da arquitetura do sistema, facilitando a compreensão de como os diferentes componentes se encaixam e se relacionam.

Além disso, a gravação da reunião disponibilizada no vídeo 1 permite que os membros da equipe revisem as discussões e decisões tomadas durante o processo de modelagem do diagrama de pacotes, garantindo um registro valioso das deliberações.

No geral, este artefato desempenha um papel fundamental na comunicação e documentação da estrutura arquitetônica do sistema, contribuindo para uma melhor compreensão por parte de todos os envolvidos no projeto. É um recurso valioso para orientar o desenvolvimento futuro e a manutenção do sistema.

</div>

## Referências

- [1] https://www.uml-diagrams.org/package-diagrams-overview.html;
- [2] https://react.dev/reference/react

## Histórico de Versão

|  Versão  |   Data da alteração  |   Alteração  |  Responsável  |  Revisor  | Data de revisão |
| :--------: | :--------------------: | :-----------: | :--------------: | :--------: | :-----------------: |
|    `1.0`    |    25/09/2023   |  Criando documento  |  [Igor Penha](https://github.com/igorpenhaa)   |   |  |
|    `1.1`    |    29/09/2023   |  Adição de legenda do artefato  |  [Bernardo Pissutti](https://github.com/berssutti)   |   |  |
|    `1.3`    |    03/09/2023   |  Adição do diagrama e melhorando o escopo |  [Igor Penha](https://github.com/igorpenhaa)   |   |  |
|    `1.4`    |    08/09/2023   |  Adição da conclusão e correções finais para entrega. |  [Bruno Ribeiro](https://github.com/BrunoRiibeiro) | [Igor Penha](https://github.com/igorpenhaa) | 08/09/2023 |

</div>
