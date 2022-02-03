#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 16:04:29 2022

@author: alexiadeboynes
"""


import streamlit as st
import pandas as pd
from gsheetsdb import connect

st.title("My First Streamlit Web App")

df = pd.DataFrame({"one": [1, 2, 3], "two": [4, 5, 6], "three": [7, 8, 9]})
st.write(df)

st.title("Connect to Google Sheets")
gsheet_url = "https://docs.google.com/spreadsheets/d/1FMFVt2piMLi18dYNqjnomnkZgK7mEYjeaF0l8O_JWew/edit?usp=sharing" 
encoding='latin-1'
conn = connect()
rows = conn.execute(f'SELECT * FROM "{gsheet_url}"')
df_gsheet = pd.DataFrame(rows)
st.write(df_gsheet)