from flask import Blueprint, request, jsonify
from app import db
from app.models import Livro, Usuario

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return jsonify({
        "message": "Sistema de Biblioteca Acadêmica 🚀",
        "version": "1.0",
        "endpoints": {
            "health": "/health",
            "buscar_livros": "/api/livros?search=termo&categoria=filter",
            "cadastrar_livro": "/api/livros (POST)",
            "detalhes_livro": "/api/livros/<id>"
        }
    })

@main_bp.route('/health')
def health_check():
    return jsonify({"status": "OK", "message": "Sistema operacional"})

@main_bp.route('/api/livros', methods=['GET'])
def buscar_livros():
    try:
        search_term = request.args.get('search', '').strip()
        categoria = request.args.get('categoria', '')
        
        query = Livro.query
        
        if search_term:
            query = query.filter(
                db.or_(
                    Livro.titulo.ilike(f'%{search_term}%'),
                    Livro.autor.ilike(f'%{search_term}%'),
                    Livro.isbn.ilike(f'%{search_term}%')
                )
            )
        
        if categoria:
            query = query.filter(Livro.categoria == categoria)
        
        livros = query.all()
        
        return jsonify({
            "success": True,
            "count": len(livros),
            "livros": [livro.to_dict() for livro in livros]
        })
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@main_bp.route('/api/livros', methods=['POST'])
def cadastrar_livro():
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"success": False, "error": "Dados não fornecidos"}), 400
        
        # Campos obrigatórios
        required_fields = ['isbn', 'titulo', 'autor', 'categoria']
        for field in required_fields:
            if not data.get(field):
                return jsonify({"success": False, "error": f"Campo obrigatório: {field}"}), 400
        
        # Verificar se ISBN já existe
        livro_existente = Livro.query.filter_by(isbn=data['isbn']).first()
        if livro_existente:
            return jsonify({
                "success": False,
                "error": f"ISBN {data['isbn']} já cadastrado",
                "livro_existente": livro_existente.to_dict()
            }), 400
        
        novo_livro = Livro(
            isbn=data['isbn'],
            titulo=data['titulo'],
            autor=data['autor'],
            categoria=data['categoria'],
            editora=data.get('editora'),
            ano_publicacao=data.get('ano_publicacao'),
            quantidade_total=data.get('quantidade_total', 1),
            quantidade_disponivel=data.get('quantidade_total', 1),
            sinopse=data.get('sinopse')
        )
        
        db.session.add(novo_livro)
        db.session.commit()
        
        return jsonify({
            "success": True,
            "message": f"Livro '{novo_livro.titulo}' cadastrado com sucesso!",
            "livro": novo_livro.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "error": str(e)}), 500

@main_bp.route('/api/livros/<int:livro_id>', methods=['GET'])
def detalhes_livro(livro_id):
    try:
        livro = Livro.query.get_or_404(livro_id)
        return jsonify({"success": True, "livro": livro.to_dict()})
    except Exception as e:
        return jsonify({"success": False, "error": "Livro não encontrado"}), 404