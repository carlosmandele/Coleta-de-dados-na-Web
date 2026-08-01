# -*- coding: utf-8 -*-
"""
## Web Scraping - Automatizando uma recolha de dados na web com Python


##### Copyright (c) 2023, KALOMBOLA, C. M.

O conteúdo deste projeto é licenciado <a href="https://creativecommons.org/licenses/by/4.0/deed.fr" target='_blank'>Creative Commons Attribution 4.0 (CC BY 4.0)</a>
"""

# Importação das libs
#-*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from selenium import webdriver
import re
import pandas as pd

print("Bibliotecas Python importadas comsucesso !")

"""### Análisando os pontos de entrada de formulário com a função de inspeção do browser:
<ul>
    <ul>
        <li>Abrir a página do <a href="https://www.marees.gc.ca/fra/station?sid=2985" target='_blank'>formulário</a> no site Pêches et Océans Canada;</li>
        <li>Reconstruir a sequência de interações com o formulário (cliques, menus e entrada do teclado);</li>
        <li>Obter identificadores de botões, menus, campos de entrada;</li>
    </ul>
</ul>

### Programando um script de interação Selenium com o formulário sobre as condições do mar
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from warnings import filterwarnings
filterwarnings("ignore")

# Instanciar um driver para o navegador
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
robot_edge = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))


# Abrindo a página web onde o formulárion está localizado
robot_edge.get("https://www.marees.gc.ca/fr/stations/")

localidade = "Tadoussac"

# Solicitar o formulário para a localidade
seizure_localidade = robot_edge.find_element(By.XPATH, "//div/label/input")
seizure_localidade.clear()
seizure_localidade.send_keys(localidade)

# Solicitar um tempo de resposta
import time
time.sleep(2)

# Clique no hiperlink para a página web sobre as condições do mar de Tadoussac
hiperlink_localidade = robot_edge.find_element(By.XPATH, "//td/a")
hiperlink_localidade.click()

# Solicitar um tempo de resposta
time.sleep(2)

# Definindo o componente calendário
seizure_date = robot_edge.find_element(By.ID, "water-levels-date")
seizure_date.clear()
robot_edge.execute_script("arguments[0].value = '2023-09-14';", seizure_date)

"""
Enviando o pedido para obter o cronograma em Tadoussac para
os proximos sete dias a partir de 14 de setembro de 2023
"""
bouton_send = robot_edge.find_element(By.ID, "water-levels-date-submit")
bouton_send.click()

# Solicitar um tempo de resposta
time.sleep(2)

# Obtendo os resultados da página web
page_answer = robot_edge.page_source

print("Selenium script deve abrir um navegador e exibir uma mensagem")
print("do tipo: « Browser is being controlled by automated test software. »")
print("em seguida, o script Selenium simula interações com o formulário.\n")
print("Script Selenium executado, formulário enviado, página de resultados recuperada...")

"""### Análise dos resultados retornado da página web  com `BeautifulSoup`"""

# Análise dos resultados retornado da página web
page_resultats = BeautifulSoup(page_answer,"html.parser")

# Inspecionando a página web devolvida
print(page_resultats.prettify())

"""###  Extraindo seções relevantes da página de resultados"""

# Recuperando parâmetros da consulta de pesquisa de informações
raw_parameters = page_resultats.find_all("table", {"class":"day-tables clearfix table-bordered responsive-enabled table table-hover table-striped"})
print("Seções relevantes em HTML:\n")
print("Número de dias:",len(raw_parameters),"\n")

# raw_parameters = raw_parameters.find("div", {"class":"wb-eqht wb-init wb-eqht-inited"})
print(raw_parameters)

"""### Exibindo texto sem formatação, sem tags HTML"""

print("Seções de texto sem formatação relevantes sem tags HTML:\n")
for parametro_brut in raw_parameters:
    text_view = parametro_brut.getText().strip()
    print(text_view)

"""### Renderizando tabelas em HTML"""

import re
from IPython.display import display, HTML

# Extraindo atributos
FORME_1 = r"(?:.*\n)<caption>(\d\d\d\d-\d\d-\d\d\s*\(\w*\))\<\/caption>"

for parametro_brut in raw_parameters:
    titulo = re.match(re.compile(FORME_1),str(parametro_brut)).group(1)
    substitution = re.sub(FORME_1, '<table>', str(parametro_brut))
    display(HTML(titulo+"\n"+substitution))

"""### Extração de dados das condições do mar"""

def extrair_numero_station(texto_inserido):
    FORME_1 = r'\s+\((\d*)\)\s+|\s+Pêches\s+et\s+Océans Canada<\/title>'
    return re.search(FORME_1, str(texto_inserido)).group(1)

numero_station = extrair_numero_station(page_resultats)
print("Numéro de estação:",numero_station)

def extrair_fuso_horario(texto_inserido):
    FORME_2 = r'<th>Heure\s*(\w*)<\/th>'
    return re.search(FORME_2, str(texto_inserido)).group(1)

fuso_horario = extrair_fuso_horario(raw_parameters[0])
print("Fuso horario:",fuso_horario)

from datetime import datetime

def extrair_data(texto_inserido):
    FORME_3 = r"(\d\d\d\d)-(\d\d)-(\d\d)"
    extraction_resultados = re.search(re.compile(FORME_3),str(texto_inserido))
    # Reescrevendo a data em português
    data_str = extraction_resultados.group(3) + "-" + extraction_resultados.group(2) + "-" + extraction_resultados.group(1)
    return data_str

extrair_data(raw_parameters[0])

def extrair_dados_mares(texto_inserido):
    FORME_4 = r"<td>(\d*:\d*)<\/td>\n<td>(\d*.\d*)<\/td>"
    extraction_resultados = re.findall(re.compile(FORME_4),str(texto_inserido))
    return extraction_resultados

extrair_dados_mares(raw_parameters[0])

"""### Fazendo backup dos dados no arquivo `dados_mares_pag_web.csv`"""

output_file_path = './'
filename_outpute = "dados_mares_pag_web.csv"
with open(output_file_path+filename_outpute,'w') as arquivo_saida:
    # Escrevendo o cabeçalho do arquivo
    arquivo_saida.write('localite\tstation\tfuseau_horaire\tdate\theure\thauteur_m\n')
    for parametro_brut in raw_parameters:
        titulo = re.match(re.compile(FORME_1),str(parametro_brut)).group(1)
        data = extrair_data(parametro_brut)
        list_dados_mares = extrair_dados_mares(parametro_brut)
        for dados_mares in list_dados_mares:
            # Savando os dados no arquivo
            arquivo_saida.write(localidade+'\t'+numero_station+'\t'+fuso_horario+'\t'+data+'\t'
                                 +dados_mares[0]+'\t'+dados_mares[1]+'\n')

print("Dados sobre as condições do mar salvos no arquivo "+ filename_outpute)

"""### Testando carregamento e a leitura do arquivo de dados"""

import pandas as pd

filename_outpute = "dados_mares_pag_web.csv"

dados_mares_df = pd.read_csv(output_file_path+filename_outpute,delimiter='\t')
dados_mares_df

print("Projeto finalizado")