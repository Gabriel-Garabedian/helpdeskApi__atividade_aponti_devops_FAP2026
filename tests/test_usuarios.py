from app import app

def test_usuarios():

    client=app.test_client()

    resposta=client.get("/usuarios")

    assert resposta.status_code==200