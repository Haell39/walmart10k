# Projeto Walmart Sales Data Analysis

Olá, sou Rafael e desenvolvi este projeto para analisar dados de vendas da Walmart. O objetivo foi extrair, limpar e explorar um dataset com 10.000 registros de vendas, utilizando Python e SQL, além de exportar os dados tratados para bancos MySQL e PostgreSQL. A seguir, apresento um resumo do projeto e as instruções básicas para executá-lo.

---

## ✨ Visão Geral

- **Fonte dos Dados:** Baixei o dataset de vendas da Walmart via API do Kaggle.
- **Processamento dos Dados:**  
  - Criação e ativação de ambiente virtual em Python.
  - Download e descompactação dos dados.
  - Limpeza e tratamento dos dados (remoção de duplicatas, tratamento de valores nulos e formatação de colunas, como a conversão de preços para o tipo numérico).
  - Criação de novas colunas, como o cálculo do valor total da venda (unit_price × quantity).

- **Integração com Bancos de Dados:**  
  - Exportação dos dados limpos para MySQL e PostgreSQL utilizando SQLAlchemy.
  - Execução de queries para resolver diversos problemas de negócio, como análise de métodos de pagamento, desempenho por filial e categorização de vendas por turno.

---

## 🛠️ Pré-Requisitos

- **Python** (versão 3.7+)
- **VS Code** ou outro editor de código de sua preferência
- Bibliotecas Python:
  - `pandas`
  - `SQLAlchemy`
  - `pymysql` (para MySQL)
  - `psycopg2` (para PostgreSQL)
- Acesso à API do Kaggle (token de autenticação configurado na pasta `~/.kaggle`)

---

## 🚀 Instalação e Execução

1. **Clone o repositório e acesse o diretório do projeto:**

   ```bash
   git clone https://github.com/seuusuario/projeto-walmart.git
   cd projeto-walmart
   ```

2. **Crie e ative o ambiente virtual:**

   ```bash
   python -m venv meu_ambiente
   source meu_ambiente/bin/activate  # Linux/macOS
   meu_ambiente\Scripts\activate     # Windows
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Baixe o dataset via API do Kaggle:**

   Certifique-se de ter seu token configurado em `~/.kaggle/kaggle.json` e execute:

   ```bash
   kaggle datasets download -d seu_usuario/walmart-sales-data
   unzip walmart-sales-data.zip
   ```

5. **Execute os scripts de limpeza e análise:**

   Abra o projeto no VS Code e execute os notebooks ou scripts Python para:
   - Processar e limpar os dados.
   - Exportar os dados para MySQL e PostgreSQL.
   - Realizar as consultas SQL para solucionar os problemas de negócio.

---

## 📂 Estrutura do Projeto

- **`data/`**: Dataset original e arquivo limpo.
- **`notebooks/`**: Jupyter Notebooks demonstrando cada etapa do projeto.
- **`scripts/`**: Scripts Python para automação da limpeza, exportação e análise.
- **`requirements.txt`**: Lista de bibliotecas necessárias.
- **`README.md`**: Este arquivo.

---

## 🔍 Considerações Finais

Este projeto foi desenvolvido como parte de uma série de desafios SQL. Procuro sempre melhorar meus conhecimentos em manipulação de dados, integração entre ferramentas e análise de negócio. Sinta-se à vontade para explorar, modificar e sugerir melhorias!

---

## 📧 Contato

Se tiver alguma dúvida ou sugestão, entre em contato comigo pelo email: rafaeldutrapro@gmail.com
