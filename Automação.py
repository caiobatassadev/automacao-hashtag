# Passo a passo do projeto (sempre!)
# Passo 1: Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui as auto
from time import sleep
# pyautogui.write - Escreve texto
# pyautogui.press - Aperta uma teclaTESA00TELG000821    LG  0125  Samsung
# pyautogui.click - Clicar em algum lugar da tela
# pyautogui.hotkey - combinação de teclas

# Delay entre os comandos
auto.PAUSE = 0.5

# Abrir o navegador (opera)
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
auto.press('win')
auto.write('Opera')
auto.press('enter')
sleep(2)
auto.write(link)
auto.press('enter')
sleep(2) 

# Passo 2: Fazer o Login

auto.click(x=828, y=391) # Selecionar o campo email
auto.write('caiombatassa@gmail.com') # Digitar o email
auto.press('tab') # passar ao próximo campo
auto.write('Caio.1909007') 
auto.press('tab')
auto.press('enter') # clicar no botão de login
sleep(2)

# Passo 3: Importar a base de produtos para cadastro
import pandas as pd
tabela = pd.read_csv('produtos.csv')

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
    auto.click(x=737, y=282)
    # pegar da tabela o valor que campo que queremos preencher
    codigo = tabela.loc[linha, 'codigo']
    auto.write(str(codigo))
    # passar para o próximo campo
    auto.press('tab')
    # preencher os campos
    auto.write(str(tabela.loc[linha, 'marca']))
    auto.press('tab')
    auto.write(str(tabela.loc[linha, 'tipo']))
    auto.press('tab')
    auto.write(str(tabela.loc[linha, 'categoria']))
    auto.press('tab')
    auto.write(str(tabela.loc[linha, 'preco_unitario']))
    auto.press('tab')
    auto.write(str(tabela.loc[linha, 'custo']))
    auto.press('tab')
    obs = tabela.loc[linha, 'obs']
    if not pd.isna(obs):
        auto.write(str(tabela.loc[linha, 'obs']))
    auto.scroll(-5000)
    sleep(5)
    auto.press('tab')
    auto.press('enter') # cadastra o produto (botao enviar)
    # dar o scroll do tudo para cima
    auto.scroll(5000)
    # Passo 5: Repetir o processo até acabar os produtos
    



