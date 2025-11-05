# 📚 Sistema de Gestão de Biblioteca Acadêmica

> Projeto acadêmico desenvolvido para a disciplina de Engenharia de Software.  
> Modelagem UML e desenvolvimento de um MVP funcional.

---

## 👥 Equipe

- Henrique Nicolini  
- Bruno Kenez  
- Danilo Cassiano  
- Thiago Montoia  
- Dante Kawazu  

📅 **Data:** 27/10/2025  
🔗 **Repositório:** [Biblioteca Virtual](https://github.com/hNicolini/BibliotecaVirtual)

---

## 🚀 Tecnologias Utilizadas

| Camada | Tecnologia |
|:--------|:------------|
| **Back-end** | Python + Flask |
| **Front-end** | React + Vite |
| **Banco de Dados** | SQLite |
| **Controle de Versão** | Git + GitHub |

---

## ⚙️ Como Executar o Projeto Localmente

### 🔹 Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # ou source venv/bin/activate no Linux/Mac
pip install -r requirements.txt
python run.py
```
Acesse o backend em:
👉 http://localhost:5000

### 🔹 Frontend

```bash
cd frontend
npm install
npm run dev
```

Acesse o frontend em:
👉 http://localhost:3000

## ✅ Funcionalidades Implementadas (MVP)

- 🔍 **Busca de livros** por título, autor ou ISBN  
- 🗂️ **Filtro** por categoria  
- 📖 **Listagem** com status de disponibilidade  
- 💻 **Interface responsiva**

---

## 🧠 Modelagem UML

### 📘 Diagrama de Contexto
O sistema interage com **bibliotecários, alunos e professores** para gerenciar o acervo, empréstimos e reservas, utilizando **banco de dados** e **sistema de e-mail** para notificações.

---

### 🎭 Caso de Uso Crítico — *Realizar Empréstimo (RF03)*

**Ator Principal:** Bibliotecário  

**Pré-condições:**
- Usuário cadastrado e ativo  
- Bibliotecário autenticado  
- Livro disponível no acervo  

**Fluxo Principal:**
1. Bibliotecário seleciona “Realizar Empréstimo”  
2. Sistema exibe formulário  
3. Bibliotecário informa ID do usuário e ISBN do livro  
4. Sistema valida elegibilidade  
5. Sistema verifica disponibilidade  
6. Sistema registra o empréstimo  
7. Atualiza status do exemplar  
8. Gera comprovante  
9. Exibe confirmação  

**Fluxos Alternativos:**
- **FA1:** Usuário com pendências → sistema exibe erro  
- **FA2:** Livro indisponível → sistema sugere reserva  

---

### 🧩 Modelo de Domínio Conceitual

**Principais Entidades:**
- **Usuário:** dados dos usuários  
- **Livro:** metadados do acervo  
- **Exemplar:** instâncias físicas  
- **Empréstimo:** registros de transações  
- **Reserva:** controle de fila de reservas  

---

## 📊 Status da Implementação

| Status | Descrição |
|:--|:--|
| ✅ **Concluído** | Configuração do ambiente, backend Flask, frontend React, banco SQLite, sistema de busca, API REST, interface responsiva |
| 🟡 **Em andamento** | Autenticação, controle de empréstimos, sistema de reservas |
| ❌ **Pendente** | Relatórios administrativos, notificações por e-mail, deploy em produção |

---

## 🎯 Próximos Passos

### 🏗️ Próxima Sprint
- Implementar autenticação JWT  
- Desenvolver controle completo de empréstimos  
- Criar sistema de reservas  
- Adicionar testes unitários  

### 🌐 Futuro
- Implementar notificações por e-mail  
- Desenvolver relatórios administrativos  
- Fazer deploy em ambiente cloud  
- Documentar a API  

