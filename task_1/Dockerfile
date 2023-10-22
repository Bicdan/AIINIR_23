FROM python:3.11

WORKDIR /code

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./chat /code/chat

CMD ["uvicorn", "chat.main:app", "--host", "0.0.0.0", "--port", "8082", "--reload"]