#Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

#Acessar o site que for desejado
driver = webdriver.Chrome()
driver.get('https://www.americanas.com.br/categoria/informatica/notebooks/notebook-gamer?viewMode=list')

#Coletando os dados como o nome dos produtos 
titulo_nome_dos_notebook = driver.find_elements(By.XPATH,"//h3[@class='styles__Name-sc-1e4r445-0 fYqJrQ product-name']")

valor_dos_notebook = driver.find_elements(By.XPATH,"//span[@class='src__Text-sc-154pg0p-0 styles__PromotionalPrice-sc-yl2rbe-0 dthYGD list-price']")

lista=[]
  

for titulo, valor in zip(titulo_nome_dos_notebook, valor_dos_notebook):
    lista.append([titulo.text,valor.text])

print(lista)

lista_2 = len(lista)
for i in range(lista_2):
    print(lista[i])
    