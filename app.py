from flask import Flask

from services.chamados import chamados_bp
from services.usuarios import usuarios_bp

app = Flask(__name__)

app.register_blueprint(chamados_bp)
app.register_blueprint(usuarios_bp)

@app.route("/")
def home():
    return {
        "api":"HelpDesk API",
        "versao":"1.0"
    }

if __name__ == "__main__":
    app.run(debug=True)