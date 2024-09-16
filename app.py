from flask import Flask, request
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS

from model import Session, Animalzinho

app = Flask(__name__)
CORS(app)

SWAGGER_URL = ''
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Adoção de Animais"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/animalzinhos', methods=['POST'])
def add_animalzinho():
    session = Session()
    new_animalzinho = Animalzinho(
        nome = request.json['nome'],
        especie = request.json['especie'],
        raca = request.json['raca'],
        idade = request.json['idade'],
        descricao = request.json['descricao']
    )
    session.add(new_animalzinho)
    session.commit()
    return 'Animalzinho criado', 201

@app.route('/animalzinhos/<id>', methods=['GET'])
def get_animalzinho(id):
    session = Session()
    animalzinho_encontrado = session.query(Animalzinho).filter(Animalzinho.id == id).first()
    if not animalzinho_encontrado:
        return "Produto não encontrado na base :/", 404
    else:
        return {
        "id": animalzinho_encontrado.id,
        "nome": animalzinho_encontrado.nome,
        "especie": animalzinho_encontrado.especie,
        "raca": animalzinho_encontrado.raca,
        "idade": animalzinho_encontrado.idade,
        "descricao": animalzinho_encontrado.descricao,
    }, 200

@app.route('/animalzinhos', methods=['GET'])
def get_animalzinhos():
    session = Session()
    todos_animalzinhos = session.query(Animalzinho).all()
    if not todos_animalzinhos:
        return {"animalzinhos": []}, 200
    else:
        print(todos_animalzinhos)
        result = []
        for animalzinho in todos_animalzinhos:
            result.append({
                "id": animalzinho.id,
                "nome": animalzinho.nome,
                "especie": animalzinho.especie,
                "raca": animalzinho.raca,
                "idade": animalzinho.idade,
                "descricao": animalzinho.descricao,
            })
        return result, 200

@app.route('/animalzinhos/<id>', methods=['DELETE'])
def delete_animalzinho(id):
    session = Session()
    animalzinho_deletado = session.query(Animalzinho).filter(Animalzinho.id == id).delete()
    session.commit()
    if animalzinho_deletado:
        return "Animalzinho adotado", 204
    else:
        return {"mensagem": "Animalzinho não encontrado :/"}, 404

if __name__ == '__main__':
    app.run(debug=True)
