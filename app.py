# ncaafb_app.py
import streamlit as st
import pandas as pd
import sqlalchemy
import pymysql

# -----------------------------------
# DATABASE CONNECTION
# -----------------------------------

# Update this with your actual database credentials
DB_USER = "root"      # change as needed
DB_PASSWORD = "Skill@1234"
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "ncaafb_db"

engine = sqlalchemy.create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)