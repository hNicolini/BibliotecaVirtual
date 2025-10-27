from app import db
from datetime import datetime

class Livro(db.Model):
    __tablename__ = 'livros'  # ⚠️ NOME EXPLÍCITO DA TABELA
    
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(20), unique=True, nullable=False)
    titulo = db.Column(db.String(200), nullable=False)
    autor = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    editora = db.Column(db.String(100))
    ano_publicacao = db.Column(db.Integer)
    quantidade_total = db.Column(db.Integer, default=1)
    quantidade_disponivel = db.Column(db.Integer, default=1)
    sinopse = db.Column(db.Text)
    data_cadastro = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'isbn': self.isbn,
            'titulo': self.titulo,
            'autor': self.autor,
            'categoria': self.categoria,
            'editora': self.editora,
            'ano_publicacao': self.ano_publicacao,
            'quantidade_total': self.quantidade_total,
            'quantidade_disponivel': self.quantidade_disponivel,
            'status': 'Disponível' if self.quantidade_disponivel > 0 else 'Indisponível',
            'data_cadastro': self.data_cadastro.isoformat() if self.data_cadastro else None
        }

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    cpf = db.Column(db.String(14), unique=True, nullable=False)
    tipo = db.Column(db.String(20), nullable=False)
    ativo = db.Column(db.Boolean, default=True)
    data_cadastro = db.Column(db.DateTime, default=datetime.utcnow)