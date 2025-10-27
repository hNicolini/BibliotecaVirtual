from app import create_app, db
from app.models import Livro, Usuario

def init_database():
    """Função para inicializar o banco manualmente"""
    app = create_app()
    
    with app.app_context():
        db.create_all()
        print("✅ Banco de dados inicializado!")

if __name__ == '__main__':
    init_database()