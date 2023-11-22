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

# Conteinerização
O princípio central de um conteiner é encapsular uma aplicação e toda a estrutura que irá servir à ela como, por exemplo, o sistema operacional, as variaveis de ambiente, bibliotecas utilizadas, etc. Para podermos gerar o contêiner, portanto, precisamos criar uma imagem do mesmo e, para isso, usamos o Dockerfile.

## Dockerfile - A alma do Docker
O Dockerfile consiste de um arquivo, sem extensão, que reúne todas as configurações do contêiner pretendido, nele damos as instruções que irão ser responsáveis por criar e configurar nosso conteiner de forma correta. Para que ele consiga fazer isso utilizamos instruções de código nas quais informamos o ambiente, o tipo de aplicação, o sistema operacional, as variáveis, instruções de execução, usuário que irá executar a aplicação, diretórios de trabalho, etc.

As instruçõe que não podem faltar no Dockerfile são:
* FROM -> é responsável por indicar o tipo de aplicação (plataforma) e o sistema operacional, por exemplo: python:alpine, node:ubuntu, dotnet:centos
* COPY / ADD -> indica os arquivos que serão enviados para o contêiner, desse modo podemos evitar subir, por exemplo, diretórios de debug, testes ou arquivos irrelevantes para a aplicação.
* WORKDIR -> indica o nome do diretório de trabalho, ou seja, o diretório padrão onde todos as instruções irão ser baseadas.
* CMD / ENTRYPOINT -> lista de instruções (baseadas no sistema operacional escolhido em FROM) que serão executadas quando o contêiner for iniciado.
* RUN -> executa a aplicação.
* ENV -> recebe a lista de dependências que o ambiente necessita para executar a aplicação.
* EXPOSE -> seta a porta por onde a aplicação será acessada.
* USER -> identifica o usuário que irá executar a aplicação.
  
Documentação completa em https://docs.docker.com/engine/reference/builder/#dockerfile-reference.

## Criando o Dockerfile
### FROM - Escolhendo a plataforma e SO
Ao criarmos um contêiner a primeira coisa que precisamos considerar é a plataforma em que a nossa aplicação será executada e qual o sistema operacional que iremos utilizar, isso devido o docker possui uma tecnologia que permite criarmos o contêiner já com a plataforma definida. A escolha do sistema operacional também é importante pois definirá o quão robusto e, consequentemente, pesado será o SO incluído no contêiner.

### ADD e COPY - Listando os arquivos que serão carregados para o nosso contêiner.
Há uma diferença entre essas instruções onde o COPY irá alcançar apenas os arquivos locais enquanto que o ADD consegue alcançar os arquivos remotos a partir de uma url ou arquivo compactado.

### RUN - Rodando instruções durante o build
A instrução RUN permite que, ao ser realizada a build do contêiner, consigamos já instalar dependências ou executar instruções diretamente nessa etapa, por exemplo, se nossa aplicação pede uma versão espcífica do python ou, para executar a aplicação precisamos ter o pandas instalado podemos inserir estes comandos diretamente no processo de build:

    FROM ubuntu:latest
    WORKDIR /app
    COPY . .
    RUN apt-get update && apt-get install -y locales
    RUN apt-get install -y python3 python3-pip && pip install --upgrade pip && pip install -r requirements.txt

### ENV - Setando variáveis de ambiente
O ENV é detinado à configurarmos váriaveis de ambiente no nosso contêiner, por exemplo, se a aplicação que utilizamos depende de uma aplicação externa acessada por uma URL podemos inserir essa url no ENV que ela será, automaticamente, incluída no path do nosso ambiente.

### EXPOSE - Configurando o acesso à aplicação ou recurso
Pelo EXPOSE configuramos a porta que será utilizada para acessarmos a aplicação. Como vimos o contêiner se comporta de modo similar à uma VM e, portanto, para que possamos acessar a aplicação externamente ao contêiner precisamos definir por qual porta essa comunicação será realizada.

