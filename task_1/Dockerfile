FROM python:3.11

WORKDIR /chat

RUN pip install --no-cache-dir --upgrade -r /chat/requirements.txt

COPY ./main.py /chat/main.py
COPY ./loader.py /chat/loader.py
COPY ./model.py /chat/model.py
COPY ./tinkoff-terms /chat/tinkoff-terms

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]