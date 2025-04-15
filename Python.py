import requests
import time
import os

# Limpa a tela (funciona no iSH também)
os.system("clear")

# Arte em ASCII
ascii_art = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣼⣿⣼⣿⣿⣟⣿⣭⣻⣶⣴⣦⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⢇⡌⣣⣾⣿⣿⣾⣿⣷⣸⣿⡷⣝⢿⣷⣄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣾⣿⢹⡘⡇⢿⣿⣟⣻⢛⣹⣿⣿⣿⣷⠽⣧⣽⣿⢀⡀⠀
⠀⢀⠀⣠⣶⣶⡾⢛⣿⣏⠯⢁⣤⣬⣙⠻⣿⠿⣿⣿⣿⣿⣧⡙⣿⣿⣟⡁⠀
⢀⡀⠭⢥⣤⣤⣶⣿⡿⢸⣷⠰⣭⣙⣃⠘⢷⣶⣶⣼⣿⣿⢿⣷⣿⣿⡟⣅⠀
⠀⠐⢶⣖⡋⠙⢛⠫⢴⣿⢿⣀⡈⠳⣌⢿⡺⢉⣿⣾⣿⣿⣮⣿⡿⣳⢀⣏⠀
⠀⣀⣈⠹⣿⠿⢿⣦⣤⣭⣿⠞⠙⢲⣊⡡⡍⠘⠭⣙⡥⢿⡋⣴⣟⡵⢺⡏⠁
⠀⠀⠈⢳⣶⣾⠏⣩⡿⠋⠀⠀⡒⠶⣄⡀⠉⢉⠧⠶⢦⡀⠥⢉⣶⣶⠏⣇⠀
⠀⠀⠀⠈⠉⠁⢰⣿⣷⠀⠀⠀⠈⠲⠤⠟⠒⠂⠀⢀⣀⠁⠠⣼⣿⣯⢀⡇⠀
⠀⠀⠀⠀⠀⠀⠸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⡜⠣⠤⢠⣾⣿⣿⠉⣼⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢿⣿⡇⠀⢀⡀⠀⢀⠀⠀⡼⠀⣠⣴⣿⣿⣿⣿⢀⡏⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⣿⣷⡾⠛⠛⠿⣾⣦⣰⣷⡾⠟⣿⣯⢊⡽⣿⠞⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣇⠀⢱⣶⠂⡼⠃⣿⡇⣸⠇⣧⡟⣰⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣶⣼⡯⠞⠁⢠⣿⣷⣿⣰⢏⣴⣿⡿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⣡⡏⣿⢡⡞⣩⡿⠃⠀⠀⠀⠀

██████╗ ███████╗██╗     ███████╗████████╗ █████╗ 
██╔══██╗██╔════╝██║     ██╔════╝╚══██╔══╝██╔══██╗
██║  ██║█████╗  ██║     █████╗     ██║   ███████║
██║  ██║██╔══╝  ██║     ██╔══╝     ██║   ██╔══██║
██████╔╝███████╗███████╗███████╗   ██║   ██║  ██║
╚═════╝ ╚══════╝╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝
"""

print(ascii_art)
print("\n[ Delta Key Bypass Automático REAL ]")
print("Cole abaixo o link encurtado do Delta (começa com 'https://auth.platorelay.com'):\n")

# Entrada do usuário
url = input(">>> ")

print("\n[~] Bypassando o link... Aguarde...\n")
time.sleep(1)

try:
    bypass_api = f"https://bypass.bot.nu/bypass2?url={url}"
    response = requests.get(bypass_api)
    data = response.json()

    if 'destination' in data:
        print("[✓] Bypass completo!")
        print("Link final da key:")
        print(f"\n{data['destination']}\n")
    else:
        print("[X] Falha ao fazer o bypass. Link inválido ou API bloqueada.")
except Exception as err:
    print(f"[ERRO] Ocorreu um problema: {err}")
