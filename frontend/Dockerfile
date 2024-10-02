FROM python:3.9

WORKDIR /code

COPY . /code/

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "src/index.py"]
