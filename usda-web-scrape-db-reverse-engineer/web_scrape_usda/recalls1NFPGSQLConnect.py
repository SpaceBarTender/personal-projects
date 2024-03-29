from usdarecalls1nf import dfUSDA
import psycopg2
from sqlalchemy import create_engine
from psycopg2.extras import execute_values
import pandas as pd

# TODO: FIGURE OUT WHERE ACTUAL IDS SHOULD BE- RECALLS TAKE ARE SOURCED FROM
# FACILITY AND APPLY TO ALL IMPACTED PRODUCTS, RECALLID-IMPPROD-ID-IMPROD

conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres",
                         password='41998', port=5432)

cur = conn.cursor()
cur.execute("""DROP TABLE IF EXISTS recallsraw""")
cur.execute("""CREATE TABLE IF NOT EXISTS recallsraw (
            recall_status VARCHAR,
            recall_title VARCHAR,
            reason VARCHAR,
            summary VARCHAR,
            link VARCHAR,
            start_date DATE,
            date_status VARCHAR,
            impacted_product VARCHAR,
            location VARCHAR
);
""")
conn.commit()
cur.close()
conn.close()

#create engine dialect+driver://username:password@server/database
engine = create_engine('postgresql+psycopg2://postgres:41998@localhost/postgres')
print(engine)

#df.to_sql methods: append, fail, replace
dfUSDA.to_sql('recallsraw', engine, if_exists='append', index=False)
   


# # cur.close()
# # conn.close()