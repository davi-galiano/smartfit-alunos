from flask import jsonify, request
from models.aluno_model import listar_alunos, buscar_aluno, adicionar_aluno, atualizar_aluno, deletar_aluno

def get_alunos():
    return jsonify(listar_alunos())

def get_aluno(id):
    aluno = buscar_aluno(id)
    if aluno:
        return jsonify(aluno)
    return jsonify({"erro": "Aluno não encontrado"}), 404

def create_aluno():
    dados = request.get_json()
    novo_aluno = {
        "id": len(listar_alunos()) + 1,
        "nome": dados["nome"],
        "cpf": dados["cpf"],
        "idade": dados["idade"]
    }
    adicionar_aluno(novo_aluno)
    return jsonify(novo_aluno), 201

def update_aluno(id):
    dados = request.get_json()
    aluno = atualizar_aluno(id, dados)
    if aluno:
        return jsonify(aluno)
    return jsonify({"erro": "Aluno não encontrado"}), 404

def delete_aluno(id):
    aluno = deletar_aluno(id)
    if aluno:
        return jsonify({"mensagem": "Aluno excluído com sucesso"})
    return jsonify({"erro": "Aluno não encontrado"}), 404
