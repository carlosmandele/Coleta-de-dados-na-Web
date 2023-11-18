## Web Scraping com Python: Automatizando uma recolha de dados na web com Selenium
   
Projeto realizado durante minha aula de visão computacional (Deep learning) avançado na Université Cégep de Matane

##### Copyright (c) 2023, Carlos MANDELE

O conteúdo deste projeto é licenciado <a href="https://creativecommons.org/licenses/by/4.0/deed.fr" target='_blank'>Creative Commons Attribution 4.0 (CC BY 4.0)</a>,<br/>e os códigos estão em <a href="https://www.apache.org/licenses/LICENSE-2.0" target='_blank'>licence Apache 2.0</a>.
 

##
Web scraping é uma técnica que compreende a recolha de dados de paginas web com objetivo de extrair informações específicas. Neste projeto, o objetivo é extair informações de forma automatizada sobre as condições das marés em Tadoussac (Canada) para os próximos sete dias, utilizando Python e as bibliotecas Selenium e BeautifulSoup.

 ##
<h2 style="font-size:150%;
 text-align:center">Etapas do desenvolvimento do projeto:</h2>
 
1- Instalação de um driver para o controle do navegador pelo Selenium
* Instalação Selenium
* Instalação Beautiful Soup

2- Solicitar ao servidor a obtenção do conteúdo (código HTML) de uma página web para uma URL específico

3- No caso de um formulário:
* Abertura da página web do formulário
* Análise de pontos de entrada com a função de inspeção do navegador:

  a) Reconstruir a sequência de interações com o formulário (cliques, menus e entrada do teclado)
  
  b) Obter os identificadores de botões, menus, campos de entrada

3.1- No caso de um formulário:
* Programação de um script de interação Selenium com o formulário
* Execução do script Selenium de interações com o formulário


4- Download da página web de resultados retornada pelo servidor

5- Identificação da informação que se pretende extrair da página web de resultados

6- Extraindo secções relevantes da página web de resultados com Beautiful Soup

7- Extrair informações detalhadas com expressões regulares

8- Salvando em uma estrutura de dados na memória e/ou em um arquivo


#
<p xmlns:cc="http://creativecommons.org/ns#" >This work is licensed under <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"></a></p>
