import os
import psycopg2

#Insira aqui as informações do seu banco de dados. Veja o schema.sql para visualizar a tabela utilizada.
conn = psycopg2.connect(
    host="localhost",
    database="crud_pessoas",
    user="postgres",
    password="caio123"
)
cursor = conn.cursor()

run = True

def questionario():
    """Cadastra uma nova pessoa no banco"""
    os.system("cls || clear")
    name = input("Insert your name: ")

    os.system("cls || clear")
    age = int(input("Insert your age: "))

    os.system("cls || clear")
    peso = float(input("Insert your weight: "))

    cursor.execute(
        "INSERT INTO pessoas (nome, idade, peso) VALUES (%s, %s, %s)",
        (name, age, peso)
    )
    conn.commit()
    print(f"\n{name} cadastrado com sucesso!")
    input("Pressione ENTER para continuar...")

def show_media():
    """Mostra a média de idade e peso"""
    cursor.execute("SELECT AVG(peso), AVG(idade) FROM pessoas")
    media_peso, media_idade = cursor.fetchone()

    if media_peso:
        print(f"\nMédia de peso: {media_peso:.2f}")
        print(f"Média de idade: {media_idade:.1f}")
    else:
        print("\nNenhuma pessoa cadastrada ainda.")

    input("Pressione ENTER para continuar...")

def listar_pessoas():
    """Lista todas as pessoas cadastradas"""
    cursor.execute("SELECT id, nome, idade, peso FROM pessoas")
    pessoas = cursor.fetchall()

    if pessoas:
        print("\n--- Lista de Pessoas ---")
        for p in pessoas:
            print(f"ID: {p[0]}, Nome: {p[1]}, Idade: {p[2]}, Peso: {p[3]}")
    else:
        print("\nNenhuma pessoa cadastrada ainda.")

    input("Pressione ENTER para continuar...")

def selecao():
    """Menu de seleção"""
    try:
        escolha = int(input("Escolha: "))
    except ValueError:
        print("Escolha inválida!")
        return

    if escolha == 1:
        questionario()
    elif escolha == 2:
        show_media()
    elif escolha == 3:
        listar_pessoas()
    elif escolha == 4:
        global run
        run = False
    else:
        print("Opção inválida!")
        input("Pressione ENTER para continuar...")

def main():
    os.system("cls || clear")
    print("------------------------------------")
    print("-----------Seja bem-vinde-----------")
    print("1. Registrar Usuário")
    print("2. Ver Médias")
    print("3. Listar Pessoas")
    print("4. Sair")
    selecao()

while run:
    main