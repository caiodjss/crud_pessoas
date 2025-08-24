#Teste de calculo de média com os dados do BD
import psycopg2

#Insira aqui as informações do seu banco de dados. Veja o schema.sql para visualizar a tabela utilizada.
conn = psycopg2.connect(
    host="localhost",
    database="crud_pessoas",
    user="postgres",
    password="caio123"
)
cursor = conn.cursor()

cursor.execute("SELECT AVG(peso), AVG(idade) FROM pessoas;")
media_peso, media_idade = cursor.fetchone()

print(f"Média de peso: {media_peso:.2f}")
print(f"Média de idade: {media_idade:.1f}")

cursor.close()
conn.close()
