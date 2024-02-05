from usdarecalls1nf import dfUSDA
import psycopg2

conn = psycopg2.connect(host="localhost", dbname="postgres", user="sbt",
                         password='41998', port=5432)

cur = conn.cursor()

# conn.commit()

# cur.close()
# conn.close()