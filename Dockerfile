FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY requirements.txt /requirements1.txt
COPY app/notiontoics/requirements.txt /requirements2.txt
RUN pip install -r /requirements1.txt
RUN pip install -r /requirements2.txt


COPY app /app