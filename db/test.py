# import os
# import psycopg2

# conn = psycopg2.connect("postgresql://godsonntungi:RYqUz9J-MRUebzUJgGmw-Q@energy-opt-14560.5xj.gcp-us-central1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full")

# with conn.cursor() as cur:
#     cur.execute("SELECT now()")
#     res = cur.fetchall()
#     conn.commit()
#     print(res)

from models import MachineData
from datetime import datetime


def add_stream_data(data):
    return MachineData.add_stream_data(data)



if __name__=="__main__":

    for i in range (100):
        print(i)
        add_stream_data(
         {"machine_id":"3984324",
    "timestamp":datetime.now(),
    "power":100,
    "current":23,
    "prediction":0})