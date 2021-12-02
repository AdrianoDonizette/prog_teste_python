from selenium import webdriver
import time

navegador: webdriver = webdriver.Chrome("chromedriver.exe")

#passo 1: entra no site do instagram
navegador.get("https://instagram.com/")
time.sleep(2)

#passo 2: faz login
navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("AdrianoTestBotPython")
navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("adF489300")
time.sleep(0.5)
navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
time.sleep(3)

#passo 3: clica no "agora não" do "salvar informações de login"
navegador.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
time.sleep(2)

#passo 4: clica no "agora não" do "salvar notificação"
navegador.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
time.sleep(1)

#passo 5: clica na barra de pesquisa para procurar o perfil
navegador.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input').click()


#passo 6: digita o nome do perfil na barra de pesquisa
navegador.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys("VihSantos")
time.sleep(1)

#passo 7: clica no perfil pesquisado
navegador.find_element_by_class_name("-qQT3").click()
time.sleep(3)

#passo 8: clica para seguir o perfil pesquisado
navegador.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/div/div/span/span[1]/button').click()