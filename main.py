import shutil
from datetime import datetime, timedelta
import time
import subprocess
from halo import Halo
import os

class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'

def run_server():
  """
  Inicia e mantém o servidor Minecraft em execução até a hora do backup.
  """
  # Horário da execução do comando
  now = datetime.now()

  # Pegar a data atual do backup
  date_now = now.strftime(f"{bcolors.OKGREEN}%H:%M{bcolors.ENDC} at {bcolors.OKGREEN}%d/%m/%y")

  comando = ["java", "-Xmx4G", "-jar", "paper-1.20.2-318.jar"]

  # Definir horário de Backup
  hora_finalizacao = datetime(now.year, now.month, now.day, 5, 0, 0)
  if now.hour >= 5:
    hora_finalizacao += timedelta(days=1)

  diferenca_tempo = hora_finalizacao - now
  tempo_maximo = diferenca_tempo.total_seconds()

  print(f"\n\n✔️ Server started at {date_now}!")
  print("""
 ██████╗ ██╗   ██╗ █████╗ ██████╗ ██████╗ ██╗ █████╗ ███╗   ██╗
██╔════╝ ██║   ██║██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗████╗  ██║
██║  ███╗██║   ██║███████║██████╔╝██║  ██║██║███████║██╔██╗ ██║
██║   ██║██║   ██║██╔══██║██╔══██╗██║  ██║██║██╔══██║██║╚██╗██║
╚██████╔╝╚██████╔╝██║  ██║██║  ██║██████╔╝██║██║  ██║██║ ╚████║
 ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
""")
  global processo
  processo = subprocess.Popen(comando, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

  inicio = time.time()

  try:
    while True:

      tempo_restante = tempo_maximo - (time.time() - inicio)

      if tempo_restante <= 0:
        print("\n❌ Server stopped! (Sending 'stop' command to halt the server...)")
        processo.stdin.write("stop\n")
        processo.stdin.flush()
        break
  except KeyboardInterrupt:
      print("❌ (CTRL + C detected!) Halting server... (Sending 'stop' command to stop the server...)")
      processo.stdin.write("stop\n")
      processo.stdin.flush()
      time.sleep(10)

  processo.terminate()



def backup():
  """
  Realiza a compressão do arquivo de mundo do Minecraft para backup.
  """

  try:
    diretorio_atual = os.getcwd()
    print(f"🗃️ Starting backup at {bcolors.OKGREEN}{diretorio_atual}{bcolors.ENDC}")

    prefixo = "mundo_backup"

    arquivos = os.listdir(diretorio_atual)
    arquivos_com_prefixo = [arquivo for arquivo in arquivos if arquivo.startswith(prefixo)]

    if arquivos_com_prefixo:
      print("📁 Previous backup detected!")

      for arquivo in arquivos_com_prefixo:
        print("❌ Deleting previous backup file...")
        os.remove(os.path.join(diretorio_atual, arquivo))
    else:
      print("✔️ No previous backup detected.")


    # Time of command execution
    now = datetime.now()

    # Getting current date of backup
    backup_date = now.strftime("%d.%m-%H-%M")

    print(f"💾 Backup at {now.strftime("%H:%M")} on {now.strftime("%d/%m/%y")}")
    spinner = Halo(text=f"Performing backup...", spinner='dots')
    spinner.start()

    # Compressing the world file
    nome_do_arquivo_de_backup = f"mundo_backup {backup_date}"
    shutil.make_archive(nome_do_arquivo_de_backup, 'zip', "mundo")

    spinner.stop()

    print("✔️ Backup completed!")
  except KeyboardInterrupt:
    print("\n\n❌ (CTRL + C detected!) Stopping backup...")
    processo.terminate()
    os._exit(130)
    


if __name__ == '__main__':
  while True:
    run_server()
    backup()
