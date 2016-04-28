# Méliuz DevOps

Dentro deste diretório você encontrará duas aplicações: uma escrita em python e outra em php.

As aplicações são muito simples, porém, elas devem ser implantadas em servidores diferentes conforme instruções do teste.

As aplicações possuem dependências, sendo elas:

PHP: Guzzle
Python: Flask

As dependências devem ser instaladas via composer (php) e pip (python).

Para a aplicação PHP funcionar, ela deverá ter acesso a uma variável de ambiente chamada `PYTHON_APP_ADDRESS`.
Essa variável deve conter o endereço web da aplicação Python, assim: `http://python_app.meliuz.com.br`.

