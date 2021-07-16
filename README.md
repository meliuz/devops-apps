# Este repositório foi arquivado e o novo repositório de apps SRE foi criado: https://github.com/meliuz/challenge-sre

## Méliuz DevOps

Dentro deste diretório você encontrará duas aplicações: uma escrita em Python e outra em PHP.

As aplicações são muito simples, porém, elas devem ser implantadas em servidores diferentes conforme instruções do teste. Ambas possuem dependências, listadas nos arquivos do gerenciador de pacotes de cada linguagem:

* PHP: `composer.json`
* Python: `requirements.txt`

As mesmas são instaladas via `composer` (PHP) e `pip` (Python).

Os seguintes endpoints podem ser utilizados para testar as aplicações:

* PHP e Python: `/`
* PHP: `/ping.php`
* Python: `/ping`

O ambiente de desenvolvimento pode ser criado, utilizando Docker e Docker Compose, a partir dos comandos:

    make build
    make up

Note que há dependências entre os containers e seus endereços e portas são informados através de variáveis de ambiente.

## Instruções importantes:
Este teste é confidencial, portanto não é autorizada a exibição ou envio por nenhum meio, quão menos sua divulgação através de repositórios públicos. Também não é permitido pedir ajuda ou compartilhar com terceiros.
Você terá 7 dias para fazer o case.

### CASE:
Automatize a criação de um ambiente (prefencialmente cloud AWS, mas podendo ser implementado em Azure, GCP ou localmente com virtualbox) com as seguintes especificações:
- O ambiente deve servir uma aplicação Python e uma aplicação PHP;
- As aplicações devem responder numa URL, caso o teste seja feito em Cloud url deve ser pública, caso privado url deve ser acessivel localmente;
- A aplicação PHP pode ter sua saúde testada no path /ping;
- A aplicação Python pode ter sua saúde testada no path /ping;
- As aplicações de exemplo devem ser clonadas deste próprio [repositório git](https://github.com/meliuz/devops-apps), sendo que ambas possuem dependências para funcionar;
- A aplicação php possui um arquivo .htaccess para funcionar como esperado;
- Na aplicação PHP é necessário configurar uma variável de ambiente “PYTHON_APP_ADDRESS” com a URL pública da aplicação Python (o IP de uma instância ou qualquer outro endereço acessível, onde a aplicação esteja sendo servida);
- A automação deverá realizar o deploy das aplicações disponíveis de forma automática;
- O ambiente deve ser seguro a ataques externos (o mais seguro que você conseguir sem indisponibilizar as aplicações);
- As aplicações devem estar configuradas para um scale up de uma máquina quando o grupo atingir mais de 70% do CPU por mais de 5 minutos;
- As aplicações devem estar configuradas para um scale down de uma máquina quando o grupo atingir menos de 30% de CPU por mais de 5 minutos;
- O ambiente deve ser hospedado no Brasil e pode usar as zonas 1a e 1c, caso o exercício seja feito na AWS;
Ao acessar o path /ping da aplicação PHP, o resultado esperado é um retorno 200 com o seguinte output:
- IP da API: xxx.xxx.xxx.xxx IP da aplicação: xxx.xxx.xxx.xxx;
- Criar um script para apagar o ambiente proposto de forma automática;

Você pode criar a automação da melhor forma que entender (script bash, terraform, ansible etc.), desde que inclua um passo-a-passo do que devemos fazer para montar o ambiente e que funcione em Linux (pois seu ambiente de trabalho no Méliuz usará Linux).

**IMPORTANTE:** Você também deve criar um arquivo `Makefile` com os comandos de execução e um `README.md` explicando como executar esse processo de automação criado, além de comentários sobre este teste e como você tomou as decisões para resolve-lo.

Iremos avaliar a adequação à solução proposta, nível de automação do processo, decisões de projeto e segurança além de facilidade de reprodutibilidade do ambiente proposto.

Você deve criar um repositório privado no [Github](https://github.com) e compartilhar com o usuário [pauloroberto97](https://github.com/pauloroberto97), [adilson-cruz](https://github.com/adilson-cruz), [anderson-pids](https://github.com/anderson-pids) e [marcelma](https://github.com/marcelma).

Lembre-se de não deixar as credenciais de sua conta nos arquivos do repositório.
