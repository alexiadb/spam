#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 09:27:13 2022

@author: alexiadeboynes
"""

import streamlit as st
import pandas as pd



df = pd.read_csv("https://github.com/alexiadb/spam/blob/main/spam.csv", encoding='latin-1').head()
st.write(df)




st.write("""#my first app
         Hello *world*
         """)
     
         

