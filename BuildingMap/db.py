import psycopg2

# Database connection details
host = "postgresql-dev-kartai.postgres.database.azure.com"
port = "5432"
database = "kartai_bachelor_2023"
user = "kartai_bachelor_2023@postgresql-dev-kartai"
password = "Io4$7M1e"

# Connect to PostgreSQL database
conn = psycopg2.connect(
    host=host,
    port=port,
    database=database,
    user=user,
    password=password
)

# Create a cursor object
cur = conn.cursor()

# Create buildings table
cur.execute("""
    CREATE TABLE IF NOT EXISTS buildings (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        address VARCHAR(255) NOT NULL,
        latitude FLOAT NOT NULL,
        longitude FLOAT NOT NULL
    )
""")

# Commit changes and close cursor and connection
conn.commit()
cur.close()
conn.close()
