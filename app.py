import nltk
import string
import pandas as pd
from nltk import word_tokenize
from nltk.corpus import stopwords
import os
import matplotlib.pyplot as plt
# import sys, fitz
from zipfile import ZipFile
import docx2txt
import streamlit as st
import plotly.graph_objects as go
# import shutil
from openpyxl import load_workbook
from openpyxl.drawing.image import Image
import re
import pymongo
import random
from docx2python import docx2python
# import dns


from analysis import obj

st.set_page_config(initial_sidebar_state='expanded',layout='wide')

client = pymongo.MongoClient(
            "mongodb+srv://admin:pavilion15@cluster0.pefyq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client['ResumeData']
col = db['user_data']

a = col.find({'user': 'admin'})
for i in a:
    admin_pwd = (i['pwd'])

def sign_up():
    new_name = st.text_input('Enter Name:')
    new_username = st.text_input('Enter Username:')
    new_password = st.text_input('Enter Password:', type='password')
    values = [new_name, new_username, new_password]
    new_user = dict(zip(keys, values))
    if st.button('Sign Up'):
        col.insert_one(new_user)
        st.success('User Added! Please refresh and login')

def login():
    username = st.sidebar.text_input('Enter username:')
    passwd = st.sidebar.text_input('Enter password:', type = 'password')
    check = col.find({'username': username})
    for i in check:
        if passwd==i['pwd']:
            return True
        elif passwd=='':
            pass
        else:
            st.sidebar.warning('Incorrect Password')
            return False

keys = ['name', 'username', 'pwd']
st.sidebar.image('mainlogo.png')
option = st.sidebar.radio('Welcome! Provide your credentials:', ['Login', 'Add New User(Admin Only)'])

if option=='Add New User(Admin Only)':
    entered_admin_pwd = st.text_input('Enter Admin Password', type='password')
    if entered_admin_pwd==admin_pwd:
        sign_up()
    elif entered_admin_pwd=='':
        pass
    else:
        st.warning('Incorrect Admin Password')
elif option=='Login':
    if login():
        # st.sidebar.image('mainlogo.png')
        st.image('mainlogo.png')
        st.image(['tagline1.png', 'tagline2.png'] )
        st.title("Internal Employee Detail Summarizer")
        choice = st.radio("What's on your mind ?", ['New Summarization', 'Summarize from DB', 'View DB'])
        if choice=='New Summarization':
            zip_file = st.file_uploader('Upload the Resume ZIP file: ')
            def generate_summary():
                obj.get_experience_db(zip_file)
                (obj.summarize(zip_file))
                obj.mongodb_upload(zip_file)
            if st.button('Start Analysis'):
                st.info('Extracting and Processing the resumes...')
                generate_summary()
                st.header('Excel Report:')
                st.write("Download a Report in Excel format, which comprises of all the detailed analysis and summary of each resume.")
                with open("excel_report.xlsx", "rb") as file:
                     btn = st.download_button(
                         label="Download Excel Report",
                         data=file,
                         file_name="excel_report.xlsx")
        elif choice=='View DB':
            obj.mongodb_view()
        elif choice=='Summarize from DB':
            obj.mongodb_summarize()
