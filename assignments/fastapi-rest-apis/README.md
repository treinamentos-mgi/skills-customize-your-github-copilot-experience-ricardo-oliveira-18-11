# 📘 Atividade: Building REST APIs com FastAPI

## 🎯 Objetivo

Construa uma API REST em Python usando FastAPI. Pratique rotas, métodos HTTP, validação de dados e códigos de status ao criar uma API simples para gerenciar produtos.

## 📝 Tarefas

### 🛠️ Criar os endpoints básicos

#### Descrição

Na pasta desta tarefa, instale FastAPI e Uvicorn com `python -m pip install fastapi uvicorn`. Complete os endpoints básicos no arquivo `starter-code.py` e execute a aplicação com `uvicorn starter-code:app --reload`.

#### Requisitos

O programa concluído deve:

- Responder a `GET /` com uma mensagem JSON identificando a API.
- Responder a `GET /health` com o status `ok`.
- Permitir a consulta da documentação interativa em `/docs`.

### 🛠️ Consultar produtos

#### Descrição

Implemente os endpoints de leitura para listar os produtos cadastrados e consultar um produto pelo identificador. Use os modelos Pydantic fornecidos no starter code.

#### Requisitos

O programa concluído deve:

- Retornar a lista de produtos em `GET /products`.
- Retornar o produto correspondente em `GET /products/{product_id}`.
- Responder com o código HTTP `404` quando o identificador não corresponder a um produto.
- Rejeitar dados inválidos conforme os tipos definidos no modelo de entrada.

### 🛠️ Gerenciar produtos

#### Descrição

Implemente a criação, atualização e remoção de produtos. Use a lista em memória fornecida no starter code como armazenamento.

#### Requisitos

O programa concluído deve:

- Criar produtos por `POST /products` e responder com o código HTTP `201`.
- Atualizar produtos existentes por `PUT /products/{product_id}` e responder com `404` quando o produto não existir.
- Remover produtos por `DELETE /products/{product_id}` e responder com o código HTTP `204` quando a remoção for concluída.
- Responder com `404` ao tentar atualizar ou remover um produto inexistente.
- Gerar identificadores únicos para novos produtos. Os dados podem ser reiniciados quando a aplicação for encerrada.