Digamos, então, que eu tenha um contêiner dedicado ao banco de dados da nossa aplicação e esse contêiner e DB estão configurados para utilizarem a porta 3060, ao criarmos o contêiner inserimos no Dockerfile o EXPOSE 3060, o que fará com que essa porta esteja acessível externamente.
    
    Atenção, o EXPOSE configura as portas no contêiner, para que um usuário externo ao servidor que hospeda o contêiner é necessário criar uma estrutura de endereçamento (NAT) que mapeie a porta que será utilizada para acessar o servidor e apontar essa porta para a porta de acesso do contêiner.

### CMD - Executando a aplicação
De forma semelhante ao RUN, o CMD executa uma instrução definida no dockerfile, porém o RUN executa essas instruções na criação do contêiner enquanto que o CMD executa essas instruções na execução / abertura do contêiner. É importante sabermos essa diferença pois se inserirmos uma instrução para abrir a nossa aplicação ou executar alguma rotina específica no nosso contêiner sempre que ele for aberto, caso coloquemos essa instrução em RUN duas coisas podem acontecer: 

1. Ocorrerá um erro durante o processo de build e a imagem não será criada.
2. Nenhum erro irá ocorrer mas nossa aplicação não será iniciada automaticamente ao executarmos o contêiner.

É importante diferenciarmos essas duas estruturas pois o uso incorreto delas pode gerar diversos problemas de orquestração e, mesmo, de performance da aplicação.

Exemplo:

    FROM ubuntu:latest
    WORKDIR /app
    COPY . .
    RUN apt-get update && apt-get install -y locales
    RUN apt-get install -y python3 python3-pip && pip install --upgrade pip && pip install -r requirements.txt
    CMD python3 -u app.py

Vemos que a última linha contém a instrução python3 -u app.py, isso significa que, como ela é uma instrução CMD, sempre que o nosso contêiner for executado ela irá executar o arquivo app.py utilizando o python3. E garantimos que o python3 está instalado pelas instruções RUN anteriores que incluíram a instalação tanto do python3 quanto das dependências da aplicação através da instalação das bibliotecas listadas no requirements.txt.

### USER - Definido usuários
Pelo USER configuramos os usário que irá excutar a aplicação. É importante salientar  que, caso não utilizemos essa estratégia a aplicação será executada sempre pleo usuário root, ou seja, pelo administrador global desse contêiner. É, portanto, essencial realizarmos sempre a criação do(s) usuário(s) que são responsáveis por executar a aplicação.

Para fazermos essa lógica temos que obseravar que o Dockerfile é executado de cima para baixo e da esquerda para a direita. Ou seja, para garantirmos que tudo será executado pelo usuário desejado, precisamos passar a instrução USER apenas quando nenhuma ação dependente do root for necessária.

Exemplo:

    FROM ubuntu:latest
    WORKDIR /app
    COPY . .
    RUN addgroup dev && adduser -S -G application_user dev
    RUN apt-get update && apt-get install -y locales
    RUN apt-get install -y python3 python3-pip && pip install --upgrade pip && pip install -r requirements.txt
    USER application_user
    CMD python3 -u app.py

No Dockerfile acime observe que, na terceira linha temos a instrução para criar o grupo dev e o usuário applicatio_user, já vinculando o usuário ao grupo recém criado. A partir de então seguimos com as ações de RUN instalando depêndências e atualizando o SO. Apenas antes do CMD, ou seja, quando a aplicação for ser executada, inserimos o USER, portanto, neste momento, a aplicação será executada pelo application_user, e não pelo root.

    Atenção: ao orquestramos a criação e atribuição de usuário precisamos sempre nos atentar para que o usuário no qual está posicionado o file possui as permissões necessárias para realizar as operações, caso ele não possua isso pode ocasionar erros ou mesmo falha da aplicação.

