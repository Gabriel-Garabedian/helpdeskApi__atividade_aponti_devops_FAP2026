from app import app

def test_chamados():

    client=app.test_client()

    resposta=client.get("/chamados")

    assert resposta.status_code==200