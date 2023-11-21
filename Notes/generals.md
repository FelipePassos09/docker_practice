# O que é Docker
Docker consiste de uma plataforma que encapsula, armazena e orquestra sistemas operacionais e/ou aplicações conteinerizadas, ou seja, cada contêiner contém uma imagem fiel, independente do sistema ou máquina na qual for executado.
O uso de conteinêres é, portanto, uma forma eficaz e segura de se desenvolver e executar aplicações de modo que não hajam problemas de incompatibilidade, versionamento de dependências ou outros relacionados.

## Diferenças entre VM's e Contêineres
A principal diferença entre VM's e Contêineres é o método de virtualização e orquestração empregado. Enquanto que na estrutura de VM utilizamos um hipervisor que, geralmente, é dependente de um sistema operacional e um hardware, os contêineres permitem a execução isolada de cada um além de compartilharem recursos de hardware, diferente das VM's, que reservam recursos em função da configuração realizada para cada uma.
Os contêineres, portanto, permitem uma eecução muito mais eficiente, rápida e segura, além de serem mais estáveis e com tempos de carga muito reduzidos em comparação com máquinas virtuais.

## Como o Docker Funciona
Como observamos acima, o docker trabalha com contêineres que consistem em uma imagem fiel e estática de uma determinada aplicação. Por exemplo, caso tenhamos uma aplicação rodando em um linux, com a versão 3.10 do python, algumas bibliotecas e um banco de dados, ao criarmos a imagem, todas essas variáveis e versões serão replicadas para o nosso contêiner, portanto, ao ser executado em outro servidor a imagem irá gerar o mesmo resultado, indepente do que exite previamente no servidor de destino.

## Docker Hub
Trata-se de um repositório remoto, tal qual o github, onde é possível armazenar, backupear e compartilhar imagens de conteinêres entre um ou mais servidores.

## Executando um conteiner em modo interativo
Para executarmos um conteiner em modo interativo, ou seja, sem a necessidade de baixar todos os recursos e manter este sendo executado indefinidamente, podemos utilizar o comando docker run -it <distro-name> neste caso ele irá executar uma instância do sistema operacional selecionado em tempo tempo real sem a necessidade de baixarmos todos os recursos deste, isso é útil em casos onde precisamos simular ou mesmo rodar alguma aplicação dentro deste conteiner e, caso ele não receba nenhuma interação, ele automaticamente se incerrará.
