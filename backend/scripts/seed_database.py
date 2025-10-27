from app import create_app, db
from app.models import Livro, Usuario

app = create_app()

with app.app_context():
    # Criar tabelas
    db.create_all()
    
    # Adicionar dados de exemplo
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
            sinopse='Uma abordagem para desenvolvimento de software complexo'
        ),
        Livro(
            isbn='978-85-5519-029-4',
            titulo='Clean Code',
            autor='Robert C. Martin',
            categoria='Tecnologia',
            editora='Alta Books',
            ano_publicacao=2009,
            quantidade_total=2,
            quantidade_disponivel=2
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
    
    # Usuário de exemplo
    usuario_admin = Usuario(
        nome='João Silva',
        email='joao@email.com',
        cpf='123.456.789-00',
        tipo='bibliotecario'
    )
    
    db.session.add(usuario_admin)
    db.session.commit()
    
    print("✅ Banco de dados populado com sucesso!")