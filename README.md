# CRUD de Pessoas - Python + PostgreSQL

## Descrição
Projeto simples de CRUD para gerenciar pessoas (nome, idade, peso), calcular médias e listar registros usando **Python** e **PostgreSQL**.

## Estrutura do Projeto
```
CRUD/
├── backend/
│   ├── main.py
│   ├── insert_test.py
│   ├── test_conn.py
│   └── test_media.py
├── venv/                    # ambiente virtual
├── schema.sql              # script para criar o banco e tabelas
└── README.md
```

- **backend/**: Código Python do backend
- **schema.sql**: Criação do banco e tabela `pessoas`
- **venv/**: Ambiente virtual (não versionado)
- **.gitignore**: Ignora `venv/` e outros arquivos temporários

## Configuração do Banco de Dados

1. **Criar o banco e tabelas**
   - Execute o `schema.sql` no PostgreSQL
   - O script criará:
     - Banco de dados `crud_pessoas`
     - Tabela `pessoas` com campos: id, nome, idade, peso

2. **Configurar conexão**
   - Edite os scripts Python para ajustar `user` e `password` conforme sua configuração do PostgreSQL

## Como Usar

1. **Configurar ambiente virtual**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

2. **Instalar dependências**
   ```bash
   pip install -r requirements.txt
   ```

3. **Executar scripts**
   ```bash
   # Menu interativo principal
   python backend/main.py

   # Inserir dados de teste
   python backend/insert_test.py

   # Ver média calculada
   python backend/test_media.py

   # Testar conexão com o banco
   python backend/test_conn.py
   ```

## Funcionalidades
- Create: Adicionar novas pessoas
- Read: Listar todas as pessoas ou buscar por ID
- Update: Atualizar informações de pessoas existentes
- Delete: Remover pessoas do sistema
- Médias: Calcular média de idade e peso das pessoas cadastradas

## Observações
- Certifique-se de que o PostgreSQL está em execução antes de executar os scripts
- Ajuste as credenciais de conexão no código conforme necessário
- O projeto foi desenvolvido para fins educacionais