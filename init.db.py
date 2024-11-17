import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO clientes (empresa, contato, email, telefone, cidade, segmento) VALUES (?, ?, ?, ?, ?, ?)",
            ('Garer','Nina Maria', 'nina@garer.com', '34586324', 'Americana', 'Peças')
            )

cur.execute("INSERT INTO clientes (empresa, contato, email, telefone, cidade, segmento) VALUES (?, ?, ?, ?, ?, ?)",
            ('Marquez','Alexandre Sousa', 'alsousa@marquez.com', '33232324', 'Holambra', 'Automotivo')
            )

cur.execute("INSERT INTO projetos (cliente, servicos, valor, inicio, fim) VALUES (?, ?, ?, ?, ?)",
            ('Garer', 'Teste Laboratório', 5000, '10/11/2024', '30/01/2025')
            )

cur.execute("INSERT INTO projetos (cliente, servicos, valor, inicio, fim) VALUES (?, ?, ?, ?, ?)",
            ('Marquez', 'Instalação sensores', 10000, '10/11/2024', '30/01/2025')
            )

cur.execute("INSERT INTO servicos (descricao, valor, segmento) VALUES (?, ?, ?)",
            ('Teste Laboratório', 5000, 'Laboratório')
            )

cur.execute("INSERT INTO servicos (descricao, valor, segmento) VALUES (?, ?, ?)",
            ('Instalação sensores', 10000, 'Equipamento')
            )

connection.commit()
connection.close()
