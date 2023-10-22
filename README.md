 <h1 style="font-size:200%;
  text-align:center">Web Scraping com Python: Automatizando uma recolha de dados na web com Selenium</h1>
  <h4 style="font-size:150%;
 text-align:center">Este projeto é parte da formação em Vision artificielle (Visão Computacional) da Cegep-Matane</h4>
<h4 style="font-size:150%;
 text-align:center">by Carlos Mandele, Data Scientist in progress</h4>
 

##
Web scraping é uma técnica que compreende a recolha de dados de paginas web com objetivo de extrair informações específicas. Neste projeto, o objetivo é extair informações de forma automatizada sobre as condições das marés em Tadoussac(Canada) para os próximos sete dias, utilizando Python e as bibliotecas Selenium e BeautifulSoup.

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
