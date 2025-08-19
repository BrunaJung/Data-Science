import mysql.connector

# Configurações de conexão (substitua com suas credenciais)
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'port': 3307,
}

# Nomes dos bancos de dados
DB_ORIGEM = 'faculdade'
DB_DESTINO = 'BI_Faculdade'

def criar_e_configurar_bi():
    """
    Cria o banco de dados de destino e as tabelas de dimensão e fato,
    conforme o novo modelo estrela.
    """
    conn = None
    cursor = None
    try:
        # Conecta sem especificar o banco de dados para poder criar um novo
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        print(f"Verificando e recriando o banco de dados {DB_DESTINO}...")
        # Adicionei esta linha para garantir que o banco de dados não exista
        cursor.execute(f"DROP DATABASE IF EXISTS {DB_DESTINO}")
        cursor.execute(f"CREATE DATABASE {DB_DESTINO}")

        # Reconecte ao novo banco de dados para garantir que a conexão está ativa
        conn.database = DB_DESTINO

        # Recriando a tabela de dimensão de estudantes
        print("Criando a tabela de dimensão dim_estudante...")
        cursor.execute("DROP TABLE IF EXISTS fato_notas;")
        cursor.execute("DROP TABLE IF EXISTS dim_estudante;")
        cursor.execute("""
            CREATE TABLE dim_estudante (
                tf_estudante BIGINT PRIMARY KEY,
                nome_estudante VARCHAR(255),
                matricula VARCHAR(255)
            );
        """)

        # Recriando a tabela de dimensão de disciplinas
        print("Criando a tabela de dimensão dim_disciplina...")
        cursor.execute("DROP TABLE IF EXISTS dim_disciplina;")
        cursor.execute("""
            CREATE TABLE dim_disciplina (
                tf_disciplina BIGINT PRIMARY KEY,
                nome_disciplina VARCHAR(255) NOT NULL
            );
        """)

        # Recriando a tabela de fatos para as notas
        print("Criando a tabela de fatos fato_notas...")
        cursor.execute("""
            CREATE TABLE fato_notas (
                tf_estudante BIGINT,
                tf_disciplina BIGINT,
                nota DOUBLE,
                FOREIGN KEY (tf_estudante) REFERENCES dim_estudante(tf_estudante),
                FOREIGN KEY (tf_disciplina) REFERENCES dim_disciplina(tf_disciplina)
            );
        """)
        
        conn.commit()
        print("Estrutura do banco de dados BI_Faculdade criada com sucesso.")

    except mysql.connector.Error as err:
        print(f"Erro ao criar a estrutura do banco de dados: {err}")
        if conn:
            conn.rollback()
    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

def carregar_dimensoes():
    """Carrega as tabelas de dimensão de estudantes e disciplinas."""
    conn_origem = None
    conn_destino = None
    cursor_origem = None
    cursor_destino = None
    try:
        conn_origem = mysql.connector.connect(database=DB_ORIGEM, **DB_CONFIG)
        cursor_origem = conn_origem.cursor()
        
        conn_destino = mysql.connector.connect(database=DB_DESTINO, **DB_CONFIG)
        cursor_destino = conn_destino.cursor()

        # Extrai e carrega a dimensão de estudantes
        print("Carregando dim_estudante...")
        # Usa o RGM como chave de fato (tf_estudante) e como número de matrícula
        cursor_origem.execute("SELECT rgm, nome FROM estudantes")
        estudantes = cursor_origem.fetchall()
        
        for rgm, nome in estudantes:
            cursor_destino.execute("""
                INSERT INTO dim_estudante (tf_estudante, nome_estudante, matricula) 
                VALUES (%s, %s, %s)
                ON DUPLICATE KEY UPDATE nome_estudante = VALUES(nome_estudante), matricula = VALUES(matricula)
            """, (rgm, nome, rgm))
        conn_destino.commit()
        print("Dimensão de Estudantes carregada com sucesso.")

        # Extrai e carrega a dimensão de disciplinas
        print("Carregando dim_disciplina...")
        cursor_origem.execute("SELECT codigo, nome_disciplina FROM disciplinas")
        disciplinas = cursor_origem.fetchall()

        for codigo, nome_disciplina in disciplinas:
            cursor_destino.execute("""
                INSERT INTO dim_disciplina (tf_disciplina, nome_disciplina)
                VALUES (%s, %s)
                ON DUPLICATE KEY UPDATE nome_disciplina = VALUES(nome_disciplina)
            """, (codigo, nome_disciplina))
        conn_destino.commit()
        print("Dimensão de Disciplinas carregada com sucesso.")

    except mysql.connector.Error as err:
        print(f"Erro ao carregar as dimensões: {err}")
        if conn_destino:
            conn_destino.rollback()
    finally:
        if cursor_origem: cursor_origem.close()
        if cursor_destino: cursor_destino.close()
        if conn_origem and conn_origem.is_connected(): conn_origem.close()
        if conn_destino and conn_destino.is_connected(): conn_destino.close()

def carregar_tabela_fato_notas():
    """
    Carrega a tabela de fatos 'fato_notas'.
    A consulta de origem junta as tabelas para obter todas as informações necessárias.
    """
    conn_origem = None
    conn_destino = None
    cursor_origem = None
    cursor_destino = None
    try:
        conn_origem = mysql.connector.connect(database=DB_ORIGEM, **DB_CONFIG)
        cursor_origem = conn_origem.cursor()

        conn_destino = mysql.connector.connect(database=DB_DESTINO, **DB_CONFIG)
        cursor_destino = conn_destino.cursor()

        print("Carregando a tabela de fatos fato_notas...")
        query = """
            SELECT
                m.rgm_estudante,
                m.codigo_disciplina,
                nb.nota
            FROM notas_bimestrais nb
            JOIN matriculas m ON nb.id_matricula = m.id;
        """
        cursor_origem.execute(query)
        registros_notas = cursor_origem.fetchall()

        for rgm_estudante, codigo_disciplina, nota in registros_notas:
            cursor_destino.execute("""
                INSERT INTO fato_notas (tf_estudante, tf_disciplina, nota)
                VALUES (%s, %s, %s)
            """, (rgm_estudante, codigo_disciplina, nota))
        
        conn_destino.commit()
        print("Tabela de fatos 'fato_notas' carregada com sucesso.")

    except mysql.connector.Error as err:
        print(f"Erro ao carregar a tabela de fatos: {err}")
        if conn_destino:
            conn_destino.rollback()
    finally:
        if cursor_origem: cursor_origem.close()
        if cursor_destino: cursor_destino.close()
        if conn_origem and conn_origem.is_connected(): conn_origem.close()
        if conn_destino and conn_destino.is_connected(): conn_destino.close()


if __name__ == "__main__":
    criar_e_configurar_bi()
    carregar_dimensoes()
    carregar_tabela_fato_notas()
