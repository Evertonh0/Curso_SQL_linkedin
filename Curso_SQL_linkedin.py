# Importando e conectando no database:
import sqlite3
conexao = sqlite3.connect('alunos_politecnica.db')
cursor = conexao.cursor()

# Criando a tabela dentro do database:
cursor.execute("""
  CREATE TABLE IF NOT EXISTS alunos (
    matricula INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    cpf INTEGER
    curso TEXT
  );

""")

# Selecionando os dados da tabela alunos:
cursor.execute("SELECT * FROM alunos;")

# Puxando os dados para o python:
resultados = cursor.fetchall()

# Printando os dados obtidos da tabela alunos:
print('DADOS DA TABELA alunos')
for linha in resultados:
  print(linha)

# Fechando a conexão:
conexao.close()

