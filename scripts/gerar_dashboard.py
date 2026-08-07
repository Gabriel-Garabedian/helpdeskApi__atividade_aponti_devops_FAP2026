import json

with open("data/chamados.json", encoding="utf-8") as f:

    chamados = json.load(f)

texto = f"""

RELATÓRIO

Chamados cadastrados: {len(chamados)}

"""

with open("relatorio.txt", "w", encoding="utf-8") as f:

    f.write(texto)

print("Relatório gerado.")
