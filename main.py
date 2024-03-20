import shutil
from datetime import datetime, timedelta
import time
import subprocess
from halo import Halo
import os

def run_server():
  """
  Inicia e mantém o servidor Minecraft em execução até a hora do backup.
  """
  # Horário da execução do comando
  now = datetime.now()

  comando = ["java", "-Xmx4G", "-jar", "paper-1.20.2-318.jar"]

  # Definir horário de Backup
  hora_finalizacao = datetime(now.year, now.month, now.day, 5, 0, 0)
  if now.hour >= 5:
    hora_finalizacao += timedelta(days=1)

  diferenca_tempo = hora_finalizacao - now
  tempo_maximo = diferenca_tempo.total_seconds()

  print("\n\n🚀 Servidor iniciado\n\n")
  processo = subprocess.Popen(comando, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

  inicio = time.time()

  try:
    while True:

      tempo_restante = tempo_maximo - (time.time() - inicio)

      if tempo_restante <= 0:
        print("\n🗃️ Hora de fazer backup. Enviando comando 'stop' para parar o servidor...")
        processo.stdin.write("stop\n")
        processo.stdin.flush()
        break
          
  except KeyboardInterrupt:
      print("Interrompendo...")
      processo.terminate()

  time.sleep(10)



def backup():
  """
  Realiza a compressão do arquivo de mundo do Minecraft para backup.
  """

  diretorio_atual = os.getcwd()

  prefixo = "mundo_backup"

  arquivos = os.listdir(diretorio_atual)
  arquivos_com_prefixo = [arquivo for arquivo in arquivos if arquivo.startswith(prefixo)]

  if arquivos_com_prefixo:
    print("📁 Detectado um backup anterior!")

    for arquivo in arquivos_com_prefixo:
      print("❌ Excluindo arquivo anterior de backup...")
      os.remove(os.path.join(diretorio_atual, arquivo))
  else:
    print("✔️ Não foi identificado backup anterior")


  # Horário da execução do comando
  now = datetime.now()

  # Pegar a data atual do backup
  backup_date = now.strftime("%d.%m-%H-%M")

  print(f"💾 Backup às {now.strftime("%H:%M")} do dia {now.strftime("%d/%m/%y")}")
  spinner = Halo(text=f"Realizando backup...", spinner='dots')
  spinner.start()

  # Comprimindo o arquivo do mundo
  nome_do_arquivo_de_backup = f"mundo_backup {backup_date}"
  shutil.make_archive(nome_do_arquivo_de_backup, 'zip', "mundo")

  spinner.stop()

  print("✔️ Backup finalizado!")


if __name__ == '__main__':
  while True:
    run_server()
    backup()
