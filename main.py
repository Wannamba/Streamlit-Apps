import streamlit as st

import snowflake.connector
import sys
import pandas as pd
from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine

header = st.container()
dataset = st.container()
features = st.container()
model_training =  st.container()

with header:
    st.title('Data source for Volume BRT IT')
    st.text('in this project, ....0')

con = snowflake.connector.connect(
    user="S.PUTRA@SEVENSENDERS.COM", 
    account="rv69958.eu-central-1",
    authenticator="externalbrowser",
    warehouse="SEVENSENDERS_DWH",
    database="TRAINING",
    schema="TRAINING.WANNA"
)
cur = con.cursor()
print(sys.executable)
print(sys.version)
print(sys.version_info)
try:
    cur.execute("select current_date")
    one_row=cur.fetchone()
    print("Current_Date:",one_row[0])
    cur.execute("SELECT current_version()")
    one_row = cur.fetchone()
    print("Snowfalke_Version:",one_row[0])
finally:
    cur.close()
cur.close()

cur=con.cursor()
sql= "SELECT * FROM TRAINING.WANNA.REV_CALC_EXTRACTED"
cur.execute(sql)

df= cur.fetch_pandas_all()
df
