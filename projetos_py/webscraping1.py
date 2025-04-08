#web scraping -  Danny - 03-12-2021

import time
import requests
import pandas as pd  
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

# Pegar conteudo HTML a partir da URL
url = "https://stats.nba.com/players/traditional/?PerMode=Totals&Season=2019-20&SeasonType=Regular%20Season&sort=PLAYER_NAME&dir=-1"
#url = "https://ageopro.com.br/painel/hora_brasil.php?key=852963741jkytBN"

top10ranking = {}

rankings = {
    '3points': {'field': 'FG3M', 'label': '3PM'},
    'points': {'field': 'PTS', 'label': 'PTS'},
    'assistants': {'field': 'AST', 'label': 'AST'},
    'rebounds': {'field': 'REB', 'label': 'REB'},
    'steals': {'field': 'STL', 'label': 'STL'},
    'bloks': {'field': 'BLK', 'label': 'BLK'},
}

def buildrank(type):

    field = rankings[type]['field']
    label = rankings[type]['field']

    driver.find_element_by_xpath(
        f"//div[@class='nba-stat-table']//table//thead//tr//th[@data-field='{field}']").click()

    element = driver.find_element_by_xpath("//div[@class='nba-stat-table']//table")
    html_content = element.get_attribute('outerHTML')
    print(html_content)

    # Pasear o conteudo HTML - BeutifullSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find(name='table')

    # Estruturar o conteuda em uma Data Frame - Pandas
    df_full = pd.read_html(str(table))[0].head(10)
    df = df_full[['Unnamed: 0', 'PLAYER', 'TEAM', label]]
    df.columns = ['pos', 'player', 'team', 'total']
    print(df)

    # Tranformar os dados em um dicionario de dados próprio
    return df.to_dict('records')

#print(top10ranking['points'])

Option = Options()
Option.headless = True
driver = webdriver.Firefox()

driver.get(url)
time.sleep(10)

for k in rankings:
    top10ranking[k] = buildrank(k) 


driver.quit()
# Converter e salvar o aquivo JSON
#js = json.dumps(top10ranking)
#fp = open('ranking.json', 'w')
#fp.write(js)
#fp.close() 

with open('ranking.json', 'w', encoding='utf-8') as jp:
    js = json.dumps(top10ranking, indent=4)
    jp.write(js)






# libs:
# pip install request2
# pip install pandas
# pip install lxml
# pip install beautifulsoup4
# pip install selenium

# baixei o componente do selenium e coloquei na pasta 
#C:\Users\meuUsuario\AppData\Local\Programs\Python\Python37
#para arrumar o bug de variavel de ambiente Geckodriver