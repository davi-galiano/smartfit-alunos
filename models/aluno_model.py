alunos = [
    {"id": 1, "nome": "Lucas Almeida", "cpf": "12345678901", "idade": 20},
    {"id": 2, "nome": "Beatriz Santos", "cpf": "23456789012", "idade": 22},
    {"id": 3, "nome": "Gabriel Ferreira", "cpf": "34567890123", "idade": 19},
    {"id": 4, "nome": "Mariana Oliveira", "cpf": "45678901234", "idade": 21},
    {"id": 5, "nome": "Rafael Costa", "cpf": "56789012345", "idade": 23},
]

def listar_alunos():
    return alunos

def buscar_aluno(id):
    return next((aluno for aluno in alunos if aluno["id"] == id), None)

def adicionar_aluno(novo_aluno):
    alunos.append(novo_aluno)
    return novo_aluno

def atualizar_aluno(id, dados):
    aluno = buscar_aluno(id)
    if aluno:
        aluno.update(dados)
    return aluno

def deletar_aluno(id):
    global alunos
    aluno = buscar_aluno(id)
    if aluno:
        alunos = [a for a in alunos if a["id"] != id]
    return aluno
