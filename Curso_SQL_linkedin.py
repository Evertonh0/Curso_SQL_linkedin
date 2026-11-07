# Importando e conectando no database:
import sqlite3
conexao = sqlite3.connect('alunos_politecnica.db')
cursor = conexao.cursor()

# Criando a tabela dentro do database:
cursor.execute("""
  CREATE TABLE IF NOT EXISTS alunos_politecnica (
    matricula INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    cpf INTEGER,
    curso TEXT
  );

""")

# Inserindo dados na tabela:
cursor.execute("INSERT INTO alunos_politecnica (nome, cpf, curso) VALUES ('Fulano de tal', 1234567891011, 'nome do curso');")

# Selecionando os dados da tabela alunos:
cursor.execute("SELECT * FROM alunos_politecnica;")

# Puxando os dados para o python:
resultados = cursor.fetchall()

# Printando os dados obtidos da tabela alunos:
print('DADOS DA TABELA alunos_politecnica')
for linha in resultados:
  print(linha)


