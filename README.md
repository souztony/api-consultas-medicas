# API de Gerenciamento de Consultas Médicas - Lacrei Saúde 🌈

API RESTful desenvolvida para o desafio técnico da Lacrei Saúde, com o objetivo de facilitar o gerenciamento de profissionais e consultas médicas, promovendo a inclusão e acessibilidade.

## 🚀 Tecnologias Utilizadas

- **Python 3.12+**
- **Django & Django REST Framework**
- **Poetry** (Gerenciamento de dependências)
- **PostgreSQL** (Banco de dados)
- **Docker & Docker Compose** (Containerização)
- **GitHub Actions** (CI/CD)
- **drf-spectacular** (Documentação Swagger/OpenAPI)

---

## 🛠️ Configuração do Ambiente

### Local (com Poetry)

1. **Instale o Poetry** (se não tiver):
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```
2. **Instale as dependências**:
   ```bash
   poetry install
   ```
3. **Configure as variáveis de ambiente**:
   Crie um arquivo `.env` baseado no `.env.example`.
4. **Rode as migrações**:
   ```bash
   poetry run python manage.py migrate
   ```
5. **Inicie o servidor**:
   ```bash
   poetry run python manage.py runserver
   ```

### Docker (Recomendado)

Inicie toda a infraestrutura (API + Banco de Dados) com um comando:
```bash
docker-compose up --build
```
A API estará disponível em `http://localhost:8000`.

---

## 🧪 Testes Automatizados

Os testes foram desenvolvidos utilizando o `APITestCase` do Django.

Para rodar os testes localmente:
```bash
poetry run python manage.py test
```
Via Docker:
```bash
docker-compose exec web python manage.py test
```

---

## 📖 Documentação da API (Swagger)

A documentação interativa está disponível nos seguintes endpoints:
- **Swagger UI**: `http://localhost:8000/api/docs/`
- **Redoc**: `http://localhost:8000/api/redoc/`

---

## ⚙️ CI/CD e Deploy

A pipeline do GitHub Actions (.github/workflows/ci-cd.yml) automatiza o fluxo:
1. **Lint**: Verificação de qualidade de código com `ruff`.
2. **Testes**: Execução dos testes automatizados.
3. **Build**: Criação da imagem Docker.
4. **Deploy**: Placeholder para deploy automatizado na AWS (Staging e Produção).

### Estratégia de Rollback 🔄

Propomos a utilização de **Blue/Green Deployment** via AWS ECS ou App Runner.
Em caso de falha:
1. **Reverter Commit**: O pipeline detecta o revert na branch principal e re-executa o deploy da versão estável anterior.
2. **Tráfego**: O Load Balancer redireciona o tráfego de volta para o ambiente estável (Green) instantaneamente.

---

## 🧠 Justificativas Técnicas

1. **Django REST Framework**: Escolhido pela robustez, ecossistema e facilidade de implementar CRUDs seguros rapidamente.
2. **JWT (SimpleJWT)**: Implementado para garantir autenticação stateless e segura.
3. **Poetry**: Utilizado para garantir reprodutibilidade das dependências e isolamento do ambiente.
4. **PostgreSQL**: Banco de dados relacional padrão da indústria, ideal para garantir integridade via chaves estrangeiras.
5. **Docker Multi-stage**: O Dockerfile foi otimizado para ser leve, instalando apenas o necessário para a execução.

---

## 💳 Integração Assas (Bônus - Proposta)

Para o split de pagamentos:
- **Fluxo**: Ao confirmar uma consulta (`Appointment`), criar uma cobrança na API da Assas.
- **Split**: Configurar o `split` no objeto de cobrança enviando o ID da conta do profissional na Assas.
- **Arquitetura**: Utilizar Webhooks para capturar eventos de pagamento e atualizar o status da consulta no sistema.

---

## 💙 Lacrei Saúde

Este projeto reflete o compromisso com a qualidade técnica e o impacto social. **Código é cuidado.**
