#Teste de conexão com o BD
import psycopg2

#Insira aqui as informações do seu banco de dados. Veja o schema.sql para visualizar a tabela utilizada.
conn = psycopg2.connect(
    host="localhost",
    database="crud_pessoas",
    user="postgres",
    password="caio123"
)

print("Conectado com sucesso!")
conn.close()