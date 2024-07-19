from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pyautogui
import time

class Navegador:
    def __init__(self):
        self.servico = Service(ChromeDriverManager().install())
        self.navegador = webdriver.Chrome(service = self.servico)
        self.tempoEspera = 0.5
        
    def getLink(self, link):
        self.navegador.get(link)
        time.sleep(self.tempoEspera * 6)
        
    def enviarChave(self, xpath, chave):
        self.navegador.find_element('xpath', xpath).send_keys(chave)
        time.sleep(self.tempoEspera)

    def enviarChaves(self, listaXpaths, listaChaves):
        for contador in range(0, len(listaXpaths)):
            self.enviarChave(listaXpaths[contador], listaChaves[contador])

    def clicar(self, xpath):
        self.navegador.find_element('xpath', xpath).click()
        time.sleep(self.tempoEspera*2)

    def clicarMais(self, listaXpaths):
        for contador in range(0, len(listaXpaths)):
            self.clicar(listaXpaths[contador])

    def fechar(self):
        self.navegador.close()


class Teclado:
    def digitar(self, chave):
        pyautogui.press(chave)

    def digitarFrase(self, frase):
        for letra in frase:
            self.digitar(letra)
            
    def tab(self, vezes):
        for c in range(0, vezes):
            time.sleep(1)
            self.digitar('TAB')

    def downUp(self, vezes):
        for c in range(0, vezes):
            self.digitar('Down')
            time.sleep(1)
            self.digitar('Up')
            time.sleep(1)

    def enter(self):
        self.digitar('ENTER')

# Instanciar navegador
navegador = Navegador()
teclado = Teclado()

# Ir para o link
navegador.getLink('https://www.linkexemplo.com.br')

# Definir listas
listaXpaths = ['/html/body/div/form/input[1]', '/html/body/div/form/input[2]', '/html/body/div/form/input[3]']
listaChaves = ['login', 'email', 'senha']

# Percorrer listas e enviar chaves
navegador.enviarChaves(listaXpaths, listaChaves)

# Definir listas
listaXpaths = ['/html/body/div/form/button', '//*[@id="menu"]/ul/li[7]/a', '//*[@id="menu"]/ul/li[7]/ul/li[1]/a', '//*[@id="conteudo"]/div[4]/ng-view/div/div[2]/div/form/div/ul/li[4]/a', '//*[@id="conteudo"]/div[4]/ng-view/div/div[2]/div/form/div/div/div[4]/table/tbody/tr[1]/td[7]/div/button', '//*[@id="conteudo"]/div[4]/ng-view/div/div[2]/div/form/div/div/div[4]/table/tbody/tr[1]/td[7]/div/ul/li[2]/a']

# Percorrer listas e clicar
navegador.clicarMais(listaXpaths)

# Fechar navegador
navegador.getLink('https://www.linkservidoremail.com.br')

# Definir listas
listaXpaths = ['//*[@id="username"]', '//*[@id="password"]']
listaChaves = ['email', 'senha']

# Percorrer listas e enviar chaves
navegador.enviarChaves(listaXpaths, listaChaves)

# Definir listas
listaXpaths = ['//*[@id="lgnDiv"]/div[9]/div/span', '//*[@id="_ariaId_26"]']

#Clicar no acesso do servidor e envio de email
navegador.clicarMais(listaXpaths)

#Enviar chave
navegador.enviarChave('//*[@id="primaryContainer"]/div[5]/div/div[1]/div/div[5]/div[3]/div/div[5]/div[1]/div/div[3]/div[4]/div/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div/div/div/span/div[1]/form/input', 'email')

#Enter
teclado.enter()

# Definir listas
listaXpaths = ['//*[@id="primaryContainer"]/div[5]/div/div[1]/div/div[5]/div[3]/div/div[5]/div[1]/div/div[3]/div[4]/div/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[6]/div[2]/input', '//*[@id="primaryContainer"]/div[5]/div/div[1]/div/div[5]/div[3]/div/div[5]/div[1]/div/div[3]/div[4]/div/div[1]/div[2]/div[2]/div[2]/div[3]/div/div[3]/div[1]/div[3]/div']
listaChaves = ['Assunto email', 'Corpo email']

# Percorrer listas e enviar chaves
navegador.enviarChaves(listaXpaths, listaChaves)

# Clicar em anexar
navegador.clicar('//*[@id="primaryContainer"]/div[5]/div/div[1]/div/div[5]/div[1]/div/div[1]/div/div/div[2]/div/button')

# Ir até área de pesquisa
teclado.tab(5)

# Selecionar
teclado.enter()

# Digitar
teclado.digitarFrase('Downloads')

# Selecionar
teclado.enter()

# Ir até área de arquivos
teclado.tab(4)

# Selecionar último arquivo de download.
teclado.downUp(1)

# Selecionar arquivo
teclado.enter()

# Aguardar anexo
time.sleep(3)

# Clicar em enviar.
navegador.clicar('//*[@id="primaryContainer"]/div[5]/div/div[1]/div/div[5]/div[3]/div/div[5]/div[1]/div/div[3]/div[4]/div/div[1]/div[2]/div[3]/div[2]/div[1]/button[1]')

# Aguardar envio
time.sleep(3)

#Finalizar instância do navegador.
navegador.fechar()
