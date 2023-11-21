# Linux
## O que são distros
Sendo um software opensource temos diversas distribuições, ou distros, que são, na prática personalizações do sistema operacional criadas por usuários ou empresas especializadas. Neste caso a maioria das distros são gratuitas e, portanto, comumente utilizadas como método para cortar custos. Junto a isso, uma vez que o linux é código aberto ele permite maior controle e personalização de recursos, facilitando o trabalho em administrar e sustentar um recurso com esse sistema operacional.

## Terminal
Geralmente estamos acostumados à realizar a operação de um computador a partir de uma interface gráfica, porém no Linux é muito mais comum realizar operações utilizando o terminal, principalmente quando falamos de servidores, devido ao fato que a interface gráfica é um recurso caro para o hardware e pouco utilizado em ambientes de produção dado que a função do SO nestes casos é viabilizar a execução de aplicações ou serviços com o mínimo de interação humana.

Alguns comandos importantes para o Linux são:
* ls -> Lista arquivos e diretórios contidos em um determinado diretório
* rm -> Remove arquivos e/ou diretórios de um diretório.
* cd -> navega entre diretórios
* mkdir -> cria um diretório.
* apt -> aciona os mecanismos de instalação e atualização do sistema operacional (no caso do ubuntu e derivados)
* mv -> Utilizado para renomear ou mover um diretorio
* touch - cria um arquivo dentro do diretório onde está posicionado.
* -r / -rf -> aplicado para remover diretórios, vazios ou não.
* cat (reading mode) /more -> utilizado para exibir o conteúdo de um arquivo onde cat exibe todo o conteúdo e o more retorna o conteúdo paginado.
* > -> cat seguido do sinal de maior que ">" implica em um redirecionamento de output, ou seja, grava o valor contido no arquivo origem será escrito no arquivo de destino. O mesmo pode ser feito com echo, nesse caso passando o conteúdo digitado diretamente para o arquivo alvo do sinal.
* grep -> utilizado para pesquisar valores (diretamente ou utilizando regex) dentro de arquivos ou diretórios.
* find -> este comando é utilizado para se pesquisar por nomes de arquivos dentro de um diretório, neste caso sendo case sensitive e aceitando expressões regulares como argumento.
* ps -> lista os processos em execução no momento.
* kill <PID> -> mata um processo a partir do PID (process id) informado

## Encadeando comandos
Para encadearmos comandos no terminal basta separá-los por ponto-e-vírgula ";", desta forma ele irá executá-los de modo sequencial, sempre da esquerda para a direita, é importante ressaltar que a separação por ; irá acarretar na execução incondicional de todos os comandos inseridos na cadeia independente da falha ou não de algum deles. Podemos também separar usando o duplo E comercial "&&", neste caso ele irá tentar realizar os comandos e caso algum deles falhe ele irá interromper a execução do restante.

## Identidades e usuários
### Criação e modificação de usuários
Podemos, através do termianl, criar, editar e excluir usuários do linux utilizando os comandos abaixo:
* useradd -> cria um usuário com o nome e permissões conforme informado no comando, neste caso observando a orientação da esquerda para a a direita, iniciando pelo useradd, em seguida a lista de permissões e, por fim, o nome do usuário.
* usermod -> modifica um usuário seguindo a mesma lógica da instrução acima.
* userdel -> remove um usuário do sistema.
### Grupos
Para gerenciarmos as permissões de usuários de forma mais fácil e organizada podemos usar grupos, dessa forma temos conjuntos de permissões já definidos em cada grupo e agrupamos os usuários a partir destes. No linux temos dois tipos de grupos sendo eles grupos primários e secundários.
Para criarmos um grupo e editarmos um grupo os comandos são os mesmos para usuários com a diferença que ao invés de user utilizamos a palavra group, no caso groupadd, groupmod e groupdel.

#### Associando usuários a grupos
Para associarmos um usuário à um grupo basta utilizarmos o comando usermod e passar as instruções -g caso queiramos alterar o grupo primario ou -G para alterar o grupo secundário, em seguida inserimos o nome do grupo qu desejamos associar o usuário e, ao final, o username do usuário, exemplo: usermod -G teste userteste.

### Permissionamento de arquivos e diretórios
No linux temos uma estrutura de permissionamento distribuída em 3 segmentos, sendo eles Usuário, Grupo e Todos e, para cada grupo, temos três attributos associados que são descritos pelas siglas abaixo:
* r -> read - significa que existe acesso para leitura.
* w -> write - representa acesso para escrita.
* x -> execute - representa acesso para executar o arquivo (apenas arquivos executáveis podem receber este comando, mesmo o usuário tendo acesso se não for um executável o campo aparecerá um traço, ou seja, vazio).
  
Há duas posiveis condições então, se um atributo de acesso é permitido ele estará preenchido com a sigla correspondente, do contrário ele estará com um traço, o que significa que está vazio, ou seja, não permitido.

Ainda temos um quarto grupo na string de permissionamento, este definido pelo primeiro caractere da string, caso seja "d" o registro indica um diretório, caso seja traço representa um arquivo ou executável.

Para adicionarmos ou alteramos a paermissão de algum arquivo utilizamos o comando chmod seguido da sigla do grupo (u: user, g: group, a: all) seguido do caractere + e a sigla da permissão (r, w, x). O mesmo pode ser feito para remoção, no caso apenas substituindo o "+" por "-".
