# Méliuz DevOps

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
