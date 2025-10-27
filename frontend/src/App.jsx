import React, { useState } from 'react'
import './App.css'

function App() {
  const [livros, setLivros] = useState([])
  const [loading, setLoading] = useState(false)
  const [searchTerm, setSearchTerm] = useState('')
  const [categoria, setCategoria] = useState('')

  const buscarLivros = async (e) => {
    if (e) e.preventDefault()
    
    setLoading(true)
    
    try {
      const params = new URLSearchParams()
      if (searchTerm) params.append('search', searchTerm)
      if (categoria) params.append('categoria', categoria)
      
      const response = await fetch(`/api/livros?${params}`)
      const data = await response.json()
      
      if (data.success) {
        setLivros(data.livros)
      } else {
        alert('Erro na busca: ' + data.error)
      }
    } catch (error) {
      console.error('Erro:', error)
      alert('Erro ao conectar com o servidor. Verifique se o backend está rodando.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="app">
      <header className="app-header">
        <h1>📚 Biblioteca Acadêmica</h1>
        <p>Sistema de Gestão de Livros - MVP</p>
      </header>
      
      <main className="app-main">
        <form onSubmit={buscarLivros} className="search-form">
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
            
            <button type="submit" className="search-button" disabled={loading}>
              {loading ? '🔍 Buscando...' : '🔍 Buscar Livros'}
            </button>
          </div>
        </form>
        
        <div className="results-section">
          <h2>Resultados da Busca ({livros.length} livros)</h2>
          
          {loading && <div className="loading">Carregando livros...</div>}
          
          {!loading && livros.length === 0 && (
            <div className="no-results">
              {searchTerm || categoria ? 'Nenhum livro encontrado.' : 'Use o campo acima para buscar livros...'}
            </div>
          )}
          
          {!loading && livros.length > 0 && (
            <div className="books-grid">
              {livros.map(livro => (
                <div key={livro.id} className="book-card">
                  <div className="book-title">{livro.titulo}</div>
                  <div className="book-author">
                    <strong>Autor:</strong> {livro.autor}
                  </div>
                  <div className="book-category">
                    <strong>Categoria:</strong> {livro.categoria}
                  </div>
                  <div className="book-isbn">
                    <strong>ISBN:</strong> {livro.isbn}
                  </div>
                  <div className="book-details">
                    <strong>Editora:</strong> {livro.editora || 'Não informada'} • 
                    <strong> Ano:</strong> {livro.ano_publicacao || 'N/I'}
                  </div>
                  <div className={`book-status ${livro.status === 'Disponível' ? 'available' : 'unavailable'}`}>
                    {livro.status} ({livro.quantidade_disponivel}/{livro.quantidade_total} exemplares)
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </main>
    </div>
  )
}

export default App