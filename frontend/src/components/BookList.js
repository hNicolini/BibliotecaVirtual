import React from 'react';
import './BookList.css';

const BookList = ({ livros, loading }) => {
  if (loading) {
    return <div className="loading">Carregando livros...</div>;
  }

  if (livros.length === 0) {
    return <div className="no-results">Nenhum livro encontrado. Tente outra busca.</div>;
  }

  return (
    <div className="book-list">
      <h2>Resultados da Busca ({livros.length} livros)</h2>
      
      <div className="books-grid">
        {livros.map(livro => (
          <div key={livro.id} className="book-card">
            <div className="book-cover">
              {livro.capa_url ? (
                <img src={livro.capa_url} alt={livro.titulo} />
              ) : (
                <div className="cover-placeholder">📖</div>
              )}
            </div>
            
            <div className="book-info">
              <h3 className="book-title">{livro.titulo}</h3>
              <p className="book-author"><strong>Autor:</strong> {livro.autor}</p>
              <p className="book-category"><strong>Categoria:</strong> {livro.categoria}</p>
              <p className="book-isbn"><strong>ISBN:</strong> {livro.isbn}</p>
              
              <div className={`book-status ${livro.quantidade_disponivel > 0 ? 'available' : 'unavailable'}`}>
                {livro.quantidade_disponivel > 0 ? '✅ Disponível' : '❌ Indisponível'}
              </div>
              
              <button className="details-button">
                Ver Detalhes
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default BookList;