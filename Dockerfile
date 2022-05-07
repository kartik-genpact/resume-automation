FROM python

WORKDIR /app

COPY . ./

RUN pip3 install -r requirements.txt

CMD ["streamlit", "run", "app.py"]