### Otimização - Tornando a nossa aplicação mais rápida
Bem, o processo mais demorado é a criação da imagem, muitas vezes devido à instalação de dependências. Para evitarmos que as dependências sejam, sempre, instaladas durante o build do nosso projeto é importante nso atentarmos para a ordem na qual fazemos essa instalação, se realizamos a atualização e instalação de dependências antes de copiarmos o projeto e sem uma base para a verificação das dependências o nosso processo de build será mais demorado, pois sempre instalaremos e copiaremos todos os elementos do nosso projeto. Em contra partida, se realizarmos a cópia antes da instalação das dependências teremos a cópia de todos os elementos do projeto então, para evitarmos isso podemos orquestrar o nosso file puxando o arquivo de dependências antes de realizarmos o run das atualizações, em seguida copiamos os arquivos restantes. Caso hajam alterações essas serão aplicadas, do contrário será utilizado o cache do contêiner, ou seja, as que já estavam contidas no projeto.

### Utilizando TAG's - identificando nossa imagens
Para identificarmos melhor as imagens no Docker utilizamos as TAG's. No Docker elas são definidas por uma extensão no nome da imagem separada por dois pontos ":". Para isso temos duas possibilidades:

1. Utilizando a instrução docker image tag => essa combinação permite a criação de uma "cópia" da imagem mas alterando a sua tag para o valor especificado. Para isso inserimos o nome:tag originais da imagem que queremos ajustar e, separado por espaço, o nome:nova-tag que queremos inserir. Note que, nesse caso serão sempre exibidos as versões anteriores e novas, com o mesmo ID.

    docker image tag app:latest app:nova-tag

2. Utilizando o build -t: assim como no passo anterior, durante o build podemos nomear a nossa image já com a sua tag, evitando assim termos que atualizá-la posteriormente. Para isso incluímos o argumento -t (tag) que permite anotarmos o nome da imagem junto à sua tag, separado por dois pontos ":".

    docker build -t app:tag-escolhida .

### Repositório - Subindo imagens para o Dockerhub
O Dockerhub funciona de forma muito semelhante ao github ou outros repositórios de código. Ele permite a criação e compartilhamento de imagens a partir de um repositório remoto. Para fazermos o envio (push) para um repositório remoto basta rodarmos um docker image tag mas, ao invés de passarmos o nome:tag da imagem, passamos a sua id e, em seguida, o domínio/repositório:tag que desejamos subir. Assim que realizada a renomeação da nossa imagem, efetuamos login no dockerhub com o comando docker login (caso esteja com o docker desktop instalado e logado não será preciso informar login e senha). Por fim realizamos o docker push domínio/repositório:tag conforme imagem que iremos enviar para o repositório.

Caso trabalhemos com versinamento no repositório precisamos sempre nos atentar de alterar as tags da imagem para a versão que iremos criar/atualizar no repositório remoto, isso irá criar as versões em formato de lista, contendo as imagens de acordo como foram buildadas.

### Salvando e Movendo imagens sem o hub
Podemos compartilhar imagens diretamente por arquivos, sem a necessidade de utilizarmos o hub. Para isso usamos a instrução docker save/load. Essas instruções permitem salvarmos uma imagem em um arquivo .tar (arquivo compactado padrão do linux) onde, posteriormente podemos carregá-las manualmente.

#### Save
A instrução save grava a imagem em um arquivo, ela cotém alguns parâmetro como o -o (output, para podermos definir o nome o arquivo de saída), então passamos o nome do arquivo de destino e, por fim, o nome:tag ou id (caso seja um id único) da imagem que pretendemos salvar.

#### Load
O load segue o caminho contrário, ele irá carregar um arquivo gravado para o docker na forma de imagem. Esse comando não necessita, obrigatóriamente, de parâmetros, basta inserirmos docker load filename.tar e ele irá carregar o arquivo para o repositório local de imagens docker.

É importante, no entanto, frisar que as imagens salvas e carregadas carregam os mesmos atributos, ou seja, nome, id, tag, etc e caso tentemos carregar uma imagem com todos os atributos iguais, mas menos atualizada ela irá sobrepor a imagem anterior, mesmo esta estando mais atualizada.

