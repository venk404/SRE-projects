import psycopg2
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = os.path.join('DB', '.env')

# If the script is not in the /app directory, use an absolute path
if not os.path.exists(env_path):
    env_path = '/app/DB/.env'



load_dotenv(env_path)
db_name = os.getenv('POSTGRES_DB')
db_user = os.getenv('POSTGRES_USER')
db_password = os.getenv('POSTGRES_PASSWORD')
db_host = os.getenv('POSTGRES_HOST')
db_port = os.getenv('POSTGRES_PORT')


while True:
    try:
        print(db_host)
        conn = psycopg2.connect(database=db_name,
                                user=db_user,
                                password=db_password,
                                host=db_host,
                                port=db_port)
        cur = conn.cursor()

        create_student_table = cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            ID SERIAL PRIMARY KEY,
            name VARCHAR(255),
            email VARCHAR(255),
            age INTEGER,
            phone VARCHAR(50)
        );
        """)
        print("Schema Created")
        # Make the changes to the database persistent
        conn.commit()
        # Close cursor and communication with the database
        cur.close()
        conn.close()
        break
    except (Exception, psycopg2.DatabaseError) as error:
        print("Schema Not Created")
        time.sleep(10)
        continue
