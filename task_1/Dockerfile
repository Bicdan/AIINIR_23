FROM python:3.11

WORKDIR /code

COPY ./chat /code/chat
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

CMD ["uvicorn", "chat.main:app", "--host", "0.0.0.0", "--port", "8082", "--reload"]