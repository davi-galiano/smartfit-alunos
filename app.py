from flask import Flask
from routes.aluno_routes import aluno_bp

app = Flask(__name__)
app.register_blueprint(aluno_bp)

if __name__ == "__main__":
    app.run(debug=True)
