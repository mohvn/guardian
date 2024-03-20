# Minecraft Server Backup Script - 🛡️ Guardian

This Python script, named Guardian, has been developed to automate the execution of a Minecraft server and perform daily backups of the server world at 5 o'clock in the morning.

## Requirements

- Python 3.x
- Library `halo` (can be installed via `pip install halo`)

### Execution

1. Make sure you have Python 3.x installed on your system.
2. Install the `halo` library using the following command:

```bash
pip install halo
```
3. Place the `paper.jar` file in the same directory as the Guardian script.
4. Run the Guardian script using the following command:

```bash
python Guardian.py
```

5. The Minecraft server will be automatically started and kept running. The backup will be performed every day at 5 o'clock in the morning.
6. The backup will be stored in the current directory in the format `mundo_backup [date-time].zip`.

## Preview
![preview](https://i.imgur.com/o1DemYT.png)

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.