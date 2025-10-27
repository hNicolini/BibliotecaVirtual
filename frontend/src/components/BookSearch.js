import React, { useState } from 'react';
import './BookSearch.css';

const BookSearch = ({ onSearchResults, onLoading }) => {
  const [searchTerm, setSearchTerm] = useState('');
  const [categoria, setCategoria] = useState('');

  const handleSearch = async (e) => {
    e.preventDefault();
    onLoading(true);
    
    try {
      const params = new URLSearchParams();
      if (searchTerm) params.append('search', searchTerm);
      if (categoria) params.append('categoria', categoria);
      
      const response = await fetch(`http://localhost:5000/api/livros?${params}`);
      const data = await response.json();
      
      onSearchResults(data.livros || []);
    } catch (error) {
      console.error('Erro na busca:', error);
      alert('Erro ao buscar livros');
    } finally {
      onLoading(false);
    }
  };

  return (
    <div className="book-search">
      <form onSubmit={handleSearch} className="search-form">
        <div className="search-inputs">
          <input
            type="text"
            placeholder="Buscar por título, autor ou ISBN..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="search-input"
          />
          
          <select 
            value={categoria}
            onChange={(e) => setCategoria(e.target.value)}
            className="category-select"
          >
            <option value="">Todas categorias</option>
            <option value="Tecnologia">Tecnologia</option>
            <option value="Literatura">Literatura</option>
            <option value="Ciências">Ciências</option>
            <option value="História">História</option>
            <option value="Matemática">Matemática</option>
          </select>
          
          <button type="submit" className="search-button">
            🔍 Buscar
          </button>
        </div>
      </form>
    </div>
  );
};

export default BookSearch;