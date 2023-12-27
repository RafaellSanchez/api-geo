import psycopg2

# Configurações de conexão (substitua com suas credenciais)
dbname = 'projeto-apis'
user = 'agnwwgnn'
password = 'BDIjCyyYYpudjw6ZdaeNfvZ34TjclZUx'
host = 'tuffi.db.elephantsql.com'
port = '5432'  # Porta padrão do PostgreSQL

try:
    # Estabelece a conexão com o banco de dados
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)

    # Cria um cursor para executar operações no banco de dados
    cursor = conn.cursor()

    # Exemplo: executa uma consulta simples para testar a conexão
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print("Conexão bem-sucedida. Versão do banco de dados:", db_version)

    # Fecha o cursor e a conexão
    cursor.close()
    conn.close()

except psycopg2.Error as e:
    print("Erro ao conectar ao banco de dados:", e)
