import json

with open("data/chamados.json",encoding="utf-8") as f:

    chamados=json.load(f)

html=f"""

<h1>Dashboard HelpDesk</h1>

<p>Total de chamados: {len(chamados)}</p>

"""

with open("dashboard/index.html","w",encoding="utf-8") as f:

    f.write(html)

print("Dashboard criado.")