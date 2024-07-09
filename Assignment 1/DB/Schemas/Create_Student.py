import psycopg2
from dotenv import load_dotenv
import os

load_dotenv('./SRE-Simple-RESt-Api/.env')
db_name = os.getenv('POSTGRES_DB')
db_user = os.getenv('POSTGRES_USER')
db_password = os.getenv('POSTGRES_PASSWORD')
db_host = os.getenv('POSTGRES_HOST')
db_port = os.getenv('POSTGRES_PORT')

conn = psycopg2.connect(database=db_name,
                            user=db_user,
                            password=db_password,
                            host=db_host,
                            port=db_port)

cur = conn.cursor()
# Execute a command: create datacamp_courses table
create_student_table = cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    ID SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    age INTEGER,
    phone VARCHAR(50)
);
""")

# Make the changes to the database persistent
conn.commit()
# Close cursor and communication with the database
cur.close()
conn.close()