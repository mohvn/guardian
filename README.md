# Minecraft Server Backup Script - 🛡️ Guardian

Este script Python, denominado Guardian, foi desenvolvido para automatizar a execução de um servidor Minecraft e realizar backups diários do mundo do servidor às 5 horas da manhã.

## Requisitos

- Python 3.x
- Biblioteca `halo` (pode ser instalada via `pip install halo`)

### Execução

1. Certifique-se de ter Python 3.x instalado em seu sistema.
2. Instale a biblioteca `halo` usando o seguinte comando:

```bash
pip install halo
```

3. Coloque o arquivo `paper.jar` no mesmo diretório do script Guardian.
4. Execute o script Guardian com o seguinte comando:

```bash
python Guardian.py
```

5. O servidor Minecraft será iniciado automaticamente e mantido em execução. O backup será realizado todos os dias às 5 horas da manhã.
6. O backup será armazenado no diretório atual com o formato `mundo_backup [data-hora].zip`.

## Preview
![preview](https://i.imgur.com/o1DemYT.png)

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter detalhes.