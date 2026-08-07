import shutil
from datetime import datetime

origem = "data/chamados.json"

destino = f"backups/chamados-{datetime.now().strftime('%Y-%m-%d')}.json"

shutil.copy(origem, destino)

print("Backup criado.")
