# pip install pyautogui
import pyautogui
import time

# clicar -> pyautogui.click
# escrever -> pyautogui.write
# apertar uma tecla -> pyautogui.press
# apertar -> pyautogui.hotkey
# scroll (rolar) -> pyautogui.scroll

pyautogui.PAUSE = 0.4

# Abrir o navegador
pyautogui.press('win')
pyautogui.write('edge')
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)
# Apertar ctrl + T
pyautogui.hotkey('ctrl', 't')

# Entrar sistema empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)
pyautogui.press('enter')

time.sleep(2)

# clicar em email e digitar o email
    # email: herculessantos@gmail.com
pyautogui.click(x=703, y=500)
pyautogui.write('herculessantos891@gmail.com')

# apertar o tab e digitar a senha
    # senha: 1234
pyautogui.press('tab')
pyautogui.write('1234')
pyautogui.press('enter')

time.sleep(2)

# Importar dados
import pandas as pd

produtos = pd.read_csv(r"D:\Python Projetos\Projetos Praticos Github\automatizacao_preenchimento_formulario-main\produtos.csv")
print(produtos)


for linha in produtos.index:
    # Cadastrar produtos
    pyautogui.click(x=909, y=346)
    
    # Código
    codigo = produtos.loc[linha, 'codigo']
    pyautogui.write(codigo)
    pyautogui.press('tab')
    
    # Marca
    pyautogui.write(produtos.loc[linha, 'marca'])
    pyautogui.press('tab')
    
    # Tipo
    pyautogui.write(str(produtos.loc[linha, 'tipo']))
    pyautogui.press('tab')
    
    # Categoria
    pyautogui.write(str(produtos.loc[linha, 'categoria']))
    pyautogui.press('delete')
    pyautogui.press('tab')
    
    # Preço unitário
    pyautogui.write(str(produtos.loc[linha, 'preco_unitario']))
    pyautogui.press('delete')
    pyautogui.press('tab')
    
    # Custo
    pyautogui.write(str(produtos.loc[linha, 'custo']))
    pyautogui.press('delete')
    pyautogui.press('tab')
    
    # Observações
    obs = produtos.loc[linha, 'obs']
    if not pd.isna(obs):
        pyautogui.write(obs)
    pyautogui.press('tab')
    
    # Enviar
    pyautogui.press('enter')
    
    pyautogui.scroll(5000)
