# Introdução ao Git

# Sumário

1. [Introdução ao Git](#introdução-ao-git)
   - [O que é Git?](#o-que-é-git)
     - [Definição e importância do controle de versão](#definição-e-importância-do-controle-de-versão)
     - [Breve história do Git](#breve-história-do-git)
2. [Conceitos Fundamentais do Git](#conceitos-fundamentais-do-git)
   - [Repositório](#repositório)
   - [Commit](#commit)
   - [Branch](#branch)
   - [Merge](#merge)
   - [Conflict](#conflict)
3. [Configuração Inicial do Git](#configuração-inicial-do-git)
   - [Configuração de usuário e email](#configuração-de-usuário-e-email)
   - [Gerando e adicionando chaves SSH](#gerando-e-adicionando-chaves-ssh)
4. [Trabalhando com Repositórios Git](#trabalhando-com-repositórios-git)
   - [Inicializando um Novo Repositório](#inicializando-um-novo-repositório)
   - [Clonando um Repositório Existente](#clonando-um-repositório-existente)
5. [Fluxo de Trabalho Básico do Git](#fluxo-de-trabalho-básico-do-git)
   - [Modificando arquivos](#modificando-arquivos)
   - [Verificando o status do repositório](#verificando-o-status-do-repositório)
   - [Adicionando alterações ao stage](#adicionando-alterações-ao-stage)
   - [Commitando alterações](#commitando-alterações)
6. [Branching e Merging](#branching-e-merging)
   - [Criando branches](#criando-branches)
   - [Navegando entre branches](#navegando-entre-branches)
   - [Merging](#merging)
7. [Resolvendo Conflitos](#resolvendo-conflitos)
   - [Identificando conflitos](#identificando-conflitos)
   - [Resolvendo conflitos manualmente](#resolvendo-conflitos-manualmente)
   - [Usando ferramentas de merge](#usando-ferramentas-de-merge)
8. [Trabalhando com Repositórios Remotos](#trabalhando-com-repositórios-remotos)
   - [Adicionando um repositório remoto](#adicionando-um-repositório-remoto)
   - [Push](#push)
   - [Pull](#pull)
   - [Fetch](#fetch)
9. [Boas Práticas com Git](#boas-práticas-com-git)
   - [Mensagens de commit claras e descritivas](#mensagens-de-commit-claras-e-descritivas)
   - [Mantendo um histórico limpo com rebase](#mantendo-um-histórico-limpo-com-rebase)
   - [Uso de tags para marcar releases](#uso-de-tags-para-marcar-releases)
10. [Git Avançado](#git-avançado)
    - [Stashing alterações](#stashing-alterações)
    - [Cherry-picking commits](#cherry-picking-commits)
    - [Rebasing interativo](#rebasing-interativo)


## O que é Git?

### Definição e importância do controle de versão

Git é um sistema de controle de versão distribuído, gratuito e de código aberto, projetado para lidar com tudo, desde pequenos a grandes projetos com velocidade e eficiência. O Git permite que múltiplos desenvolvedores trabalhem juntos em um projeto, controlando e rastreando as mudanças feitas no código fonte ao longo do tempo. Isso facilita a colaboração entre equipes, permitindo que elas vejam o histórico completo de alterações e revertam para versões anteriores do projeto quando necessário.

A importância do controle de versão não pode ser subestimada. Ele não apenas facilita a gestão de mudanças e colaboração em projetos de software, mas também ajuda a prevenir conflitos entre alterações feitas por diferentes desenvolvedores. Além disso, o controle de versão é crucial para a manutenção da integridade do código e para a implementação de um fluxo de trabalho estruturado em projetos de desenvolvimento.

### Breve história do Git

Git foi criado por Linus Torvalds em 2005 para o desenvolvimento do kernel do Linux, com a contribuição de outros desenvolvedores do kernel. A necessidade de um novo sistema de controle de versão surgiu após a comunidade de desenvolvimento do Linux decidir parar de usar um sistema proprietário que eles estavam utilizando. Torvalds projetou o Git para ser rápido, simples e, acima de tudo, capaz de suportar desenvolvimento distribuído não linear.

Desde o seu lançamento, o Git rapidamente se tornou um padrão de facto para o controle de versão de software, sendo adotado por indivíduos e organizações ao redor do mundo. Sua eficiência e flexibilidade para gerenciar projetos de qualquer tamanho, sua robusta capacidade de suportar desenvolvimento não linear (através de branches e merges), e sua facilidade de uso são algumas das razões para sua popularidade generalizada.

O Git é mais do que apenas uma ferramenta técnica; ele mudou a maneira como os desenvolvedores pensam sobre o desenvolvimento de software, permitindo abordagens mais colaborativas e iterativas. Com o surgimento de plataformas baseadas em Git, como GitHub, GitLab e Bitbucket, o Git também desempenhou um papel fundamental na promoção da cultura de código aberto, facilitando a colaboração em projetos de software em todo o mundo.

Claro, vamos detalhar os conceitos fundamentais do Git com exemplos práticos para cada um.

## Conceitos Fundamentais do Git

O Git é construído em torno de alguns conceitos chave que formam a base de sua funcionalidade e fluxo de trabalho. Entender esses conceitos é crucial para usar o Git efetivamente.

### Repositório

Um **repositório** é a coleção mais básica de arquivos de um projeto sob controle de versão do Git, juntamente com o histórico de todas as mudanças feitas nesses arquivos. O repositório contém todos os commits, ou pontos de salvamento, e branches, ou linhas de desenvolvimento.

**Exemplo:** Para iniciar um novo repositório Git no seu projeto local, você usaria o comando:
```bash
git init
```
Isso cria um novo subdiretório `.git` no seu projeto, que armazena toda a estrutura de dados do Git para o controle de versão.

### Commit

Um **commit** é uma captura do estado dos arquivos no seu repositório em um ponto no tempo. Cada commit tem um identificador único (um hash SHA-1) e inclui metadados como o autor e a data. Commits formam a espinha dorsal do histórico de um repositório e permitem que você volte a estados anteriores do projeto.

**Exemplo:** Para salvar as mudanças feitas nos arquivos do seu projeto em um novo commit, você primeiro adiciona os arquivos ao stage e então faz o commit:
```bash
git add .
git commit -m "Adiciona funcionalidade X"
```
Isso cria um commit com a mensagem "Adiciona funcionalidade X".

### Branch

Um **branch** é uma linha independente de desenvolvimento dentro de um repositório, permitindo que você trabalhe em diferentes funcionalidades ou versões do projeto simultaneamente sem afetar o código principal (geralmente o branch `master` ou `main`).

**Exemplo:** Para criar um novo branch chamado `nova-funcionalidade` e mudar para ele, você usaria:
```bash
git branch nova-funcionalidade
git checkout nova-funcionalidade
```
Ou de forma mais concisa:
```bash
git checkout -b nova-funcionalidade
```

### Merge

**Merge** é o processo de unir as mudanças de dois branches diferentes. Quando você termina de trabalhar em um branch de funcionalidade, pode querer mesclar essas mudanças de volta ao branch principal.

**Exemplo:** Para mesclar as mudanças do branch `nova-funcionalidade` de volta ao `main`, primeiro mude para o branch `main` e então faça o merge:
```bash
git checkout main
git merge nova-funcionalidade
```

### Conflict

Um **conflict** ocorre quando o Git não consegue mesclar automaticamente as mudanças de dois branches devido a alterações contraditórias nos mesmos trechos de arquivos. O Git pausará o processo de merge e pedirá que você resolva manualmente os conflitos.

**Exemplo:** Se dois branches modificaram a mesma linha de um arquivo, ao tentar fazer um merge, o Git apresentará uma mensagem de conflito. Você precisará abrir o arquivo em questão, encontrar as marcações de conflito (indicadas por `<<<<<<<`, `=======`, `>>>>>>>`), escolher a alteração a ser mantida (ou combinar as duas), salvar o arquivo, e então continuar o merge:
```bash
git add arquivo-com-conflito
git commit -m "Resolve conflito de merge"
```

Entender esses conceitos fundamentais é essencial para navegar no mundo do Git e aproveitar ao máximo suas poderosas funcionalidades de controle de versão.

Claro, vamos detalhar a seção sobre a configuração inicial do Git, incluindo como configurar seu usuário e email, e como gerar e adicionar chaves SSH para uma comunicação segura com repositórios remotos.


## Configuração Inicial do Git

Antes de começar a usar o Git para projetos de desenvolvimento, é importante configurar seu ambiente de trabalho. Isso inclui definir suas informações de usuário para commits e configurar a autenticação SSH para repositórios remotos.

### Configuração de usuário e email

O Git usa um nome de usuário e um email para associar commits a um autor. Para configurar seu nome de usuário e email no Git, use os seguintes comandos no terminal:

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seuemail@exemplo.com"
```

Essas informações serão usadas em todos os seus commits, portanto, escolha um email que você planeja usar para rastreamento de histórico de código.

### Gerando e adicionando chaves SSH

SSH (Secure Shell) é um protocolo de rede que fornece aos usuários uma maneira segura de acessar redes ou computadores. No contexto do Git, usar chaves SSH permite uma conexão segura e sem senha aos repositórios remotos. Para gerar uma nova chave SSH:

1. Abra o terminal.
2. Execute o comando `ssh-keygen`, fornecendo seu email como um rótulo. Por exemplo:

```bash
ssh-keygen -t rsa -b 4096 -C "seuemail@exemplo.com"
```

- Isso cria uma nova chave SSH, usando o email fornecido como rótulo.
- Quando solicitado a "Enter a file in which to save the key," pressione Enter para aceitar o local padrão.
- Na próxima etapa, você terá a opção de inserir uma senha segura para a chave.

3. Após gerar a chave SSH, você precisará adicionar a chave ao ssh-agent. Primeiro, inicie o ssh-agent em background:

```bash
eval "$(ssh-agent -s)"
```

4. Adicione sua chave SSH privada ao ssh-agent:

```bash
ssh-add ~/.ssh/id_rsa
```

5. Por fim, adicione a chave SSH à sua conta no GitHub, GitLab, Bitbucket ou qualquer outro serviço de hospedagem de Git que você esteja usando. Para isso, você precisará copiar o conteúdo da sua chave pública (por padrão `~/.ssh/id_rsa.pub`) para o serviço. Você pode exibir e copiar o conteúdo da chave com:

```bash
cat ~/.ssh/id_rsa.pub
```

Copie a saída desse comando e adicione-a às suas chaves SSH nas configurações do seu perfil no serviço de hospedagem de Git.

Configurar corretamente seu usuário e email, bem como estabelecer uma conexão segura SSH, são passos fundamentais para garantir que seus trabalhos com Git sejam suaves e seguros.

Vamos detalhar essas seções com exemplos práticos para ilustrar o uso básico do Git, incluindo como trabalhar com repositórios, o fluxo de trabalho básico, e como gerenciar branches e merges.

### Trabalhando com Repositórios Git

#### Inicializando um Novo Repositório

Para iniciar um novo repositório Git no seu projeto local, navegue até o diretório do projeto no terminal e execute:

```bash
git init
```

Isso cria um novo subdiretório `.git` no seu projeto, que armazena todos os metadados necessários para o controle de versão.

#### Clonando um Repositório Existente

Para clonar um repositório existente, ou seja, fazer uma cópia local de um repositório remoto, use:

```bash
git clone [URL]
```

Substitua `[URL]` pela URL do repositório que você deseja clonar. Por exemplo:

```bash
git clone https://github.com/exemplo/projeto.git
```

Isso cria uma cópia local do repositório em um novo diretório chamado `projeto`.

### Fluxo de Trabalho Básico do Git

#### Modificando arquivos

Após clonar um repositório ou inicializar um novo, você pode começar a modificar os arquivos no diretório do projeto.

#### Verificando o status do repositório

Para ver quais arquivos foram modificados ou estão prontos para serem commitados, use:

```bash
git status
```

#### Adicionando alterações ao stage

Antes de commitar suas mudanças, você precisa adicioná-las ao "stage" com:

```bash
git add [arquivo]
```

Para adicionar todas as mudanças de uma vez, use:

```bash
git add .
```

#### Commitando alterações

Para salvar suas mudanças no histórico do repositório, faça um commit com:

```bash
git commit -m "Sua mensagem de commit"
```

Substitua `"Sua mensagem de commit"` por uma breve descrição das alterações realizadas.

### Branching e Merging

#### Criando branches

Para criar um novo branch:

```bash
git branch [nome-do-branch]
```

Para criar um novo branch e mudar para ele imediatamente:

```bash
git checkout -b [nome-do-branch]
```

#### Navegando entre branches

Para mudar de um branch para outro:

```bash
git checkout [nome-do-branch]
```

#### Merging

Para mesclar as mudanças de um branch de volta ao branch principal (por exemplo, `main`), primeiro mude para o branch principal e então faça o merge:

```bash
git checkout main
git merge [nome-do-branch]
```

Isso incorpora as mudanças do `[nome-do-branch]` no branch `main`.

Vamos detalhar essas seções com exemplos práticos para fornecer uma compreensão clara de como resolver conflitos, trabalhar com repositórios remotos, seguir boas práticas com Git, e utilizar recursos avançados do Git.

### Resolvendo Conflitos

#### Identificando conflitos

Quando você tenta fazer um `merge` ou um `rebase` e o Git não consegue resolver automaticamente as diferenças entre os branches, ele entra em um estado de conflito. O Git marcará os arquivos em conflito e interromperá o processo para que você possa resolver manualmente.

```bash
Auto-merging arquivo.txt
CONFLICT (content): Merge conflict in arquivo.txt
Automatic merge failed; fix conflicts and then commit the result.
```

#### Resolvendo conflitos manualmente

1. Abra os arquivos em conflito indicados pelo Git.
2. Procure pelas seções marcadas com `<<<<<<<`, `=======`, e `>>>>>>>`. Estas marcas definem o início do conflito, a separação entre as versões em conflito, e o fim do conflito, respectivamente.
3. Edite o arquivo para resolver o conflito. Isso pode envolver escolher uma das versões ou combinar conteúdo de ambas.
4. Após resolver o conflito, remova as marcas de conflito do arquivo.
5. Adicione o arquivo ao stage e faça um commit das alterações:

```bash
git add arquivo.txt
git commit -m "Resolve conflito de merge"
```

#### Usando ferramentas de merge

Você pode usar ferramentas gráficas de merge, como `meld`, `kdiff3`, ou a ferramenta integrada do seu IDE, para resolver conflitos. Para configurar uma ferramenta de merge padrão:

```bash
git config --global merge.tool [nome-da-ferramenta]
```

E para iniciar a ferramenta de merge durante um conflito:

```bash
git mergetool
```

### Trabalhando com Repositórios Remotos

#### Adicionando um repositório remoto

Para adicionar um novo repositório remoto ao seu projeto Git:

```bash
git remote add origin https://github.com/usuario/repositorio.git
```

Substitua `origin` pelo nome que você deseja dar ao remoto (origin é o nome padrão) e a URL pelo endereço do seu repositório remoto.

#### Push

Para enviar suas alterações locais para um repositório remoto:

```bash
git push origin main
```

Isso envia os commits do branch `main` local para o branch `main` no repositório `origin`.

#### Pull

Para atualizar seu branch local com as alterações do repositório remoto:

```bash
git pull origin main
```

Isso busca (`fetch`) as alterações do branch `main` de `origin` e faz um `merge` delas no seu branch local `main`.

#### Fetch

Para buscar as alterações mais recentes de um repositório remoto sem automaticamente fazer merge:

```bash
git fetch origin
```

### Boas Práticas com Git

#### Mensagens de commit claras e descritivas

Escreva mensagens de commit que expliquem claramente o que foi alterado e por quê. Uma boa prática é começar a mensagem com um resumo conciso (menos de 50 caracteres), seguido de uma descrição mais detalhada se necessário.

#### Mantendo um histórico limpo com rebase

Use `git rebase` em vez de `git merge` para integrar alterações de um branch para outro, mantendo um histórico linear de commits. Isso facilita a leitura do histórico do projeto.

```bash
git rebase main
```

#### Uso de tags para marcar releases

Use `git tag` para marcar pontos significativos no histórico do projeto, como releases:

```bash
git tag -a v1.0 -m "Versão 1.0"
git push origin v1.0
```

### Git Avançado

#### Stashing alterações

Use `git stash` para salvar temporariamente alterações não commitadas para que você possa trocar de branch sem perder essas alterações:

```bash
git stash
git stash pop
```

#### Cherry-picking commits

Use `git cherry-pick` para aplicar um commit específico de outro branch ao branch atual:

```bash
git cherry-pick [hash-do-commit]
```

#### Rebasing interativo

Use `git rebase -i` para reordenar, remover ou combinar commits de forma interativa:

```bash
git rebase -i HEAD~3
```

Isso permite ajustar os últimos 3 commits de forma interativa.

Cada uma dessas seções oferece uma visão sobre como utilizar eficazmente o Git, desde a resolução de conflitos até a aplicação de boas práticas e o uso de recursos avançados para gerenciar seu código e colaboração de forma mais eficiente.