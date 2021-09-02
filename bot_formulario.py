# criar um preenchedor de formularios com base nos dados contidos em uma lista
# o programa devera clicar e preencher os campos corretos e ,por fim, enviar
# usar, portanto, pyautogui.click() e pyautogui.typewrite()
import pyautogui
import time

# formulario no SITE:https://docs.google.com/forms/d/e/1FAIpQLScSVDFU76rZvbO_tiIwSt6d9sOK0CZyS9KKMCP6cP5O5W5lVQ/viewform
lista_dados: list = [
    ['mateus', 'palhaços', 'Amulet', 2, 'Ok'],
    ['Larissa', 'capetas', 'Wand', 3, 'All right'],
    ['EU', 'Caos', 'Money', 4, 'Pro']
]

for quantidade in range(len(lista_dados)):
    # vendo o tamanho da resolucao para tirar as medidas:
    resolucao_x, resolucao_y = pyautogui.size()
    print(f'Resolução total da tela = {resolucao_x}:{resolucao_y}')
    print('Começando a preencher os formulários\nAguarde...')
    time.sleep(5)

    # clicando no primeiro campo (nome):
    pyautogui.click(400, 425)
    pyautogui.write(lista_dados[quantidade][0])
    time.sleep(1)

    # clicando no segundo campo (maior medo):
    pyautogui.hotkey('tab')        # clicando tab para descer
    pyautogui.moveRel()             # posicionando o mouse onde o cursor parou para clicar
    pyautogui.click()
    pyautogui.write(lista_dados[quantidade][1])
    time.sleep(1)

    # preenchendo o próximo campo (qual a fonte do seus poderes)
    pyautogui.hotkey('tab')
    pyautogui.hotkey('enter')      # abrindo a caixa de diálogo
    if lista_dados[quantidade][2] == 'Amulet':
        pyautogui.hotkey('down')      # andando pela selecao
        pyautogui.hotkey('down')      # andando pela selecao
        pyautogui.hotkey('enter')    # selecionando a caixa de diálogo
    elif lista_dados[quantidade][2] == 'Wand':
        pyautogui.hotkey('down')  # andando pela selecao
        pyautogui.hotkey('enter')  # selecionando a caixa de diálogo
    elif lista_dados[quantidade][2] == 'Money':
        for n in range(4):
            pyautogui.hotkey('down')
        pyautogui.hotkey('enter')
    time.sleep(1)

    # escolhendo a avaliacao :
    pyautogui.hotkey('tab')
    pyautogui.hotkey('left')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    time.sleep(1)

    # indo para o próximo campo (comentarios adicionais)
    pyautogui.click()
    pyautogui.typewrite('Nada, por agora.')
    time.sleep(8)

    # enviando formulário
    pyautogui.hotkey('tab')
    pyautogui.hotkey('enter')
    time.sleep(2)

    # clicando para comecar outro formulario:
    pyautogui.hotkey('tab')
    pyautogui.hotkey('enter')
    time.sleep(3)
