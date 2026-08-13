from flask import Blueprint
from controllers.aluno_controller import get_alunos, get_aluno, create_aluno, update_aluno, delete_aluno

aluno_bp = Blueprint("aluno_bp", __name__, url_prefix="/aluno")

aluno_bp.route("/", methods=["GET"])(get_alunos)
aluno_bp.route("/<int:id>", methods=["GET"])(get_aluno)
aluno_bp.route("/", methods=["POST"])(create_aluno)
aluno_bp.route("/<int:id>", methods=["PUT"])(update_aluno)
aluno_bp.route("/<int:id>", methods=["DELETE"])(delete_aluno)
