# Automatiza tarefas do MS Rewards

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Cria o navegador/sessão
opcoes = webdriver.EdgeOptions()
wbEdge = webdriver.Edge(options=opcoes)

# Navega para a página desejada
wbEdge.get("https://www.bing.com/news/?form=ml11z9&crea=ml11z9&wt.mc_id=ml11z9&rnoreward=1&rnoreward=1")

# Efetua o preenchimento do formulário para executar a pesquisa, limpando o campo após a pesquisa.
with open("pesquisas.txt", "r", encoding='utf-8') as f:
    texto_pesquisas = f.readlines()
          
    for i in texto_pesquisas:
        print(i)
        wbEdge.find_element(By.XPATH,
                           value='//*[@id="sb_form_q"]').clear()
        wbEdge.find_element(By.XPATH,
                           value='//*[@id="sb_form_q"]').send_keys(i)
        wbEdge.find_element(By.XPATH,
                           value='//*[@id="sb_form_q"]').click()
        time.sleep(10)
