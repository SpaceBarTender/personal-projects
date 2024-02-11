from usdarecalls1nf import dfUSDA
import psycopg2
from sqlalchemy import create_engine
from psycopg2.extras import execute_values
import pandas as pd

conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres",
                         password='41998', port=5432)

cur = conn.cursor()
cur.execute("""DROP TABLE IF EXISTS recalls1nf""")
cur.execute("""CREATE TABLE IF NOT EXISTS recalls1nf (
            id SERIAL PRIMARY KEY,
            RecallStatus VARCHAR(10),
            Title VARCHAR(100),
            Reason VARCHAR(100),
            Summary VARCHAR(1000),
            Link VARCHAR(200),
            StartDate DATE,
            DateStatus VARCHAR(10),
            ImpactedProducts VARCHAR(1000),
            Location VARCHAR(100)
);
""")

cur.close()
conn.close()

#create engine dialect+driver://username:password@server/database
# engine = create_engine('postgresql+psycopg2://postgres:41998@localhost/postgres')
# print(engine)

# #df.to_sql methods: append, fail, replace
# dfUSDA.to_sql('recalls1nf', engine, if_exists='append', index=False)
   
# conn.commit()

# # cur.close()
# # conn.close()