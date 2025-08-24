#Teste de inserção no BD
import psycopg2

#Insira aqui as informações do seu banco de dados. Veja o schema.sql para visualizar a tabela utilizada.
conn = psycopg2.connect(
    host="localhost",
    database="crud_pessoas",
    user="postgres",
    password="caio123" 
)
cursor = conn.cursor()

pessoas_teste = [
    ("Caio", 25, 70.5),
    ("Ana", 30, 60.2),
    ("João", 28, 80.0)
]

for pessoa in pessoas_teste:
    cursor.execute(
        "INSERT INTO pessoas (nome, idade, peso) VALUES (%s, %s, %s)",
        pessoa
    )
    print(f"{pessoa[0]} cadastrado com sucesso!")

conn.commit()

cursor.close()
conn.close()

print("\nTodos os testes concluídos ✅")