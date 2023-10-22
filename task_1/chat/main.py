from fastapi import FastAPI
from pydantic import BaseModel
from chat.model import ChatModel

app = FastAPI()
model = ChatModel()

class UserText(BaseModel):
    message: str
    user_id: str

@app.post("/message")
async def create_item(item: UserText):
    return {'message': item.message, 'result': model(item.message)['result'], 'user_id': item.user_id}