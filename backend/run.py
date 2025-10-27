from app import create_app, db

app = create_app()

def init_database():
    """Inicializa o banco de dados CORRETAMENTE"""
    with app.app_context():
        # ⚠️ REMOVER BANCO ANTIGO E CRIAR NOVO
        try:
            db.drop_all()  # Remove tabelas antigas
            print("🗑️  Tabelas antigas removidas")
        except:
            pass
            
        db.create_all()  # Cria novas tabelas
        print("✅ Novas tabelas criadas")
        
        # Verificar se já existem livros
        from app.models import Livro
        if Livro.query.count() == 0:
            print("📚 Populando banco com dados iniciais...")
            
            livros_exemplo = [
                Livro(
                    isbn='978-85-359-0277-5',
                    titulo='Domain-Driven Design',
                    autor='Eric Evans',
                    categoria='Tecnologia',
                    editora='Alta Books',
                    ano_publicacao=2016,
                    quantidade_total=3,
                    quantidade_disponivel=3,
                    sinopse='Abordagem para desenvolvimento de software complexo'
                ),
                Livro(
                    isbn='978-85-5519-029-4',
                    titulo='Clean Code',
                    autor='Robert C. Martin', 
                    categoria='Tecnologia',
                    editora='Alta Books',
                    ano_publicacao=2009,
                    quantidade_total=2,
                    quantidade_disponivel=2,
                    sinopse='Manual de artesanato em software'
                ),
                Livro(
                    isbn='978-85-725-4697-9',
                    titulo='O Cortiço',
                    autor='Aluísio Azevedo',
                    categoria='Literatura',
                    editora='Penguin Classics',
                    ano_publicacao=1890,
                    quantidade_total=5,
                    quantidade_disponivel=5
                )
            ]
            
            for livro in livros_exemplo:
                db.session.add(livro)
            
            db.session.commit()
            print("✅ Dados iniciais cadastrados!")
        else:
            print("📊 Banco já possui dados")

if __name__ == '__main__':
    print("🚀 Iniciando servidor Flask...")
    print("📍 URL: http://localhost:5000")
    print("🔧 Debug mode: ON")
    
    # Inicializar banco antes de rodar
    init_database()
    
    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=False)