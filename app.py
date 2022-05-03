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
st.sidebar.image('mainlogo.png')
st.image('mainlogo.png')
st.image(['tagline1.png', 'tagline2.png'] )
st.title("Internal Employee Detail Summarizer")
choice = st.sidebar.radio("What's on your mind ?", ['New Summarization', 'Summarize from DB', 'View DB'])
if choice=='New Summarization':
    global zip_file
    zip_file = st.sidebar.file_uploader('Upload the Resume ZIP file: ')
    def generate_summary():
        obj.get_experience_db(zip_file)
        (obj.summarize(zip_file))
        obj.mongodb_upload(zip_file)
    if st.sidebar.button('Start Analysis'):
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
