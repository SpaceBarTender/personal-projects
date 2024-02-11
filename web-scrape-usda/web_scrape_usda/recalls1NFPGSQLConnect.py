from usdarecalls1nf import dfUSDA
import psycopg2
import sqlalchemy

conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres",
                         password='41998', port=5432)

cur = conn.cursor()
cur.execute("""DROP TABLE IF EXISTS recalls1nf""")
cur.execute("""CREATE TABLE IF NOT EXISTS recalls1nf (
            id SERIAL PRIMARY KEY,
            status VARCHAR (10),
            start_date DATE,
            date_status VARCHAR(10),
            recall_status VARCHAR(10),
            title VARCHAR(100),
            reason VARCHAR(100),
            summary VARCHAR(1000),
            link VARCHAR(200),
            impacted_products VARCHAR(1000),
            location VARCHAR(100)
);
""")

# for row in dfUSDA.iterrows():
#     cur.execute("""INSERT INTO recalls1nf (Satus, Title, Reason, Summary, Link, StartDate, DateStatus, Impacted_Products, Location)
#                 VALUES ()""")

   
conn.commit()

# cur.close()
# conn.close()